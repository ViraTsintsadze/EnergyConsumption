# 1) just ones
import tkinter as tk
from tkinter import ttk
import os
import pandas as pd
import numpy as np
import re
from tkinter import filedialog
from tkinter import HORIZONTAL


Color0 = 'alice blue' #Ligtest
Color4 = 'SteelBlue4' #Darkest, more grey then blue

cokebook_file = 'codebook_edited_shortened.xlsx'
path = os.getcwd()
pdCodebook = pd.read_excel(os.path.join(path,cokebook_file), delimiter=',', header=0)
pdVarDescr = pd.DataFrame(pdCodebook, columns = ['Cath #', 'SAS Variable Name', 'Variable Description','Coded Responses' ,'Final Response Set'])
str_entry_indicator=' - '

def add_radiobut(fr, text, variable, value, row_counter):
    widg = tk.Radiobutton(fr, text=text, variable=variable, value=value, bg = Color0)
    widg.grid(column=1, row=row_counter, sticky="W")
    return widg,row_counter+1

def add_entry(fr, text, variable, value, row_counter ):
    widg = tk.Entry(fr, textvariable=variable).grid(column=1, row=row_counter, sticky="W")       
    return widg, row_counter+1

   
def buttonSave_clicked():
    New_Parameters.iloc[0]['FOOTHER'] = FOOTHER_tk_Var.get()
    New_Parameters.iloc[0]['FUELAUX'] = FUELAUX_tk_Var.get()
    New_Parameters.iloc[0]['LPOTHER'] = LPOTHER_tk_Var.get()
    New_Parameters.iloc[0]['UGOTH'] = UGOTH_tk_Var.get()
    New_Parameters.iloc[0]['USEEL'] = USEEL_tk_Var.get()
    New_Parameters.iloc[0]['USEFO'] = USEFO_tk_Var.get()
    New_Parameters.iloc[0]['USELP'] = USELP_tk_Var.get()
    New_Parameters.iloc[0]['USENG'] = USENG_tk_Var.get()
    New_Parameters.iloc[0]['USESOLAR'] = USESOLAR_tk_Var.get()
    New_Parameters.iloc[0]['USEWWAC'] = USEWWAC_tk_Var.get()
    New_Parameters.iloc[0]['FOODPROC'] = FOODPROC_tk_Var.get()
    New_Parameters.iloc[0]['LOCRFRI2'] = LOCRFRI2_tk_Var.get()
    New_Parameters.iloc[0]['STOVEN'] = STOVEN_tk_Var.get()
    New_Parameters.iloc[0]['COLDMA'] = COLDMA_tk_Var.get()
    New_Parameters.iloc[0]['HOTMA'] = HOTMA_tk_Var.get()
    New_Parameters.iloc[0]['NOACDAYS'] = NOACDAYS_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATDAYS'] = NOHEATDAYS_tk_Var.get()
    New_Parameters.iloc[0]['USEWOOD'] = USEWOOD_tk_Var.get()
    New_Parameters.iloc[0]['WDOTHER'] = WDOTHER_tk_Var.get()
    New_Parameters.iloc[0]['WDPELLET'] = WDPELLET_tk_Var.get()
    New_Parameters.iloc[0]['WOODLOGS'] = WOODLOGS_tk_Var.get()
    New_Parameters.iloc[0]['TVONWE2'] = TVONWE2_tk_Var.get()
    New_Parameters.iloc[0]['TVONWD2'] = TVONWD2_tk_Var.get()
    New_Parameters.iloc[0]['TVSIZE2'] = TVSIZE2_tk_Var.get()
    New_Parameters.iloc[0]['TVTYPE2'] = TVTYPE2_tk_Var.get()
    New_Parameters.iloc[0]['TYPERFR2'] = TYPERFR2_tk_Var.get()
    New_Parameters.iloc[0]['DBT1'] = DBT1_tk_Var.get()
    New_Parameters.iloc[0]['DBT99'] = DBT99_tk_Var.get()
    New_Parameters.iloc[0]['DNTHEAT'] = DNTHEAT_tk_Var.get()
    New_Parameters.iloc[0]['EQUIPAUX'] = EQUIPAUX_tk_Var.get()
    New_Parameters.iloc[0]['EQUIPAUXTYPE'] = EQUIPAUXTYPE_tk_Var.get()
    New_Parameters.iloc[0]['INTDATA'] = INTDATA_tk_Var.get()
    New_Parameters.iloc[0]['INTDATAACC'] = INTDATAACC_tk_Var.get()
    New_Parameters.iloc[0]['NHSLDMEM'] = NHSLDMEM_tk_Var.get()
    New_Parameters.iloc[0]['OA_LAT'] = OA_LAT_tk_Var.get()
    New_Parameters.iloc[0]['SIZRFRI2'] = SIZRFRI2_tk_Var.get()
    New_Parameters.iloc[0]['WWACAGE'] = WWACAGE_tk_Var.get()
    New_Parameters.iloc[0]['WSF'] = WSF_tk_Var.get()
    New_Parameters.iloc[0]['GWT'] = GWT_tk_Var.get()
    New_Parameters.iloc[0]['CDD30YR'] = CDD30YR_tk_Var.get()
    New_Parameters.iloc[0]['CDD65'] = CDD65_tk_Var.get()
    New_Parameters.iloc[0]['CDD80'] = CDD80_tk_Var.get()
    New_Parameters.iloc[0]['GNDHDD65'] = GNDHDD65_tk_Var.get()
    New_Parameters.iloc[0]['HDD30YR'] = HDD30YR_tk_Var.get()
    New_Parameters.iloc[0]['HDD50'] = HDD50_tk_Var.get()
    New_Parameters.iloc[0]['HDD65'] = HDD65_tk_Var.get()
    New_Parameters.iloc[0]['IECC_CLIMATE_PUB'] = IECC_CLIMATE_PUB_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST11'] = ENERGYASST11_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST12'] = ENERGYASST12_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST13'] = ENERGYASST13_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST14'] = ENERGYASST14_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST15'] = ENERGYASST15_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASSTOTH'] = ENERGYASSTOTH_tk_Var.get()
    New_Parameters.iloc[0]['PROTHERMAC'] = PROTHERMAC_tk_Var.get()
    New_Parameters.iloc[0]['SWAMPCOL'] = SWAMPCOL_tk_Var.get()
    New_Parameters.iloc[0]['USECENAC'] = USECENAC_tk_Var.get()
    New_Parameters.iloc[0]['BENOTHER'] = BENOTHER_tk_Var.get()
    New_Parameters.iloc[0]['EELIGHTS'] = EELIGHTS_tk_Var.get()
    New_Parameters.iloc[0]['FREEAUDIT'] = FREEAUDIT_tk_Var.get()
    New_Parameters.iloc[0]['NOACHELP'] = NOACHELP_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATHELP'] = NOHEATHELP_tk_Var.get()
    New_Parameters.iloc[0]['PAYHELP'] = PAYHELP_tk_Var.get()
    New_Parameters.iloc[0]['DUALCOOKTFUEL'] = DUALCOOKTFUEL_tk_Var.get()
    New_Parameters.iloc[0]['OUTGRILLFUEL'] = OUTGRILLFUEL_tk_Var.get()
    New_Parameters.iloc[0]['OVENFUEL'] = OVENFUEL_tk_Var.get()
    New_Parameters.iloc[0]['STOVEFUEL'] = STOVEFUEL_tk_Var.get()
    New_Parameters.iloc[0]['FUELH2O'] = FUELH2O_tk_Var.get()
    New_Parameters.iloc[0]['FUELH2O2'] = FUELH2O2_tk_Var.get()
    New_Parameters.iloc[0]['FOPAY'] = FOPAY_tk_Var.get()
    New_Parameters.iloc[0]['LPGPAY'] = LPGPAY_tk_Var.get()
    New_Parameters.iloc[0]['NGPAY'] = NGPAY_tk_Var.get()
    New_Parameters.iloc[0]['AUDIT'] = AUDIT_tk_Var.get()
    New_Parameters.iloc[0]['AUDITCHG'] = AUDITCHG_tk_Var.get()
    New_Parameters.iloc[0]['REBATEAPP'] = REBATEAPP_tk_Var.get()
    New_Parameters.iloc[0]['RECYCAPP'] = RECYCAPP_tk_Var.get()
    New_Parameters.iloc[0]['SMARTMETER'] = SMARTMETER_tk_Var.get()
    New_Parameters.iloc[0]['SMARTTHERM'] = SMARTTHERM_tk_Var.get()
    New_Parameters.iloc[0]['MOISTURE'] = MOISTURE_tk_Var.get()
    New_Parameters.iloc[0]['NOTMOIST'] = NOTMOIST_tk_Var.get()
    New_Parameters.iloc[0]['USEMOISTURE'] = USEMOISTURE_tk_Var.get()
    New_Parameters.iloc[0]['USENOTMOIST'] = USENOTMOIST_tk_Var.get()
    New_Parameters.iloc[0]['EDUCATION'] = EDUCATION_tk_Var.get()
    New_Parameters.iloc[0]['EMPLOYHH'] = EMPLOYHH_tk_Var.get()
    New_Parameters.iloc[0]['HHAGE'] = HHAGE_tk_Var.get()
    New_Parameters.iloc[0]['HHSEX'] = HHSEX_tk_Var.get()
    New_Parameters.iloc[0]['HOUSEHOLDER_RACE'] = HOUSEHOLDER_RACE_tk_Var.get()
    New_Parameters.iloc[0]['MONEYPY'] = MONEYPY_tk_Var.get()
    New_Parameters.iloc[0]['NUMADULT'] = NUMADULT_tk_Var.get()
    New_Parameters.iloc[0]['NUMCHILD'] = NUMCHILD_tk_Var.get()
    New_Parameters.iloc[0]['SDESCENT'] = SDESCENT_tk_Var.get()
    New_Parameters.iloc[0]['ESFREEZE'] = ESFREEZE_tk_Var.get()
    New_Parameters.iloc[0]['ESCWASH'] = ESCWASH_tk_Var.get()
    New_Parameters.iloc[0]['ESDISHW'] = ESDISHW_tk_Var.get()
    New_Parameters.iloc[0]['ESDRYER'] = ESDRYER_tk_Var.get()
    New_Parameters.iloc[0]['ESFRIG'] = ESFRIG_tk_Var.get()
    New_Parameters.iloc[0]['ESLIGHT'] = ESLIGHT_tk_Var.get()
    New_Parameters.iloc[0]['ESWATER'] = ESWATER_tk_Var.get()
    New_Parameters.iloc[0]['ESWIN'] = ESWIN_tk_Var.get()
    New_Parameters.iloc[0]['TEMPGONE'] = TEMPGONE_tk_Var.get()
    New_Parameters.iloc[0]['TEMPGONEAC'] = TEMPGONEAC_tk_Var.get()
    New_Parameters.iloc[0]['TEMPHOME'] = TEMPHOME_tk_Var.get()
    New_Parameters.iloc[0]['TEMPHOMEAC'] = TEMPHOMEAC_tk_Var.get()
    New_Parameters.iloc[0]['TEMPNITE'] = TEMPNITE_tk_Var.get()
    New_Parameters.iloc[0]['TEMPNITEAC'] = TEMPNITEAC_tk_Var.get()
    New_Parameters.iloc[0]['THERMAIN'] = THERMAIN_tk_Var.get()
    New_Parameters.iloc[0]['THERMAINAC'] = THERMAINAC_tk_Var.get()
    New_Parameters.iloc[0]['NUMATTICFAN'] = NUMATTICFAN_tk_Var.get()
    New_Parameters.iloc[0]['NUMCFAN'] = NUMCFAN_tk_Var.get()
    New_Parameters.iloc[0]['NUMFLOORFAN'] = NUMFLOORFAN_tk_Var.get()
    New_Parameters.iloc[0]['NUMWHOLEFAN'] = NUMWHOLEFAN_tk_Var.get()
    New_Parameters.iloc[0]['H2OHEATAPT'] = H2OHEATAPT_tk_Var.get()
    New_Parameters.iloc[0]['MORETHAN1H2O'] = MORETHAN1H2O_tk_Var.get()
    New_Parameters.iloc[0]['WHEATAGE'] = WHEATAGE_tk_Var.get()
    New_Parameters.iloc[0]['WHEATSIZ'] = WHEATSIZ_tk_Var.get()
    New_Parameters.iloc[0]['ATTCHEAT'] = ATTCHEAT_tk_Var.get()
    New_Parameters.iloc[0]['BASEHEAT'] = BASEHEAT_tk_Var.get()
    New_Parameters.iloc[0]['EQUIPAGE'] = EQUIPAGE_tk_Var.get()
    New_Parameters.iloc[0]['EQUIPM'] = EQUIPM_tk_Var.get()
    New_Parameters.iloc[0]['EQUIPMUSE'] = EQUIPMUSE_tk_Var.get()
    New_Parameters.iloc[0]['GARGHEAT'] = GARGHEAT_tk_Var.get()
    New_Parameters.iloc[0]['HEATHOME'] = HEATHOME_tk_Var.get()
    New_Parameters.iloc[0]['INTERNET'] = INTERNET_tk_Var.get()
    New_Parameters.iloc[0]['INTSTREAM'] = INTSTREAM_tk_Var.get()
    New_Parameters.iloc[0]['INWIRELESS'] = INWIRELESS_tk_Var.get()
    New_Parameters.iloc[0]['CABLESAT'] = CABLESAT_tk_Var.get()
    New_Parameters.iloc[0]['COMBODVR'] = COMBODVR_tk_Var.get()
    New_Parameters.iloc[0]['DVD'] = DVD_tk_Var.get()
    New_Parameters.iloc[0]['PLAYSTA'] = PLAYSTA_tk_Var.get()
    New_Parameters.iloc[0]['SEPDVR'] = SEPDVR_tk_Var.get()
    New_Parameters.iloc[0]['TVAUDIOSYS'] = TVAUDIOSYS_tk_Var.get()
    New_Parameters.iloc[0]['VCR'] = VCR_tk_Var.get()
    New_Parameters.iloc[0]['AGECDRYER'] = AGECDRYER_tk_Var.get()
    New_Parameters.iloc[0]['AGECWASH'] = AGECWASH_tk_Var.get()
    New_Parameters.iloc[0]['CWASHER'] = CWASHER_tk_Var.get()
    New_Parameters.iloc[0]['DRYER'] = DRYER_tk_Var.get()
    New_Parameters.iloc[0]['DRYRFUEL'] = DRYRFUEL_tk_Var.get()
    New_Parameters.iloc[0]['DRYRUSE'] = DRYRUSE_tk_Var.get()
    New_Parameters.iloc[0]['APPOTHER'] = APPOTHER_tk_Var.get()
    New_Parameters.iloc[0]['BLENDER'] = BLENDER_tk_Var.get()
    New_Parameters.iloc[0]['COFFEE'] = COFFEE_tk_Var.get()
    New_Parameters.iloc[0]['CROCKPOT'] = CROCKPOT_tk_Var.get()
    New_Parameters.iloc[0]['RICECOOK'] = RICECOOK_tk_Var.get()
    New_Parameters.iloc[0]['TOAST'] = TOAST_tk_Var.get()
    New_Parameters.iloc[0]['TOASTOVN'] = TOASTOVN_tk_Var.get()
    New_Parameters.iloc[0]['TYPEGLASS'] = TYPEGLASS_tk_Var.get()
    New_Parameters.iloc[0]['WALLTYPE'] = WALLTYPE_tk_Var.get()
    New_Parameters.iloc[0]['WINDOWS'] = WINDOWS_tk_Var.get()
    New_Parameters.iloc[0]['WINFRAME'] = WINFRAME_tk_Var.get()
    New_Parameters.iloc[0]['ELCOOL'] = ELCOOL_tk_Var.get()
    New_Parameters.iloc[0]['ELFOOD'] = ELFOOD_tk_Var.get()
    New_Parameters.iloc[0]['ELOTHER'] = ELOTHER_tk_Var.get()
    New_Parameters.iloc[0]['ELWARM'] = ELWARM_tk_Var.get()
    New_Parameters.iloc[0]['ELWATER'] = ELWATER_tk_Var.get()
    New_Parameters.iloc[0]['OCCUPYYRANGE'] = OCCUPYYRANGE_tk_Var.get()
    New_Parameters.iloc[0]['YEARMADERANGE'] = YEARMADERANGE_tk_Var.get()
    New_Parameters.iloc[0]['ATHOME'] = ATHOME_tk_Var.get()
    New_Parameters.iloc[0]['ELPAY'] = ELPAY_tk_Var.get()
    New_Parameters.iloc[0]['ENERGYASST'] = ENERGYASST_tk_Var.get()
    New_Parameters.iloc[0]['KOWNRENT'] = KOWNRENT_tk_Var.get()
    New_Parameters.iloc[0]['NOACBROKE'] = NOACBROKE_tk_Var.get()
    New_Parameters.iloc[0]['NOACEL'] = NOACEL_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATBROKE'] = NOHEATBROKE_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATBULK'] = NOHEATBULK_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATEL'] = NOHEATEL_tk_Var.get()
    New_Parameters.iloc[0]['NOHEATNG'] = NOHEATNG_tk_Var.get()
    New_Parameters.iloc[0]['SCALEB'] = SCALEB_tk_Var.get()
    New_Parameters.iloc[0]['SCALEE'] = SCALEE_tk_Var.get()
    New_Parameters.iloc[0]['SCALEG'] = SCALEG_tk_Var.get()
    New_Parameters.iloc[0]['LGTIN4'] = LGTIN4_tk_Var.get()
    New_Parameters.iloc[0]['LGTINCAN'] = LGTINCAN_tk_Var.get()
    New_Parameters.iloc[0]['LGTINCFL'] = LGTINCFL_tk_Var.get()
    New_Parameters.iloc[0]['LGTINCNTL'] = LGTINCNTL_tk_Var.get()
    New_Parameters.iloc[0]['LGTINLED'] = LGTINLED_tk_Var.get()
    New_Parameters.iloc[0]['LGTINNUM'] = LGTINNUM_tk_Var.get()
    New_Parameters.iloc[0]['LGTOUTCNTL'] = LGTOUTCNTL_tk_Var.get()
    New_Parameters.iloc[0]['LGTOUTNUM'] = LGTOUTNUM_tk_Var.get()
    New_Parameters.iloc[0]['TAXCREDITAPP'] = TAXCREDITAPP_tk_Var.get()
    New_Parameters.iloc[0]['AGEFRZR'] = AGEFRZR_tk_Var.get()
    New_Parameters.iloc[0]['NUMFREEZ'] = NUMFREEZ_tk_Var.get()
    New_Parameters.iloc[0]['SIZFREEZ'] = SIZFREEZ_tk_Var.get()
    New_Parameters.iloc[0]['UPRTFRZR'] = UPRTFRZR_tk_Var.get()
    New_Parameters.iloc[0]['AGECENAC'] = AGECENAC_tk_Var.get()
    New_Parameters.iloc[0]['AIRCOND'] = AIRCOND_tk_Var.get()
    New_Parameters.iloc[0]['ATTCCOOL'] = ATTCCOOL_tk_Var.get()
    New_Parameters.iloc[0]['BASECOOL'] = BASECOOL_tk_Var.get()
    New_Parameters.iloc[0]['CENACHP'] = CENACHP_tk_Var.get()
    New_Parameters.iloc[0]['COOLTYPE'] = COOLTYPE_tk_Var.get()
    New_Parameters.iloc[0]['GARGCOOL'] = GARGCOOL_tk_Var.get()
    New_Parameters.iloc[0]['NUMBERAC'] = NUMBERAC_tk_Var.get()
    New_Parameters.iloc[0]['PROTHERM'] = PROTHERM_tk_Var.get()
    New_Parameters.iloc[0]['CELLPHONE'] = CELLPHONE_tk_Var.get()
    New_Parameters.iloc[0]['DESKTOP'] = DESKTOP_tk_Var.get()
    New_Parameters.iloc[0]['ELPERIPH'] = ELPERIPH_tk_Var.get()
    New_Parameters.iloc[0]['NUMLAPTOP'] = NUMLAPTOP_tk_Var.get()
    New_Parameters.iloc[0]['NUMSMPHONE'] = NUMSMPHONE_tk_Var.get()
    New_Parameters.iloc[0]['NUMTABLET'] = NUMTABLET_tk_Var.get()
    New_Parameters.iloc[0]['TVCOLOR'] = TVCOLOR_tk_Var.get()
    New_Parameters.iloc[0]['TVONWD1'] = TVONWD1_tk_Var.get()
    New_Parameters.iloc[0]['TVONWE1'] = TVONWE1_tk_Var.get()
    New_Parameters.iloc[0]['TVSIZE1'] = TVSIZE1_tk_Var.get()
    New_Parameters.iloc[0]['TVTYPE1'] = TVTYPE1_tk_Var.get()
    New_Parameters.iloc[0]['AGEDW'] = AGEDW_tk_Var.get()
    New_Parameters.iloc[0]['DISHWASH'] = DISHWASH_tk_Var.get()
    New_Parameters.iloc[0]['DWASHUSE'] = DWASHUSE_tk_Var.get()
    New_Parameters.iloc[0]['DWCYCLE'] = DWCYCLE_tk_Var.get()
    New_Parameters.iloc[0]['RNSETEMP'] = RNSETEMP_tk_Var.get()
    New_Parameters.iloc[0]['TOPFRONT'] = TOPFRONT_tk_Var.get()
    New_Parameters.iloc[0]['WASHLOAD'] = WASHLOAD_tk_Var.get()
    New_Parameters.iloc[0]['WASHTEMP'] = WASHTEMP_tk_Var.get()
    New_Parameters.iloc[0]['AMTMICRO'] = AMTMICRO_tk_Var.get()
    New_Parameters.iloc[0]['COOKTUSE'] = COOKTUSE_tk_Var.get()
    New_Parameters.iloc[0]['DUALOVENFUEL'] = DUALOVENFUEL_tk_Var.get()
    New_Parameters.iloc[0]['MICRO'] = MICRO_tk_Var.get()
    New_Parameters.iloc[0]['NUMMEAL'] = NUMMEAL_tk_Var.get()
    New_Parameters.iloc[0]['OUTGRILL'] = OUTGRILL_tk_Var.get()
    New_Parameters.iloc[0]['OVEN'] = OVEN_tk_Var.get()
    New_Parameters.iloc[0]['OVENUSE'] = OVENUSE_tk_Var.get()
    New_Parameters.iloc[0]['SEPCOOKTUSE'] = SEPCOOKTUSE_tk_Var.get()
    New_Parameters.iloc[0]['SEPOVENUSE'] = SEPOVENUSE_tk_Var.get()
    New_Parameters.iloc[0]['STOVE'] = STOVE_tk_Var.get()
    New_Parameters.iloc[0]['AGERFRI1'] = AGERFRI1_tk_Var.get()
    New_Parameters.iloc[0]['AGERFRI2'] = AGERFRI2_tk_Var.get()
    New_Parameters.iloc[0]['ICE'] = ICE_tk_Var.get()
    New_Parameters.iloc[0]['NUMFRIG'] = NUMFRIG_tk_Var.get()
    New_Parameters.iloc[0]['SIZRFRI1'] = SIZRFRI1_tk_Var.get()
    New_Parameters.iloc[0]['TYPERFR1'] = TYPERFR1_tk_Var.get()
    New_Parameters.iloc[0]['ALTFUELPEV'] = ALTFUELPEV_tk_Var.get()
    New_Parameters.iloc[0]['BACKUP'] = BACKUP_tk_Var.get()
    New_Parameters.iloc[0]['OUTLET'] = OUTLET_tk_Var.get()
    New_Parameters.iloc[0]['SOLAR'] = SOLAR_tk_Var.get()
    New_Parameters.iloc[0]['FUELPOOL'] = FUELPOOL_tk_Var.get()
    New_Parameters.iloc[0]['FUELTUB'] = FUELTUB_tk_Var.get()
    New_Parameters.iloc[0]['MONPOOL'] = MONPOOL_tk_Var.get()
    New_Parameters.iloc[0]['MONTUB'] = MONTUB_tk_Var.get()
    New_Parameters.iloc[0]['POOL'] = POOL_tk_Var.get()
    New_Parameters.iloc[0]['RECBATH'] = RECBATH_tk_Var.get()
    New_Parameters.iloc[0]['SWIMPOOL'] = SWIMPOOL_tk_Var.get()
    New_Parameters.iloc[0]['ADQINSUL'] = ADQINSUL_tk_Var.get()
    New_Parameters.iloc[0]['DOOR1SUM'] = DOOR1SUM_tk_Var.get()
    New_Parameters.iloc[0]['DRAFTY'] = DRAFTY_tk_Var.get()
    New_Parameters.iloc[0]['HIGHCEIL'] = HIGHCEIL_tk_Var.get()
    New_Parameters.iloc[0]['ROOFTYPE'] = ROOFTYPE_tk_Var.get()
    New_Parameters.iloc[0]['FOWARM'] = FOWARM_tk_Var.get()
    New_Parameters.iloc[0]['FOWATER'] = FOWATER_tk_Var.get()
    New_Parameters.iloc[0]['LPCOOK'] = LPCOOK_tk_Var.get()
    New_Parameters.iloc[0]['LPWARM'] = LPWARM_tk_Var.get()
    New_Parameters.iloc[0]['LPWATER'] = LPWATER_tk_Var.get()
    New_Parameters.iloc[0]['SOLOTHER'] = SOLOTHER_tk_Var.get()
    New_Parameters.iloc[0]['SOLWATER'] = SOLWATER_tk_Var.get()
    New_Parameters.iloc[0]['UGASHERE'] = UGASHERE_tk_Var.get()
    New_Parameters.iloc[0]['UGCOOK'] = UGCOOK_tk_Var.get()
    New_Parameters.iloc[0]['UGWARM'] = UGWARM_tk_Var.get()
    New_Parameters.iloc[0]['UGWATER'] = UGWATER_tk_Var.get()
    New_Parameters.iloc[0]['WDWARM'] = WDWARM_tk_Var.get()
    New_Parameters.iloc[0]['WDWATER'] = WDWATER_tk_Var.get()
    New_Parameters.iloc[0]['NHAFBATH'] = NHAFBATH_tk_Var.get()
    New_Parameters.iloc[0]['OTHROOMS'] = OTHROOMS_tk_Var.get()
    New_Parameters.iloc[0]['TOTCSQFT'] = TOTCSQFT_tk_Var.get()
    New_Parameters.iloc[0]['TOTHSQFT'] = TOTHSQFT_tk_Var.get()
    New_Parameters.iloc[0]['ATTIC'] = ATTIC_tk_Var.get()
    New_Parameters.iloc[0]['ATTICFIN'] = ATTICFIN_tk_Var.get()
    New_Parameters.iloc[0]['BASEFIN'] = BASEFIN_tk_Var.get()
    New_Parameters.iloc[0]['BEDROOMS'] = BEDROOMS_tk_Var.get()
    New_Parameters.iloc[0]['CELLAR'] = CELLAR_tk_Var.get()
    New_Parameters.iloc[0]['NCOMBATH'] = NCOMBATH_tk_Var.get()
    New_Parameters.iloc[0]['PRKGPLC1'] = PRKGPLC1_tk_Var.get()
    New_Parameters.iloc[0]['SIZEOFGARAGE'] = SIZEOFGARAGE_tk_Var.get()
    New_Parameters.iloc[0]['STORIES'] = STORIES_tk_Var.get()
    New_Parameters.iloc[0]['STUDIO'] = STUDIO_tk_Var.get()
    New_Parameters.iloc[0]['TOTROOMS'] = TOTROOMS_tk_Var.get()
    New_Parameters.iloc[0]['TOTSQFT_EN'] = TOTSQFT_EN_tk_Var.get()
    New_Parameters.iloc[0]['CLIMATE_REGION_PUB'] = CLIMATE_REGION_PUB_tk_Var.get()
    New_Parameters.iloc[0]['DIVISION'] = DIVISION_tk_Var.get()
    New_Parameters.iloc[0]['METROMICRO'] = METROMICRO_tk_Var.get()
    New_Parameters.iloc[0]['REGIONC'] = REGIONC_tk_Var.get()
    New_Parameters.iloc[0]['TYPEHUQ'] = TYPEHUQ_tk_Var.get()
    New_Parameters.iloc[0]['UATYP10'] = UATYP10_tk_Var.get()# 3) just ones
    savefile = filedialog.asksaveasfilename(title = "Choose file", filetypes = (('CSV files','*.csv'),))
    if not'.csv' in savefile:
        savefile=savefile+'.csv'
    New_Parameters.to_csv(savefile, index=False)
    return New_Parameters
    
