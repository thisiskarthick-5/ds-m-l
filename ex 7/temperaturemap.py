import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Create data grid
lon = np.linspace(-180, 180, 360)
lat = np.linspace(-90, 90, 180)
lon2d, lat2d = np.meshgrid(lon, lat)

# Example data (like temperature)
data = np.sin(np.radians(lat2d)) * np.cos(np.radians(lon2d))

plt.figure(figsize=(12,6))
m = Basemap(projection='cyl', resolution='l')
m.drawcoastlines()

# Plot contour
cs = m.contourf(lon2d, lat2d, data, cmap='coolwarm')
plt.colorbar(cs, orientation='vertical', label='Value')
plt.title("Contour Map Example (Simulated Data)")
plt.show()
