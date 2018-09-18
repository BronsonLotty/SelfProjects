import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(16,8))
m = Basemap()
m.drawcoastlines()
plt.show()





from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', lat_0=0, lon_0=0)

# 填充蓝色的全球
map.drawmapboundary(fill_color='aqua')
# 填充陆地颜色
map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()
plt.show()