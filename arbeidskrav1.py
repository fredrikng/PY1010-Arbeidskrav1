# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:22:22 2024

@author: Fredrik
"""

# Elbil
# Årlige utgifter
# Årlig kjørelengde 8000 km

el_aarlig_forsikring = 5000
el_aarlig_avgift = 8.38 * 365
el_aarlig_drivstoff = 0.2 * 8000 * 2
el_aarlig_bom = 0.1 * 8000
el_total_kostnad = el_aarlig_forsikring + el_aarlig_avgift + el_aarlig_drivstoff + el_aarlig_bom

print("Kostnader for elbil")
print("Årlig forsikringsavgift er: ", el_aarlig_forsikring)
print("Årlig trafikkavgift er: ", el_aarlig_avgift)
print("Årlig drivstoffavgift er: ", el_aarlig_drivstoff)
print("Årlig bomavgift er: ", el_aarlig_bom)
print("Årlig total kostnad er: ", el_total_kostnad)


# Bensinbil
# Årlige utgifter
# Årlig kjørelengde 8000 km

ben_aarlig_forsikring = 7500
ben_aarlig_avgift = 8.38 * 365
ben_aarlig_drivstoff = 1 * 8000
ben_aarlig_bom = 0.3 * 8000
ben_total_kostnad = ben_aarlig_forsikring + ben_aarlig_avgift + ben_aarlig_drivstoff + ben_aarlig_bom

print("Kostnader for bensin bil")
print("Årlig forsikringsavgift er: ", ben_aarlig_forsikring)
print("Årlig trafikkavgift er: ", ben_aarlig_avgift)
print("Årlig drivstoffavgift er: ", ben_aarlig_drivstoff)
print("Årlig bomavgift er: ", ben_aarlig_bom)
print("Årlig total kostnad er: ", ben_total_kostnad)

# Konklusjon
print("Du sparer", (int(ben_total_kostnad - el_total_kostnad)), "i året med å kjøre elbil")