# ================
# Search patterns
# ================

# Access stratum
Patt_UEacc = "accessStratumRelease ---"
Patt_UEacc_eNB = "accessStratumRelease :  ----"

# LTE UE Categories
Patt_UEcat = "..ue-Category"
Patt_UEcat_eNB = "ue-Category"
# Patt_UEul12 = "..ue-CategoryUL-r12 ---"
# Patt_UEdl12 = "..ue-CategoryDL-r12 ---"
# Patt_UEdl13 = "..ue-CategoryDL-v1330"

# Sasha:
# ue-CategoryDL = [r12:['1','2'], v1330: 23452'']

# Supportet Bands
Patt_SB = ""
Patt_SBtmf = "bandEUTRA --- 0x"
# Patt_SBeNB = "bandEUTRA: ---- 0x"
# eRAN13.1 renew:
Patt_SBeNB = "bandEUTRA :  ---- 0x"

Patt_UtraBands = ""
Patt_UtraBands_tmf = "..SupportedBandUTRA-FDD ---"
Patt_UtraBands_eNB = "SupportedBandUTRA-FDD :  ----"

Patt_GeRANBands = ""
Patt_GeRANBands_tmf = "..SupportedBandGERAN ---"
Patt_GeRANBands_eNB = "SupportedBandGERAN :  ----"

## R12, R1250
Patt_SBr12 = "SupportedBandEUTRA-v12"
Patt_SBr1250 = "SupportedBandEUTRA-v1250"
Patt_ul64 = "ul-64QAM-r12 --- supported"
Patt_ul64_1250 = "ul-64QAM-r12 :  ---- supported"
Patt_ul64tmf = "ul-64QAM-r12 --- supported"
Patt_dl256 = "dl-256QAM-r12 --- supported"
Patt_dl256_1250 = "dl-256QAM-r12 :  ---- supported"
Patt_dl256tmf = "dl-256QAM-r12 --- supported"

## R1430+++
Patt_SBr14 = "supportedBandCombination-v1430"
# "ul-256QAM-r14 :  ---- supported(00)"
Patt_ul256r14 = "ul-256QAM"

# FGI
Patt_FGI8 = ''
Patt_FGI8_tmf = "..featureGroupIndicators ---"
Patt_FGI8_eNB =   "featureGroupIndicators :  ----"

Patt_FGI9 = ''
Patt_FGI9_tmf = "..featureGroupIndRel9Add-r9 ---"
Patt_FGI9_eNB =   "featureGroupIndRel9Add-r9 :  ----"

Patt_FGI9a = ''
Patt_FGI9a_tmf = "..featureGroupIndicators-r9 ---"
Patt_FGI9a_eNB =   "featureGroupIndRel9Add-r9 : ----"

Patt_EUTRA = "..UE-EUTRA-Capability"
Patt_EUTRAv9a0 = "..UE-EUTRA-Capability-v9a0-IEs"
Patt_EUTRA9fdd = "..fdd-Add-UE-EUTRA-Capabilities-r9"
Patt_EUTRA9tdd = "..tdd-Add-UE-EUTRA-Capabilities-r9"

Patt_FGI10 = ''
Patt_FGI10_tmf = "..featureGroupIndRel10-r10 ---"
Patt_FGI10_eNB =   "featureGroupIndRel10-r10 :  ----"

Patt_geranCS = ''
Patt_geranCS_tmf = "..rat-Type --- geran-cs"
Patt_geranCS_eNB = "rat-Type :  ---- geran-cs"

Patt_geranPS = ''
Patt_geranPS_tmf = "..rat-Type --- geran-ps"
Patt_geranPS_eNB = "rat-Type :  ---- geran-ps"

Patt_UTRA = ''
Patt_UTRA_tmf = "..rat-Type --- utra"
Patt_UTRA_eNB = "rat-Type :  ---- utra"

Patt_UERATcap = ''
Patt_UERATcap_tmf = "..ueRATCap ---"
Patt_UERATcap_eNB = "ueRATCap :  ----"

