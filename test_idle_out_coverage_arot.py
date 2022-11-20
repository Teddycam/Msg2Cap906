import re
import os
import paramiko
import sys
from time import sleep
from datetime import datetime
import yaml
from yaml.loader import BaseLoader


def LoadConfig():
    os.chdir('/home/rotanski/automation')
    setup_file = 'configs/devices.yaml'
    try:
        android_dev = {}
        linux_dev = {}
        atts = {}
        with open(setup_file, 'r') as f:
            config = yaml.load(f, Loader=BaseLoader)
            for key, value in config.items():
                if value.get('type') == 'android':
                    android_dev.update({key:value})
                if value.get('type') == 'linux':
                    linux_dev.update({key:value})
                if value.get('type') == 'attenuator':
                    atts.update({key:value})
                # if config[i].get('type') != 'android' and i != 'linux' and i != 'attenuators':
                #     print('Only "android", "linux" and "attenuators" types are supported. Type "%s" is unknown' % i)
    except FileNotFoundError:
        print('Setup config file "%s" is absent' % setup_file)
        print('Interrupt test and finish')
        sys.exit()
    except yaml.YAMLError as e:
        print(e)
        print('Interrupt test and finish')
        sys.exit()
    return android_dev, linux_dev, atts


def ExecuteADBcommand(android_dev, name, command):
    ssh_ip = android_dev.get(name).get('host')
    ssh_port = android_dev.get(name).get('port')
    ssh_user = android_dev.get(name).get('ssh_user')
    ssh_pwd = android_dev.get(name).get('ssh_pwd')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_ip, port=int(ssh_port), username=ssh_user, password=ssh_pwd)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    stdout = ssh_stdout.readlines() + ssh_stderr.readlines()
    ssh.close()
    return stdout

def ExecuteLinuxcommand(linux_dev, name, command):
    ssh_ip = linux_dev.get(name).get('host')
    ssh_port = linux_dev.get(name).get('port')
    ssh_user = linux_dev.get(name).get('ssh_user')
    ssh_pwd = linux_dev.get(name).get('ssh_pwd')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_ip, port=int(ssh_port), username=ssh_user, password=ssh_pwd)
    command = 'sshpass -p mcn ssh mcn@' + name + ' ' + command + '\n'
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    # stdout = ssh_stdout.read().splitlines() + ssh_stderr.read().splitlines()
    stdout = ssh_stdout.readlines() + ssh_stderr.readlines()
    ssh.close()

    return stdout


def PingParce(input):
    if re.search('unreachable', input[0]):
        # print('No interface for ping')
        return False
    ping_stat = re.split(', ', input[-2])
    ping_sent = re.split(' ', ping_stat[0])
    ping_rcvd = re.split(' ', ping_stat[1])
    if ping_sent[0] == ping_rcvd[0] or int(ping_rcvd[0]) > 0:
        print('Ping OK ', ping_rcvd, ping_sent)
        return True
    else:
        return False


def CheckAndoridDeviceState(android_dev, name):
    cmd = 'adb shell dumpsys telephony.registry|grep mDataConnectionState'
    mobile_state = ExecuteADBcommand(android_dev, name, cmd)
    cmd = 'adb shell ip -br a | grep rmnet'
    intf_state = ExecuteADBcommand(android_dev, name, cmd)
    for i in mobile_state:
        if re.search('mDataConnectionState=2', i):
            # 'mUserMobileDataState = true'
            print('Device is registered')
            mobile = 'up'
        else:
            mobile = 'down'
    try:
        intf = 'down'
        for i in intf_state:
            if i.split()[2]:
                intf = 'up'
                device_ip = i.split()[2].split('/')[0]
    except Exception:
        pass
    if mobile == 'up' and intf == 'up':
        return device_ip
    else:
        # print('Device is not connected')
        return False

def CheckLinuxDeviceState(linux_dev, name):
    cmd = ' ip -br a s wwan0'
    intf_state = ExecuteLinuxcommand(linux_dev, name, cmd)
    try:
        intf = 'down'
        for i in intf_state:
            if i.split()[2]:
                intf = 'up'
                device_ip = i.split()[2].split('/')[0]
    except Exception:
        pass
    if intf == 'up':
        return device_ip
    else:
        # print('Device is not connected')
        return False

