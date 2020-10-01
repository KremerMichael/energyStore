#!/usr/bin/env python3
#This file holds our generic definitions for the tesla powerwall 2
#Values were obtained from this data sheet:
#https://www.tesla.com/sites/default/files/pdfs/powerwall/Powerwall%202_AC_Datasheet_en_northamerica.pdf

#For measures of enery storage
TOTAL_ENERGY = 14 #this is kWh
USABLE_ENERGY = 13.5 #this is kWh

#For max continuous power
MAX_CONTINUOUS = 5.8 #this is kVA, charge and discharge

#For charge/discharge efficiency
#Round Trip efficieny is 90% so say
STORAGE_EFFICIENCY = 0.949
DEPLETION_EFFICIENCY = 0.949
#Because .949 * .949 = .90 or 90% round trip

#Should probably figure out something with relation to temperature????