Patt_BWclassUL = ''
Patt_BWclassUL_tmf = "..ca-BandwidthClassUL-r10 ---"
Patt_BWclassUL_eNB =   "ca-BandwidthClassUL-r10 :  ----"

Patt_BWclassDL = ''
Patt_BWclassDL_tmf = "..ca-BandwidthClassDL-r10 ---"
Patt_BWclassDL_eNB =   "ca-BandwidthClassDL-r10 :  ----"

Patt_MIMO = ''
Patt_MIMO_tmf = "..supportedMIMO-CapabilityDL-r10 --"
Patt_MIMO_eNB =   "supportedMIMO-CapabilityDL-r10 :  ----"

Patt_CC10 = ''
Patt_CC10_tmf = "..bandEUTRA-r10 --- 0x"
Patt_CC10_eNB =   "bandEUTRA-r10 :  ---- 0x"

Patt_Band10 = ''
Patt_Band10_tmf = "..bandEUTRA-r10 ---"
Patt_Band10_eNB =   "bandEUTRA-r10 :  ----"

Patt_StartComb =   "..supportedBandCombination-r10"
Patt_StartCombeNB =  "supportedBandCombination-r10"
# Patt_StartComb1270="supportedBandCombination-v1270"

Patt_endComb = "..measParameters-v1020"
Patt_endCombeNB = "measParameters-v1020"
# Patt_endComb1130= "..measParameters-v1130"
Patt_bc = "BandCombinationParameters-r10"
Patt_bc1430 = "BandCombinationParameters-v1430"

# Notes for code:

# print("\n",file=sys.stdout)
# sourceFile = open('python.txt', 'w')
# print("Круто же, правда?", file = sourceFile)
# sourceFile.close()

FGILine1 = "0               1               2"
FGILine2 = "0123456789ABCDEF0123456789ABCDEF0"
FGILine3 = "+---------------+---------------+"


# Custom Fonts, Colors and Fills
FMono = 'Lucida Console'
FSimple = 'GT Walsheim Pro Trial Lt'
FBold = 'GT Walsheim v2 Manual Black'
C_LightYellow = '00FFFFA0'
C_LightGreen =  '00A0FFA0'
C_MGreen =      '0000A000'
C_LBlue =       '00C0C0FF'
DARKBLUE = '00000077'
DARKRED =  '00770000'
YELLOW =   '00FFFF00'
BLACK  =   '00000000'


# Bands filters and XLS conclusions base
PrimaryEUTRABand = 7 # Carrier of LTE band for which "Supported" decision should be made about 256QAM or 4/8 layers supporting
SecondaryEUTRABands = [3,7,20] # Carriers of LTE Bands, which combinations are supported in MF and lab ERANs for special marked output

# Patterns for XLS coloring of used CCs
UsedPat = ['31', '71', '72', '32', '3171', '3271', '3172', '3272', '7171', '7131', '7132', '7231' , '7232', '3131',
           '201', '202', '71201', '72201', '31201', '32201', '3171201','717131','2013131','20132']
UsedPatGreen = ['71', '72', '73', '3171', '7131', '3172', '7231', '3272', '7232', '3173', '7331', '7132', '7332', '3273']
UsedPatCA7C = ['72']

SwitchesNames = ('   FGI out   ', #0    var1
                 '  GERAN out  ', #1    var2
                 '  UTRAN out  ', #2    va3
                 ' 2g3g Binary ', #3    var4
                 ' R14_enabled ', #4    var5
                 'Table output ', #5    var6
                 ' BandsFilter ', #6    var7
                 ' ----------- ', #7    var8
                 ' ----------- ', #8    var9
                 ' ----------- ') #9    var10
                                  # 10: var11
                                    # screen_out = 1
                                    # txt_output = 2
                                    # Excel_out = 3

# Switches defaults
# =================
#bits (fl[])  0  1  2  3  4  5  6  7  8  9  10
DEF_SCR_SW = (1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1)
DEF_TXT_SW = (1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2)
DEF_XLS_SW = (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3)

