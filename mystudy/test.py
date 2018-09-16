import matplotlib.pyplot as plt
import cartopy.crs as crs
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image

lat = 116
lon = 39
img = Image.open('Flag_of_China.png')

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=crs.PlateCarree())
ax.coastlines()
ax.stock_img()
imagebox = OffsetImage(img, zoom=0.01)
imagebox.image.axes = ax
ab = AnnotationBbox(imagebox, [lat, lon], pad=0, frameon=False)
ax.add_artist(ab)

plt.show()