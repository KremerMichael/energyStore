#!/usr/bin/env python3

#This file holds our generic definitions for the various batteries

#LG Chem RESU10H
#Values were obtained from these resources
#https://advancesolar.com/wp-content/uploads/2018/05/LG-Chem-RESU10H-Datasheet-DS.pdf
#https://news.energysage.com/lg-chem-resu-battery-review/
LG_CHEM_RESU10H = {
    #For measures of energy storage
    "TOTAL_ENERGY":  9.8, #kWh
    "USABLE_ENERGY": 9.3, #kWh
    
    "MAX_CONTINUOUS": 5, #kW
    
    #Round trip efficiency is 94.5% so say
    "STORAGE_EFFIECIENCY":  .972,
    "DEPLETION_EFFICIENCY": .972,
    #Because .972 * .972 = .945 or 94.5% round trip
}
    
#tesla powerwall 2
#Values were obtained from this data sheet:
#https://www.tesla.com/sites/default/files/pdfs/powerwall/Powerwall%202_AC_Datasheet_en_northamerica.pdf
tesla_powerwall_2 = {
    #For measures of enery storage
    "TOTAL_ENERGY":  14,   #kWh
    "USABLE_ENERGY": 13.5, #kWh

    #For max continuous power
    "MAX_CONTINUOUS": 5.8, #kW, charge and discharge

    #For charge/discharge efficiency
    #Round Trip efficieny is 90% so say
    "STORAGE_EFFICIENCY":   0.949,
    "DEPLETION_EFFICIENCY": 0.949,
    #Because .949 * .949 = .90 or 90% round trip
}

#Should probably figure out something with relation to temperature????