row_counter=0
SAS_Var_N_List = pdVarDescr['SAS Variable Name'].to_list()
New_Parameters = pd.DataFrame(np.zeros((1,len(SAS_Var_N_List))), columns = SAS_Var_N_List)

windowEdit = tk.Tk()
windowEdit.configure(background=Color0)

Tab_control = ttk.Notebook(windowEdit)# 4) iterate over Tabs_list: Loc = Tabs_list[i]
tabLoc = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabLoc, text= "Loc")
##############################################################################################################

SAS_Var_Name='CLIMATE_REGION_PUB'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CLIMATE_REGION_PUB_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=CLIMATE_REGION_PUB_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=CLIMATE_REGION_PUB_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DIVISION'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DIVISION_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=DIVISION_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=DIVISION_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='METROMICRO'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

METROMICRO_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=METROMICRO_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=METROMICRO_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='REGIONC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

REGIONC_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=REGIONC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=REGIONC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TYPEHUQ'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TYPEHUQ_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=TYPEHUQ_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=TYPEHUQ_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UATYP10'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UATYP10_tk_Var = tk.IntVar()
tk.Label(tabLoc, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLoc, text=Text, variable=UATYP10_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLoc, text=Text, variable=UATYP10_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLoc, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: HouseType = Tabs_list[i]
tabHouseType = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabHouseType, text= "HouseType")
##############################################################################################################

