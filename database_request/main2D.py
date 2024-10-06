# main.py
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
import matplotlib.pyplot as plt
 
# Exoplanet data request to CSV from NASA Exoplanets Archive Web
exoplanets = pd.read_csv('exoplanets.csv', skiprows=291, dtype={'ra': float, 'dec': float, 'pl_orbsmax': float}, low_memory=False)

# Filter the request to show relevant data
exoplanets = exoplanets.dropna(subset=['pl_name', 'hostname', 'sy_snum', 'sy_pnum', 'sy_mnum', 'disc_year', 'pl_rade', 'pl_masse', 'pl_dens', 'gaia_id', 'pl_eqt'])

#Convert to numeric type, if necessary
exoplanets['ra'] = pd.to_numeric(exoplanets['ra'], errors='coerce')
exoplanets['dec'] = pd.to_numeric(exoplanets['dec'], errors='coerce')
exoplanets['pl_orbsmax'] = pd.to_numeric(exoplanets['pl_orbsmax'], errors='coerce')

# Remove rows that still have null values after conversion
exoplanets = exoplanets.dropna(subset=['ra', 'dec', 'pl_orbsmax'])

# Filter the data to ensure the ranges are valid
exoplanets = exoplanets[(exoplanets['ra'] >= 0) & (exoplanets['ra'] <= 360) & 
                         (exoplanets['dec'] >= -90) & (exoplanets['dec'] <= 90)]

# Exoplanets name selected to show data at the Beta Version
exoplanets_names = ['BD-14 3065 b', 'K2-419 A b', '55 Cnc e', 'NGTS-26 b', 'CoRoT-16 b', 'BD+20 594 b', 
                    'HD 80606 b', 'AU Mic b', 'GJ 1132 b', 'Kepler-102 b', 'HD 209458 b', 'OGLE-TR-56 b', 
                    'CoRoT-1 b', 'TOI-1408 b', 'TOI-3540 A b', 'HD 191939 c', 'TRAPPIST-1 b', 
                    'CoRoT-14 b', 'CoRoT-3 b', 'GPX-1 b', 'KELT-1 b', 'KOI-2513.01', 'TOI-1994 b', 
                    'CoRoT-20 b', 'K2-233 c', 'Gliese 12', 'HD 95338 b', 'K2-18 b', 'Kepler-1654 b', 
                    'Kepler-1661 b', 'LHS 1140 b', 'CoRoT-11 b', 'HAT-P-23 b', 'HD 80653 b', 
                    'KELT-16 b', 'KELT-9 b', 'WASP-189 b', 'WASP-33 b']

# Filter the DataFrame based on the array of exoplanet names
filtered_exoplanets = exoplanets[exoplanets['pl_name'].isin(exoplanets_names)]

# Display the relevant data for the filtered exoplanets
print(filtered_exoplanets)


######## FIRST REPRESENTATION IN 2D #########
# Create a coordinates object for all exoplanets
#exoplanet_coords = SkyCoord(
#    ra=exoplanets['ra'].values * u.deg,
#    dec=exoplanets['dec'].values * u.deg,
#   distance=exoplanets['pl_orbsmax'].values * u.AU
#)

# Convert the coordinates to a 2D reference system
#x = exoplanet_coords.cartesian.x.value
#y = exoplanet_coords.cartesian.y.value

# Print Grafic
#plt.figure(figsize=(10, 8))
#plt.scatter(x, y, s=10, alpha=0.5)
#plt.title('Distribución de Exoplanetas')
#plt.xlabel('Coordenadas X (pc)')
#plt.ylabel('Coordenadas Y (pc)')
#plt.grid(True)
#plt.axis('equal')
#plt.show()