def SetAttenuation(atts, value='min'):
    ssh_ip = atts['attenuators'].get('host')
    ssh_port = atts['attenuators'].get('port')
    ssh_user = atts['attenuators'].get('ssh_user')
    ssh_pwd = atts['attenuators'].get('ssh_pwd')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_ip, port=int(ssh_port), username=ssh_user, password=ssh_pwd)
    if value == 'min':
        command = 'sudo python3 /home/mcn/jfwusbpython/zero_att.py'
        for a in range(3):
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            att = []
            for i in range(4):
                att.append(ssh_stdout.readline().split(' ')[-1])
            if att[0] == att[1] == att[2] == att[3]:
                print('\nCoverage state.')
                print(datetime.now())
                print('Attenuation is set to %s' % att[0])
                break
            else:
                print('Attenuation has not been set, one more attempt')
            sleep(1)
        ssh.close()
    elif value == 'max':
        command = 'sudo python3 /home/mcn/jfwusbpython/max_att.py'
        for a in range(3):
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            att = []
            for i in range(4):
                att.append(ssh_stdout.readline().split(' ')[-1])
            if att[0] == att[1] == att[2] == att[3]:
                print('\nOut of coverage state.')
                print(datetime.now())
                print('Attenuation is set to %s' % att[0])
                break
            else:
                print('Attenuation has not been set, one more attempt')
            sleep(1)
        ssh.close()
    else:
        print('The value of attenuation is not correct, only "min" or "max" are accepted')


def PrepareAndoridDevice(android_dev, name):
    # WakeUP device and check device state (airplane ON or OFF)
    cmd1 = 'adb shell input keyevent KEYCODE_WAKEUP; sleep 1; adb shell settings get global airplane_mode_on'
    cmd2= 'adb shell svc data enable'
    try:
        # Get airplane mode status
        airplane = ExecuteADBcommand(android_dev, name, cmd1)
        # Enable mobile data
        ExecuteADBcommand(android_dev, name, cmd2)
    except Exception as e:
        print(e)
        print(datetime.now())
        sys.exit()
    if int(airplane[0]) == 1:
        print("Disable Airplane mode")
        cmd = 'adb shell input swipe 500 0 500 500; sleep 1; adb shell input tap 200 500'
        ExecuteADBcommand(android_dev, name, cmd)
    else:
        print('Reconnect {} to network by airplane ON/OFF'.format(name))
        cmd = 'adb shell input swipe 500 0 500 500; sleep 1; adb shell input tap 200 500; sleep 1; adb shell input tap 200 500'
        ExecuteADBcommand(android_dev, name, cmd)


def ChekDeviceIP(devices, name, wait=10, iter=10):
    print('Start checking obtained IP by %s' %name)
    if devices.get(name).get('type') == 'android':
        for i in range(iter):
            device_ip = CheckAndoridDeviceState(devices, name)
            if device_ip:
                break
            sleep(wait)
            if i == (iter - 1) and not device_ip:
                d = i * wait
                print('{} could not set PDU session during {} second'.format(name, d))
                print('Finishing test')
                print(datetime.now())
                sys.exit()
    if devices.get(name).get('type') == 'linux':
        for i in range(iter):
            device_ip = CheckLinuxDeviceState(devices, name)
            if device_ip:
                break
            sleep(wait)
            if i == (iter - 1) and not device_ip:
                d = i * wait
                print('{} could not set PDU session during {} second'.format(name, d))
                print('Finishing test')
                print(datetime.now())
                sys.exit()
    print('{} obtained {} IP address'.format(name, device_ip))
    if device_ip.split('.', 1)[0] == '51':
        setup_type = 'gr'
    elif device_ip.split('.', 1)[0] == '11':
        setup_type = 'sa'
    else:
        setup_type = False
    return setup_type

def CheckPing(devices, name):
    # Check device obtains IP
    setup_type = ChekDeviceIP(devices, name)
    if setup_type == 'gr':
        ip = '172.26.40.4'
    elif setup_type == 'sa':
        ip = '10.0.0.1'
    else:
        ip = '8.8.8.8'
    if devices.get(name).get('type') == 'android':
        print('Start pinging of {}'.format(ip))
        cmd = 'adb shell ping -c 5 -w 5 ' + ip
        output = ExecuteADBcommand(devices, name, cmd)
        if not PingParce(output):
            print(output)
            print('Ping fails. Interrupt test and finish')
            print(datetime.now())
            sys.exit()
    if devices.get(name).get('type') == 'linux':
        print('Start pinging of {}'.format(ip))
        cmd = ' ping -c 5 -w 5 ' + ip
        output = ExecuteLinuxcommand(devices, name, cmd)
        if not PingParce(output):
            print(output)
            print('Ping fails. Interrupt test and finish')
            print(datetime.now())
            sys.exit()

def OutOfCoverage(android_dev, linux_dev, timeout=60):
    print('\n======Begin Out of Coverage test. Check connectivity')
    # Disable radio (out of coverage)
    SetAttenuation(atts, 'max')
    sleep(timeout)
    # Enable radio (restore coverage)
    SetAttenuation(atts, 'min')
    # Clear counters on ucore
    UcoreCounters(setup_ip, setup_pwd, 'clear')
    # Check device obtains IP
    for name in android_dev:
        # Check ping is OK
        CheckPing(android_dev, name)
    for name in linux_dev:
        # Check ping is OK
        CheckPing(linux_dev, name)

