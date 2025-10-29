from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Create a map
plt.figure(figsize=(10, 8))

m = Basemap(projection='mill',  # 'mill' is the projection type
            llcrnrlat=-60, urcrnrlat=90,   # latitude range
            llcrnrlon=-180, urcrnrlon=180, # longitude range
            resolution='c')  # 'c' = crude, 'l' = low, 'h' = high

# Draw map features
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawparallels(range(-90,91,30), labels=[1,0,0,0])  # latitude lines
m.drawmeridians(range(-180,181,60), labels=[0,0,0,1]) # longitude lines

plt.title("World Map using Basemap")
plt.show()
