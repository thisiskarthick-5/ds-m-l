from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='l')

m.drawcoastlines()
m.drawcountries()

# Example: plot points for cities
lat = [28.61, 51.51, 40.71]   # Delhi, London, New York
lon = [77.23, -0.13, -74.01]
city_names = ['Delhi', 'London', 'New York']

x, y = m(lon, lat)
m.scatter(x, y, marker='o', color='red', zorder=5)
for i, city in enumerate(city_names):
    plt.text(x[i]+200000, y[i]+200000, city, fontsize=10)

plt.title("Major Cities on Map")
plt.show()