SAS_Var_Name='NHAFBATH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NHAFBATH_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=NHAFBATH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=NHAFBATH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OTHROOMS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OTHROOMS_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=OTHROOMS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=OTHROOMS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOTCSQFT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOTCSQFT_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=TOTCSQFT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=TOTCSQFT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOTHSQFT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOTHSQFT_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=TOTHSQFT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=TOTHSQFT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ATTIC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ATTIC_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=ATTIC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=ATTIC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ATTICFIN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ATTICFIN_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=ATTICFIN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=ATTICFIN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BASEFIN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BASEFIN_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=BASEFIN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=BASEFIN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BEDROOMS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BEDROOMS_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=BEDROOMS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=BEDROOMS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CELLAR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CELLAR_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=CELLAR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=CELLAR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NCOMBATH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NCOMBATH_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=NCOMBATH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=NCOMBATH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='PRKGPLC1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

PRKGPLC1_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=PRKGPLC1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=PRKGPLC1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SIZEOFGARAGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SIZEOFGARAGE_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=SIZEOFGARAGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=SIZEOFGARAGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='STORIES'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

STORIES_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=STORIES_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=STORIES_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='STUDIO'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

STUDIO_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=STUDIO_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=STUDIO_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOTROOMS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOTROOMS_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=TOTROOMS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=TOTROOMS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOTSQFT_EN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOTSQFT_EN_tk_Var = tk.IntVar()
tk.Label(tabHouseType, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseType, text=Text, variable=TOTSQFT_EN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseType, text=Text, variable=TOTSQFT_EN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseType, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: EnSource = Tabs_list[i]
tabEnSource = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabEnSource, text= "EnSource")
##############################################################################################################