def Idle(android_dev, linux_dev, timeout):
    print('\n======Begin IDLE test. Check connectivity')
    for name in android_dev:
        # Check ping is OK
        # CheckPing(android_dev, name)
        print('Deactivate PDU session on {}'.format(name))
        cmd = 'adb shell svc data disable'
        ExecuteADBcommand(android_dev, name, cmd)
    for name in linux_dev:
        # Check ping is OK
        # CheckPing(linux_dev, name)
        cmd = 'sudo nmcli conn down ' + name
        print('Deactivate PDU session on {}'.format(name))
        ExecuteLinuxcommand(linux_dev, name, cmd)
    print('{}sec IDLE timeout'.format(timeout))
    sleep(timeout)

    for name in android_dev:
        print('Activate PDU session')
        cmd = 'adb shell svc data enable'
        ExecuteADBcommand(android_dev, name, cmd)
        # Check ping is OK
        CheckPing(android_dev, name)
    for name in linux_dev:
        cmd = 'sudo nmcli conn up ' + name
        ExecuteLinuxcommand(linux_dev, name, cmd)
        # Check ping is OK
        CheckPing(linux_dev, name)


def GetSetup(type):
    os.chdir('/home/rotanski/automation')
    setup_file = 'configs/5G_GR_SA.conf.yaml'
    try:
        with open(setup_file, 'r') as f:
            config = yaml.load(f, Loader=BaseLoader)
            ip_list = []
            cm_pwd = []
            for i in config:
                if i.split('-', 1)[1] == type:
                    ip_list.append(config[i].get('address'))
                    cm_pwd.append(config[i].get('cm_pwd'))

    except FileNotFoundError:
        print('Setup config file "%s" is absent' %setup_file)
        print('quiting..')
        sys.exit()
    except yaml.YAMLError as e:
        print(e)
        print('quiting..')
        sys.exit()

    return ip_list, cm_pwd

def GetSliceName(ip, cm_pwd):
    ssh_user = 'mcn'
    ssh_pwd = 'mcn'
    url = ' https://' + ip + ':5443/mcn/v1/slices'
    cmd = 'curl -k --noproxy "*" --digest -u Admin:' + cm_pwd + ' --header "Accept: application/xml" --compressed -X GET '
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=ssh_user, password=ssh_pwd)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd+url)
    stdout = ssh_stdout.readlines() + ssh_stderr.readlines()
    ssh.close()
    for line in stdout:
        if re.search(str('namespace'), line):
            slice_name = line.split('>', 1)[1].split('<', 1)[0]
    return slice_name

def UcoreCounters(setup_ip, setup_pwd, action):

    slice_name = GetSliceName(setup_ip[0], setup_pwd[0])
    kb = "kubectl exec mcn-ctrl-slice-0 -n "
    oam = kb + slice_name + " -- ip a s uc-oam | grep inet | awk '{print$2}' | awk -F '/' '{print$1}'"

    for ip in setup_ip:
        ssh_user = 'mcn'
        ssh_pwd = 'mcn'
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=ssh_user, password=ssh_pwd)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(oam)
        oam_ip = ssh_stdout.readline().splitlines()
        url = '"https://' + oam_ip[0] + ':30106/cli/exec"'
        cmd = ' -it -- curl -u Admin:' + setup_pwd[0] + ' -H "Content-Type: text/plain" -X POST -k ' + url
        clear_counters = kb + slice_name + cmd + ' --data "upf_stats clear '
        read_counters = kb + slice_name + cmd + ' --data "upf_stats rest_req=on '

        if action == 'clear':
            for id in range(1, 3):
                clear = clear_counters + ' id=' + str(id) + '"'
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(clear)
                stdout = ssh_stdout.readlines() + ssh_stderr.readlines()
                # for line in stdout:
                #     print(line)
        elif action == 'get':
            with open('upf_counters.txt', 'w') as f:
                f.write('UPF counters\n')
            for id in range(1, 3):
                read = read_counters + ' id=' + str(id) + '"'
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(read)
                stdout = ssh_stdout.readlines() + ssh_stderr.readlines()
                with open('ucore_counters.txt', 'a') as f:
                    f.write('\nFrom Site:{0} UPF-{1}:\n'.format(ip, id))
                    for line in stdout:
                        f.write(line)
        ssh.close()


android_dev, linux_dev, atts = LoadConfig()
PrepareAndoridDevice(android_dev, 'HuaweiP40')
# Set attenuation to min
SetAttenuation(atts, 'min')
setup_ip, setup_pwd = GetSetup(ChekDeviceIP(android_dev, 'HuaweiP40'))
# OutOfCoverage(android_dev, linux_dev, 10)
Idle(android_dev, linux_dev, 10)

# for i in range(8):
#     print('------------------- test cycle with timeout %s -------------------' % timeout)
#     OutOfCoverageAndroid(android_dev, 'HuaweiP40', server_ip, timeout)
#     IdleAndroid(android_dev, 'HuaweiP40', server_ip, timeout)
#     timeout *= 2