SAS_Var_Name='FOWARM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FOWARM_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=FOWARM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=FOWARM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='FOWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FOWATER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=FOWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=FOWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LPCOOK'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LPCOOK_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=LPCOOK_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=LPCOOK_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LPWARM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LPWARM_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=LPWARM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=LPWARM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LPWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LPWATER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=LPWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=LPWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SOLOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SOLOTHER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=SOLOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=SOLOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SOLWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SOLWATER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=SOLWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=SOLWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UGASHERE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UGASHERE_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=UGASHERE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=UGASHERE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UGCOOK'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UGCOOK_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=UGCOOK_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=UGCOOK_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UGWARM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UGWARM_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=UGWARM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=UGWARM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UGWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UGWATER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=UGWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=UGWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WDWARM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WDWARM_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=WDWARM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=WDWARM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WDWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WDWATER_tk_Var = tk.IntVar()
tk.Label(tabEnSource, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnSource, text=Text, variable=WDWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnSource, text=Text, variable=WDWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnSource, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Doors = Tabs_list[i]
tabDoors = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabDoors, text= "Doors")
##############################################################################################################

SAS_Var_Name='ADQINSUL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ADQINSUL_tk_Var = tk.IntVar()
tk.Label(tabDoors, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDoors, text=Text, variable=ADQINSUL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDoors, text=Text, variable=ADQINSUL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDoors, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DOOR1SUM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DOOR1SUM_tk_Var = tk.IntVar()
tk.Label(tabDoors, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDoors, text=Text, variable=DOOR1SUM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDoors, text=Text, variable=DOOR1SUM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDoors, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DRAFTY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DRAFTY_tk_Var = tk.IntVar()
tk.Label(tabDoors, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDoors, text=Text, variable=DRAFTY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDoors, text=Text, variable=DRAFTY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDoors, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HIGHCEIL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HIGHCEIL_tk_Var = tk.IntVar()
tk.Label(tabDoors, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDoors, text=Text, variable=HIGHCEIL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDoors, text=Text, variable=HIGHCEIL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDoors, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ROOFTYPE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ROOFTYPE_tk_Var = tk.IntVar()
tk.Label(tabDoors, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDoors, text=Text, variable=ROOFTYPE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDoors, text=Text, variable=ROOFTYPE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDoors, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: SwimPool = Tabs_list[i]
tabSwimPool = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabSwimPool, text= "SwimPool")
##############################################################################################################

SAS_Var_Name='FUELPOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FUELPOOL_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=FUELPOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=FUELPOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='FUELTUB'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FUELTUB_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=FUELTUB_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=FUELTUB_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='MONPOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MONPOOL_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=MONPOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=MONPOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='MONTUB'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MONTUB_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=MONTUB_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=MONTUB_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='POOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

POOL_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=POOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=POOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='RECBATH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

RECBATH_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=RECBATH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=RECBATH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SWIMPOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SWIMPOOL_tk_Var = tk.IntVar()
tk.Label(tabSwimPool, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSwimPool, text=Text, variable=SWIMPOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSwimPool, text=Text, variable=SWIMPOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSwimPool, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: ElectCar = Tabs_list[i]
tabElectCar = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabElectCar, text= "ElectCar")
##############################################################################################################

SAS_Var_Name='DBT1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DBT1_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=DBT1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=DBT1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DBT99'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DBT99_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=DBT99_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=DBT99_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='INTDATA'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

INTDATA_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=INTDATA_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=INTDATA_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='INTDATAACC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

INTDATAACC_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=INTDATAACC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=INTDATAACC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ALTFUELPEV'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ALTFUELPEV_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=ALTFUELPEV_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=ALTFUELPEV_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BACKUP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BACKUP_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=BACKUP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=BACKUP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OUTLET'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OUTLET_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=OUTLET_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=OUTLET_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SOLAR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SOLAR_tk_Var = tk.IntVar()
tk.Label(tabElectCar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectCar, text=Text, variable=SOLAR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectCar, text=Text, variable=SOLAR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectCar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Fridge = Tabs_list[i]
tabFridge = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabFridge, text= "Fridge")
##############################################################################################################

SAS_Var_Name='AGERFRI1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGERFRI1_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=AGERFRI1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=AGERFRI1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='AGERFRI2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGERFRI2_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=AGERFRI2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=AGERFRI2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ICE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ICE_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=ICE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=ICE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMFRIG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMFRIG_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=NUMFRIG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=NUMFRIG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SIZRFRI1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SIZRFRI1_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=SIZRFRI1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=SIZRFRI1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TYPERFR1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TYPERFR1_tk_Var = tk.IntVar()
tk.Label(tabFridge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFridge, text=Text, variable=TYPERFR1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFridge, text=Text, variable=TYPERFR1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFridge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Cook = Tabs_list[i]
tabCook = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabCook, text= "Cook")
##############################################################################################################

SAS_Var_Name='AMTMICRO'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AMTMICRO_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=AMTMICRO_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=AMTMICRO_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='COOKTUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

COOKTUSE_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=COOKTUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=COOKTUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DUALOVENFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DUALOVENFUEL_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=DUALOVENFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=DUALOVENFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='MICRO'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MICRO_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=MICRO_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=MICRO_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMMEAL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMMEAL_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=NUMMEAL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=NUMMEAL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OUTGRILL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OUTGRILL_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=OUTGRILL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=OUTGRILL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OVEN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OVEN_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=OVEN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=OVEN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OVENUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OVENUSE_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=OVENUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=OVENUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SEPCOOKTUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SEPCOOKTUSE_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=SEPCOOKTUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=SEPCOOKTUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SEPOVENUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SEPOVENUSE_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=SEPOVENUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=SEPOVENUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='STOVE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

STOVE_tk_Var = tk.IntVar()
tk.Label(tabCook, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCook, text=Text, variable=STOVE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCook, text=Text, variable=STOVE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCook, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Dish = Tabs_list[i]
tabDish = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabDish, text= "Dish")
##############################################################################################################

SAS_Var_Name='AGEDW'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGEDW_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=AGEDW_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=AGEDW_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DISHWASH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DISHWASH_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=DISHWASH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=DISHWASH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DWASHUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DWASHUSE_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=DWASHUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=DWASHUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DWCYCLE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DWCYCLE_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=DWCYCLE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=DWCYCLE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='RNSETEMP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

RNSETEMP_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=RNSETEMP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=RNSETEMP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOPFRONT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOPFRONT_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=TOPFRONT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=TOPFRONT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WASHLOAD'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WASHLOAD_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=WASHLOAD_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=WASHLOAD_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WASHTEMP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WASHTEMP_tk_Var = tk.IntVar()
tk.Label(tabDish, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDish, text=Text, variable=WASHTEMP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDish, text=Text, variable=WASHTEMP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDish, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: TV = Tabs_list[i]
tabTV = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabTV, text= "TV")
##############################################################################################################

SAS_Var_Name='TVCOLOR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVCOLOR_tk_Var = tk.IntVar()
tk.Label(tabTV, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV, text=Text, variable=TVCOLOR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV, text=Text, variable=TVCOLOR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVONWD1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVONWD1_tk_Var = tk.IntVar()
tk.Label(tabTV, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV, text=Text, variable=TVONWD1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV, text=Text, variable=TVONWD1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVONWE1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVONWE1_tk_Var = tk.IntVar()
tk.Label(tabTV, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV, text=Text, variable=TVONWE1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV, text=Text, variable=TVONWE1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVSIZE1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVSIZE1_tk_Var = tk.IntVar()
tk.Label(tabTV, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV, text=Text, variable=TVSIZE1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV, text=Text, variable=TVSIZE1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVTYPE1'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVTYPE1_tk_Var = tk.IntVar()
tk.Label(tabTV, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV, text=Text, variable=TVTYPE1_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV, text=Text, variable=TVTYPE1_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Comp = Tabs_list[i]
tabComp = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabComp, text= "Comp")
##############################################################################################################

SAS_Var_Name='CELLPHONE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CELLPHONE_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=CELLPHONE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=CELLPHONE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DESKTOP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DESKTOP_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=DESKTOP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=DESKTOP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELPERIPH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELPERIPH_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=ELPERIPH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=ELPERIPH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMLAPTOP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMLAPTOP_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=NUMLAPTOP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=NUMLAPTOP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMSMPHONE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMSMPHONE_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=NUMSMPHONE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=NUMSMPHONE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMTABLET'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMTABLET_tk_Var = tk.IntVar()
tk.Label(tabComp, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabComp, text=Text, variable=NUMTABLET_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabComp, text=Text, variable=NUMTABLET_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabComp, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: AC = Tabs_list[i]
tabAC = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabAC, text= "AC")
##############################################################################################################

SAS_Var_Name='AGECENAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGECENAC_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=AGECENAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=AGECENAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='AIRCOND'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AIRCOND_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=AIRCOND_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=AIRCOND_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ATTCCOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ATTCCOOL_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=ATTCCOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=ATTCCOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BASECOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BASECOOL_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=BASECOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=BASECOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CENACHP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CENACHP_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=CENACHP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=CENACHP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='COOLTYPE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

COOLTYPE_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=COOLTYPE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=COOLTYPE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='GARGCOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

GARGCOOL_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=GARGCOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=GARGCOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMBERAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMBERAC_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=NUMBERAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=NUMBERAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='PROTHERM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

PROTHERM_tk_Var = tk.IntVar()
tk.Label(tabAC, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC, text=Text, variable=PROTHERM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC, text=Text, variable=PROTHERM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Freez = Tabs_list[i]
tabFreez = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabFreez, text= "Freez")
##############################################################################################################

SAS_Var_Name='AGEFRZR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGEFRZR_tk_Var = tk.IntVar()
tk.Label(tabFreez, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFreez, text=Text, variable=AGEFRZR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFreez, text=Text, variable=AGEFRZR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFreez, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMFREEZ'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMFREEZ_tk_Var = tk.IntVar()
tk.Label(tabFreez, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFreez, text=Text, variable=NUMFREEZ_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFreez, text=Text, variable=NUMFREEZ_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFreez, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SIZFREEZ'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SIZFREEZ_tk_Var = tk.IntVar()
tk.Label(tabFreez, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFreez, text=Text, variable=SIZFREEZ_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFreez, text=Text, variable=SIZFREEZ_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFreez, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UPRTFRZR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UPRTFRZR_tk_Var = tk.IntVar()
tk.Label(tabFreez, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFreez, text=Text, variable=UPRTFRZR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFreez, text=Text, variable=UPRTFRZR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFreez, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Light = Tabs_list[i]
tabLight = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabLight, text= "Light")
##############################################################################################################

SAS_Var_Name='LGTIN4'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTIN4_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTIN4_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTIN4_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTINCAN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTINCAN_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTINCAN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTINCAN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTINCFL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTINCFL_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTINCFL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTINCFL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTINCNTL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTINCNTL_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTINCNTL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTINCNTL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTINLED'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTINLED_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTINLED_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTINLED_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTINNUM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTINNUM_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTINNUM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTINNUM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTOUTCNTL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTOUTCNTL_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTOUTCNTL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTOUTCNTL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LGTOUTNUM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LGTOUTNUM_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=LGTOUTNUM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=LGTOUTNUM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TAXCREDITAPP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TAXCREDITAPP_tk_Var = tk.IntVar()
tk.Label(tabLight, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabLight, text=Text, variable=TAXCREDITAPP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabLight, text=Text, variable=TAXCREDITAPP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabLight, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Bills = Tabs_list[i]
tabBills = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabBills, text= "Bills")
##############################################################################################################

SAS_Var_Name='ATHOME'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ATHOME_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=ATHOME_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=ATHOME_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELPAY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELPAY_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=ELPAY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=ELPAY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASST'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=ENERGYASST_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=ENERGYASST_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='KOWNRENT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

KOWNRENT_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=KOWNRENT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=KOWNRENT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOACBROKE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOACBROKE_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOACBROKE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOACBROKE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOACEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOACEL_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOACEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOACEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATBROKE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATBROKE_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOHEATBROKE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOHEATBROKE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATBULK'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATBULK_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOHEATBULK_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOHEATBULK_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATEL_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOHEATEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOHEATEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATNG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATNG_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=NOHEATNG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=NOHEATNG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SCALEB'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SCALEB_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=SCALEB_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=SCALEB_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SCALEE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SCALEE_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=SCALEE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=SCALEE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SCALEG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SCALEG_tk_Var = tk.IntVar()
tk.Label(tabBills, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabBills, text=Text, variable=SCALEG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabBills, text=Text, variable=SCALEG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabBills, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: HouseAge = Tabs_list[i]
tabHouseAge = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabHouseAge, text= "HouseAge")
##############################################################################################################

SAS_Var_Name='OCCUPYYRANGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OCCUPYYRANGE_tk_Var = tk.IntVar()
tk.Label(tabHouseAge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseAge, text=Text, variable=OCCUPYYRANGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseAge, text=Text, variable=OCCUPYYRANGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseAge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='YEARMADERANGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

YEARMADERANGE_tk_Var = tk.IntVar()
tk.Label(tabHouseAge, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHouseAge, text=Text, variable=YEARMADERANGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHouseAge, text=Text, variable=YEARMADERANGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHouseAge, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: ElectrUse = Tabs_list[i]
tabElectrUse = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabElectrUse, text= "ElectrUse")
##############################################################################################################

SAS_Var_Name='ELCOOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELCOOL_tk_Var = tk.IntVar()
tk.Label(tabElectrUse, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectrUse, text=Text, variable=ELCOOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectrUse, text=Text, variable=ELCOOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectrUse, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELFOOD'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELFOOD_tk_Var = tk.IntVar()
tk.Label(tabElectrUse, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectrUse, text=Text, variable=ELFOOD_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectrUse, text=Text, variable=ELFOOD_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectrUse, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELOTHER_tk_Var = tk.IntVar()
tk.Label(tabElectrUse, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectrUse, text=Text, variable=ELOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectrUse, text=Text, variable=ELOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectrUse, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELWARM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELWARM_tk_Var = tk.IntVar()
tk.Label(tabElectrUse, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectrUse, text=Text, variable=ELWARM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectrUse, text=Text, variable=ELWARM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectrUse, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ELWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ELWATER_tk_Var = tk.IntVar()
tk.Label(tabElectrUse, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabElectrUse, text=Text, variable=ELWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabElectrUse, text=Text, variable=ELWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabElectrUse, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Winds = Tabs_list[i]
tabWinds = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabWinds, text= "Winds")
##############################################################################################################

SAS_Var_Name='TYPEGLASS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TYPEGLASS_tk_Var = tk.IntVar()
tk.Label(tabWinds, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWinds, text=Text, variable=TYPEGLASS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWinds, text=Text, variable=TYPEGLASS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWinds, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WALLTYPE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WALLTYPE_tk_Var = tk.IntVar()
tk.Label(tabWinds, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWinds, text=Text, variable=WALLTYPE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWinds, text=Text, variable=WALLTYPE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWinds, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WINDOWS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WINDOWS_tk_Var = tk.IntVar()
tk.Label(tabWinds, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWinds, text=Text, variable=WINDOWS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWinds, text=Text, variable=WINDOWS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWinds, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WINFRAME'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WINFRAME_tk_Var = tk.IntVar()
tk.Label(tabWinds, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWinds, text=Text, variable=WINFRAME_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWinds, text=Text, variable=WINFRAME_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWinds, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: SmallAppl = Tabs_list[i]
tabSmallAppl = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabSmallAppl, text= "SmallAppl")
##############################################################################################################

SAS_Var_Name='APPOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

APPOTHER_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=APPOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=APPOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BLENDER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BLENDER_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=BLENDER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=BLENDER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='COFFEE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

COFFEE_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=COFFEE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=COFFEE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CROCKPOT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CROCKPOT_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=CROCKPOT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=CROCKPOT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='RICECOOK'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

RICECOOK_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=RICECOOK_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=RICECOOK_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOAST'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOAST_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=TOAST_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=TOAST_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TOASTOVN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TOASTOVN_tk_Var = tk.IntVar()
tk.Label(tabSmallAppl, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSmallAppl, text=Text, variable=TOASTOVN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSmallAppl, text=Text, variable=TOASTOVN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSmallAppl, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Cloth = Tabs_list[i]
tabCloth = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabCloth, text= "Cloth")
##############################################################################################################

SAS_Var_Name='AGECDRYER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGECDRYER_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=AGECDRYER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=AGECDRYER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='AGECWASH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AGECWASH_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=AGECWASH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=AGECWASH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CWASHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CWASHER_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=CWASHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=CWASHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DRYER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DRYER_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=DRYER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=DRYER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DRYRFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DRYRFUEL_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=DRYRFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=DRYRFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DRYRUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DRYRUSE_tk_Var = tk.IntVar()
tk.Label(tabCloth, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCloth, text=Text, variable=DRYRUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCloth, text=Text, variable=DRYRUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCloth, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: OtherIntert = Tabs_list[i]
tabOtherIntert = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabOtherIntert, text= "OtherIntert")
##############################################################################################################

SAS_Var_Name='CABLESAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CABLESAT_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=CABLESAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=CABLESAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='COMBODVR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

COMBODVR_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=COMBODVR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=COMBODVR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='DVD'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DVD_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=DVD_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=DVD_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='PLAYSTA'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

PLAYSTA_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=PLAYSTA_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=PLAYSTA_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SEPDVR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SEPDVR_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=SEPDVR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=SEPDVR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVAUDIOSYS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVAUDIOSYS_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=TVAUDIOSYS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=TVAUDIOSYS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='VCR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

VCR_tk_Var = tk.IntVar()
tk.Label(tabOtherIntert, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabOtherIntert, text=Text, variable=VCR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabOtherIntert, text=Text, variable=VCR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabOtherIntert, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Intern = Tabs_list[i]
tabIntern = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabIntern, text= "Intern")
##############################################################################################################

SAS_Var_Name='INTERNET'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

INTERNET_tk_Var = tk.IntVar()
tk.Label(tabIntern, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabIntern, text=Text, variable=INTERNET_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabIntern, text=Text, variable=INTERNET_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabIntern, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='INTSTREAM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

INTSTREAM_tk_Var = tk.IntVar()
tk.Label(tabIntern, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabIntern, text=Text, variable=INTSTREAM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabIntern, text=Text, variable=INTSTREAM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabIntern, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='INWIRELESS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

INWIRELESS_tk_Var = tk.IntVar()
tk.Label(tabIntern, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabIntern, text=Text, variable=INWIRELESS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabIntern, text=Text, variable=INWIRELESS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabIntern, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: SpaceHeat = Tabs_list[i]
tabSpaceHeat = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabSpaceHeat, text= "SpaceHeat")
##############################################################################################################

SAS_Var_Name='ATTCHEAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ATTCHEAT_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=ATTCHEAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=ATTCHEAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='BASEHEAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BASEHEAT_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=BASEHEAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=BASEHEAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EQUIPAGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EQUIPAGE_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=EQUIPAGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=EQUIPAGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EQUIPM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EQUIPM_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=EQUIPM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=EQUIPM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EQUIPMUSE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EQUIPMUSE_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=EQUIPMUSE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=EQUIPMUSE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='GARGHEAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

GARGHEAT_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=GARGHEAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=GARGHEAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HEATHOME'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HEATHOME_tk_Var = tk.IntVar()
tk.Label(tabSpaceHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabSpaceHeat, text=Text, variable=HEATHOME_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabSpaceHeat, text=Text, variable=HEATHOME_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabSpaceHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: WaterHeat = Tabs_list[i]
tabWaterHeat = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabWaterHeat, text= "WaterHeat")
##############################################################################################################

SAS_Var_Name='H2OHEATAPT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

H2OHEATAPT_tk_Var = tk.IntVar()
tk.Label(tabWaterHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWaterHeat, text=Text, variable=H2OHEATAPT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWaterHeat, text=Text, variable=H2OHEATAPT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWaterHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='MORETHAN1H2O'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MORETHAN1H2O_tk_Var = tk.IntVar()
tk.Label(tabWaterHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWaterHeat, text=Text, variable=MORETHAN1H2O_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWaterHeat, text=Text, variable=MORETHAN1H2O_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWaterHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WHEATAGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WHEATAGE_tk_Var = tk.IntVar()
tk.Label(tabWaterHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWaterHeat, text=Text, variable=WHEATAGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWaterHeat, text=Text, variable=WHEATAGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWaterHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WHEATSIZ'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WHEATSIZ_tk_Var = tk.IntVar()
tk.Label(tabWaterHeat, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWaterHeat, text=Text, variable=WHEATSIZ_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWaterHeat, text=Text, variable=WHEATSIZ_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWaterHeat, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Fan = Tabs_list[i]
tabFan = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabFan, text= "Fan")
##############################################################################################################

SAS_Var_Name='NUMATTICFAN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMATTICFAN_tk_Var = tk.IntVar()
tk.Label(tabFan, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFan, text=Text, variable=NUMATTICFAN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFan, text=Text, variable=NUMATTICFAN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFan, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMCFAN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMCFAN_tk_Var = tk.IntVar()
tk.Label(tabFan, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFan, text=Text, variable=NUMCFAN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFan, text=Text, variable=NUMCFAN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFan, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMFLOORFAN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMFLOORFAN_tk_Var = tk.IntVar()
tk.Label(tabFan, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFan, text=Text, variable=NUMFLOORFAN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFan, text=Text, variable=NUMFLOORFAN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFan, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMWHOLEFAN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMWHOLEFAN_tk_Var = tk.IntVar()
tk.Label(tabFan, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabFan, text=Text, variable=NUMWHOLEFAN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabFan, text=Text, variable=NUMWHOLEFAN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabFan, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Tempr = Tabs_list[i]
tabTempr = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabTempr, text= "Tempr")
##############################################################################################################

SAS_Var_Name='TEMPGONE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPGONE_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPGONE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPGONE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TEMPGONEAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPGONEAC_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPGONEAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPGONEAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TEMPHOME'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPHOME_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPHOME_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPHOME_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TEMPHOMEAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPHOMEAC_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPHOMEAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPHOMEAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TEMPNITE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPNITE_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPNITE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPNITE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TEMPNITEAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TEMPNITEAC_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=TEMPNITEAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=TEMPNITEAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='THERMAIN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

THERMAIN_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=THERMAIN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=THERMAIN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='THERMAINAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

THERMAINAC_tk_Var = tk.IntVar()
tk.Label(tabTempr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTempr, text=Text, variable=THERMAINAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTempr, text=Text, variable=THERMAINAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTempr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: EnStar = Tabs_list[i]
tabEnStar = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabEnStar, text= "EnStar")
##############################################################################################################

SAS_Var_Name='ESFREEZE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESFREEZE_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESFREEZE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESFREEZE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESCWASH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESCWASH_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESCWASH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESCWASH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESDISHW'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESDISHW_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESDISHW_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESDISHW_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESDRYER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESDRYER_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESDRYER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESDRYER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESFRIG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESFRIG_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESFRIG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESFRIG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESLIGHT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESLIGHT_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESLIGHT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESLIGHT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESWATER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESWATER_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESWATER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESWATER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ESWIN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ESWIN_tk_Var = tk.IntVar()
tk.Label(tabEnStar, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnStar, text=Text, variable=ESWIN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnStar, text=Text, variable=ESWIN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnStar, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Demogr = Tabs_list[i]
tabDemogr = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabDemogr, text= "Demogr")
##############################################################################################################

SAS_Var_Name='EDUCATION'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EDUCATION_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=EDUCATION_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=EDUCATION_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EMPLOYHH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EMPLOYHH_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=EMPLOYHH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=EMPLOYHH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HHAGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HHAGE_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=HHAGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=HHAGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HHSEX'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HHSEX_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=HHSEX_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=HHSEX_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HOUSEHOLDER_RACE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HOUSEHOLDER_RACE_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=HOUSEHOLDER_RACE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=HOUSEHOLDER_RACE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='MONEYPY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MONEYPY_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=MONEYPY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=MONEYPY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMADULT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMADULT_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=NUMADULT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=NUMADULT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NUMCHILD'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NUMCHILD_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=NUMCHILD_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=NUMCHILD_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SDESCENT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SDESCENT_tk_Var = tk.IntVar()
tk.Label(tabDemogr, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDemogr, text=Text, variable=SDESCENT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDemogr, text=Text, variable=SDESCENT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDemogr, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Humid = Tabs_list[i]
tabHumid = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabHumid, text= "Humid")
##############################################################################################################

SAS_Var_Name='MOISTURE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

MOISTURE_tk_Var = tk.IntVar()
tk.Label(tabHumid, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHumid, text=Text, variable=MOISTURE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHumid, text=Text, variable=MOISTURE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHumid, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOTMOIST'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOTMOIST_tk_Var = tk.IntVar()
tk.Label(tabHumid, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHumid, text=Text, variable=NOTMOIST_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHumid, text=Text, variable=NOTMOIST_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHumid, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USEMOISTURE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USEMOISTURE_tk_Var = tk.IntVar()
tk.Label(tabHumid, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHumid, text=Text, variable=USEMOISTURE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHumid, text=Text, variable=USEMOISTURE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHumid, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USENOTMOIST'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USENOTMOIST_tk_Var = tk.IntVar()
tk.Label(tabHumid, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHumid, text=Text, variable=USENOTMOIST_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHumid, text=Text, variable=USENOTMOIST_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHumid, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Audit = Tabs_list[i]
tabAudit = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabAudit, text= "Audit")
##############################################################################################################

SAS_Var_Name='AUDIT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AUDIT_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=AUDIT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=AUDIT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='AUDITCHG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

AUDITCHG_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=AUDITCHG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=AUDITCHG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='REBATEAPP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

REBATEAPP_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=REBATEAPP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=REBATEAPP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='RECYCAPP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

RECYCAPP_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=RECYCAPP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=RECYCAPP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SMARTMETER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SMARTMETER_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=SMARTMETER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=SMARTMETER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SMARTTHERM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SMARTTHERM_tk_Var = tk.IntVar()
tk.Label(tabAudit, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAudit, text=Text, variable=SMARTTHERM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAudit, text=Text, variable=SMARTTHERM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAudit, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: WhoPays = Tabs_list[i]
tabWhoPays = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabWhoPays, text= "WhoPays")
##############################################################################################################

SAS_Var_Name='FOPAY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FOPAY_tk_Var = tk.IntVar()
tk.Label(tabWhoPays, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWhoPays, text=Text, variable=FOPAY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWhoPays, text=Text, variable=FOPAY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWhoPays, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LPGPAY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LPGPAY_tk_Var = tk.IntVar()
tk.Label(tabWhoPays, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWhoPays, text=Text, variable=LPGPAY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWhoPays, text=Text, variable=LPGPAY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWhoPays, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NGPAY'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NGPAY_tk_Var = tk.IntVar()
tk.Label(tabWhoPays, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWhoPays, text=Text, variable=NGPAY_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWhoPays, text=Text, variable=NGPAY_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWhoPays, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: HeatFuel = Tabs_list[i]
tabHeatFuel = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabHeatFuel, text= "HeatFuel")
##############################################################################################################

SAS_Var_Name='FUELH2O'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FUELH2O_tk_Var = tk.IntVar()
tk.Label(tabHeatFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHeatFuel, text=Text, variable=FUELH2O_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHeatFuel, text=Text, variable=FUELH2O_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHeatFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='FUELH2O2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FUELH2O2_tk_Var = tk.IntVar()
tk.Label(tabHeatFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabHeatFuel, text=Text, variable=FUELH2O2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabHeatFuel, text=Text, variable=FUELH2O2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabHeatFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: CookFuel = Tabs_list[i]
tabCookFuel = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabCookFuel, text= "CookFuel")
##############################################################################################################

SAS_Var_Name='DUALCOOKTFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DUALCOOKTFUEL_tk_Var = tk.IntVar()
tk.Label(tabCookFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCookFuel, text=Text, variable=DUALCOOKTFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCookFuel, text=Text, variable=DUALCOOKTFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCookFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OUTGRILLFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OUTGRILLFUEL_tk_Var = tk.IntVar()
tk.Label(tabCookFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCookFuel, text=Text, variable=OUTGRILLFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCookFuel, text=Text, variable=OUTGRILLFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCookFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OVENFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OVENFUEL_tk_Var = tk.IntVar()
tk.Label(tabCookFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCookFuel, text=Text, variable=OVENFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCookFuel, text=Text, variable=OVENFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCookFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='STOVEFUEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

STOVEFUEL_tk_Var = tk.IntVar()
tk.Label(tabCookFuel, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabCookFuel, text=Text, variable=STOVEFUEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabCookFuel, text=Text, variable=STOVEFUEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabCookFuel, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: RecSubs = Tabs_list[i]
tabRecSubs = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabRecSubs, text= "RecSubs")
##############################################################################################################

SAS_Var_Name='BENOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

BENOTHER_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=BENOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=BENOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EELIGHTS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EELIGHTS_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=EELIGHTS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=EELIGHTS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='FREEAUDIT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FREEAUDIT_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=FREEAUDIT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=FREEAUDIT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOACHELP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOACHELP_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=NOACHELP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=NOACHELP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATHELP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATHELP_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=NOHEATHELP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=NOHEATHELP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='PAYHELP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

PAYHELP_tk_Var = tk.IntVar()
tk.Label(tabRecSubs, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabRecSubs, text=Text, variable=PAYHELP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabRecSubs, text=Text, variable=PAYHELP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabRecSubs, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: AC2 = Tabs_list[i]
tabAC2 = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabAC2, text= "AC2")
##############################################################################################################

SAS_Var_Name='PROTHERMAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

PROTHERMAC_tk_Var = tk.IntVar()
tk.Label(tabAC2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC2, text=Text, variable=PROTHERMAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC2, text=Text, variable=PROTHERMAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SWAMPCOL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SWAMPCOL_tk_Var = tk.IntVar()
tk.Label(tabAC2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC2, text=Text, variable=SWAMPCOL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC2, text=Text, variable=SWAMPCOL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USECENAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USECENAC_tk_Var = tk.IntVar()
tk.Label(tabAC2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabAC2, text=Text, variable=USECENAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabAC2, text=Text, variable=USECENAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabAC2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: EnerAss = Tabs_list[i]
tabEnerAss = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabEnerAss, text= "EnerAss")
##############################################################################################################

SAS_Var_Name='ENERGYASST11'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST11_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASST11_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASST11_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASST12'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST12_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASST12_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASST12_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASST13'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST13_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASST13_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASST13_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASST14'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST14_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASST14_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASST14_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASST15'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASST15_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASST15_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASST15_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='ENERGYASSTOTH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

ENERGYASSTOTH_tk_Var = tk.IntVar()
tk.Label(tabEnerAss, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnerAss, text=Text, variable=ENERGYASSTOTH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnerAss, text=Text, variable=ENERGYASSTOTH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnerAss, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: DD = Tabs_list[i]
tabDD = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabDD, text= "DD")
##############################################################################################################

SAS_Var_Name='WSF'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WSF_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=WSF_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=WSF_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='GWT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

GWT_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=GWT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=GWT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CDD30YR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CDD30YR_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=CDD30YR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=CDD30YR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CDD65'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CDD65_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=CDD65_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=CDD65_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='CDD80'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

CDD80_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=CDD80_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=CDD80_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='GNDHDD65'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

GNDHDD65_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=GNDHDD65_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=GNDHDD65_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HDD30YR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HDD30YR_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=HDD30YR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=HDD30YR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HDD50'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HDD50_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=HDD50_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=HDD50_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HDD65'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HDD65_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=HDD65_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=HDD65_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='IECC_CLIMATE_PUB'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

IECC_CLIMATE_PUB_tk_Var = tk.IntVar()
tk.Label(tabDD, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabDD, text=Text, variable=IECC_CLIMATE_PUB_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabDD, text=Text, variable=IECC_CLIMATE_PUB_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabDD, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: other = Tabs_list[i]
tabother = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabother, text= "other")
##############################################################################################################

SAS_Var_Name='DNTHEAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

DNTHEAT_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=DNTHEAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=DNTHEAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EQUIPAUX'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EQUIPAUX_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=EQUIPAUX_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=EQUIPAUX_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='EQUIPAUXTYPE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

EQUIPAUXTYPE_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=EQUIPAUXTYPE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=EQUIPAUXTYPE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NHSLDMEM'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NHSLDMEM_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=NHSLDMEM_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=NHSLDMEM_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='OA_LAT'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

OA_LAT_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=OA_LAT_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=OA_LAT_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='SIZRFRI2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

SIZRFRI2_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=SIZRFRI2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=SIZRFRI2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WWACAGE'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WWACAGE_tk_Var = tk.IntVar()
tk.Label(tabother, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabother, text=Text, variable=WWACAGE_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabother, text=Text, variable=WWACAGE_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabother, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: TV2 = Tabs_list[i]
tabTV2 = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabTV2, text= "TV2")
##############################################################################################################

SAS_Var_Name='TVONWE2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVONWE2_tk_Var = tk.IntVar()
tk.Label(tabTV2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV2, text=Text, variable=TVONWE2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV2, text=Text, variable=TVONWE2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVONWD2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVONWD2_tk_Var = tk.IntVar()
tk.Label(tabTV2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV2, text=Text, variable=TVONWD2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV2, text=Text, variable=TVONWD2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVSIZE2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVSIZE2_tk_Var = tk.IntVar()
tk.Label(tabTV2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV2, text=Text, variable=TVSIZE2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV2, text=Text, variable=TVSIZE2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TVTYPE2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TVTYPE2_tk_Var = tk.IntVar()
tk.Label(tabTV2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV2, text=Text, variable=TVTYPE2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV2, text=Text, variable=TVTYPE2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='TYPERFR2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

TYPERFR2_tk_Var = tk.IntVar()
tk.Label(tabTV2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabTV2, text=Text, variable=TYPERFR2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabTV2, text=Text, variable=TYPERFR2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabTV2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Wood = Tabs_list[i]
tabWood = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabWood, text= "Wood")
##############################################################################################################

SAS_Var_Name='USEWOOD'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USEWOOD_tk_Var = tk.IntVar()
tk.Label(tabWood, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWood, text=Text, variable=USEWOOD_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWood, text=Text, variable=USEWOOD_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWood, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WDOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WDOTHER_tk_Var = tk.IntVar()
tk.Label(tabWood, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWood, text=Text, variable=WDOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWood, text=Text, variable=WDOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWood, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WDPELLET'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WDPELLET_tk_Var = tk.IntVar()
tk.Label(tabWood, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWood, text=Text, variable=WDPELLET_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWood, text=Text, variable=WDPELLET_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWood, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='WOODLOGS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

WOODLOGS_tk_Var = tk.IntVar()
tk.Label(tabWood, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabWood, text=Text, variable=WOODLOGS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabWood, text=Text, variable=WOODLOGS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabWood, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Unab = Tabs_list[i]
tabUnab = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabUnab, text= "Unab")
##############################################################################################################

SAS_Var_Name='COLDMA'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

COLDMA_tk_Var = tk.IntVar()
tk.Label(tabUnab, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabUnab, text=Text, variable=COLDMA_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabUnab, text=Text, variable=COLDMA_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabUnab, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='HOTMA'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

HOTMA_tk_Var = tk.IntVar()
tk.Label(tabUnab, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabUnab, text=Text, variable=HOTMA_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabUnab, text=Text, variable=HOTMA_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabUnab, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOACDAYS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOACDAYS_tk_Var = tk.IntVar()
tk.Label(tabUnab, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabUnab, text=Text, variable=NOACDAYS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabUnab, text=Text, variable=NOACDAYS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabUnab, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='NOHEATDAYS'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

NOHEATDAYS_tk_Var = tk.IntVar()
tk.Label(tabUnab, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabUnab, text=Text, variable=NOHEATDAYS_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabUnab, text=Text, variable=NOHEATDAYS_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabUnab, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: Kitch = Tabs_list[i]
tabKitch = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabKitch, text= "Kitch")
##############################################################################################################

SAS_Var_Name='FOODPROC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FOODPROC_tk_Var = tk.IntVar()
tk.Label(tabKitch, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabKitch, text=Text, variable=FOODPROC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabKitch, text=Text, variable=FOODPROC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabKitch, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LOCRFRI2'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LOCRFRI2_tk_Var = tk.IntVar()
tk.Label(tabKitch, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabKitch, text=Text, variable=LOCRFRI2_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabKitch, text=Text, variable=LOCRFRI2_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabKitch, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='STOVEN'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

STOVEN_tk_Var = tk.IntVar()
tk.Label(tabKitch, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabKitch, text=Text, variable=STOVEN_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabKitch, text=Text, variable=STOVEN_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabKitch, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 4) iterate over Tabs_list: EnS2 = Tabs_list[i]
tabEnS2 = tk.Frame(Tab_control, bg=Color0) 
Tab_control.add(tabEnS2, text= "EnS2")
##############################################################################################################

SAS_Var_Name='FOOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FOOTHER_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=FOOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=FOOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='FUELAUX'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

FUELAUX_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=FUELAUX_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=FUELAUX_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='LPOTHER'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

LPOTHER_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=LPOTHER_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=LPOTHER_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='UGOTH'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

UGOTH_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=UGOTH_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=UGOTH_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USEEL'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USEEL_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USEEL_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USEEL_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USEFO'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USEFO_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USEFO_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USEFO_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USELP'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USELP_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USELP_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USELP_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USENG'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USENG_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USENG_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USENG_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USESOLAR'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USESOLAR_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USESOLAR_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USESOLAR_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################

##############################################################################################################

SAS_Var_Name='USEWWAC'
Coded_Responses =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Coded Responses'].values
Coded_ResponsesList = np.array2string(Coded_Responses)[2:-2].split('\\n')
Coded_Responses_Texts =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Final Response Set'].values
C_Resp_Txt_List=np.array2string(Coded_Responses_Texts)[2:-2].split('\\n')
Descr =pdVarDescr[pdVarDescr['SAS Variable Name']==SAS_Var_Name]['Variable Description'].values[0]

USEWWAC_tk_Var = tk.IntVar()
tk.Label(tabEnS2, text = Descr, font=('Helvetica', 10, 'bold'), bg = Color0).grid(column=0, row=row_counter, sticky="E")
for ind in range(len(Coded_ResponsesList)):
    Code=Coded_ResponsesList[ind]
    Text=C_Resp_Txt_List[ind]
    if (str_entry_indicator in Code): #check if Entry needed
        widg, row_counter=add_entry(tabEnS2, text=Text, variable=USEWWAC_tk_Var, value=Code, row_counter = row_counter)
    else:
        widg, row_counter=add_radiobut(tabEnS2, text=Text, variable=USEWWAC_tk_Var, value=Code, row_counter = row_counter)
row_counter+=1
ttk.Separator(tabEnS2, orient=HORIZONTAL).grid(column=0, row=row_counter, sticky='EW', columnspan = 2)
row_counter+=1

####################################################################################################################
# 6) end of script, just ones
Tab_control.pack(expan = 1, fill = 'both')

buttonSave=tk.Button(windowEdit, text='Save',  command=buttonSave_clicked, bg = Color4, fg = 'white' ).pack()

windowEdit.mainloop()