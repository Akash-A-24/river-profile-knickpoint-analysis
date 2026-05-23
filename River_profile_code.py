import geopandas as gpd
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from scipy.ndimage import gaussian_filter1d

# INPUT FILES
river_file = r"C:\Users\91827\Downloads\Charles_uni\River_profile_data\Alaknanada_river_Edit.shp"
dem_file = r"C:\Users\91827\Downloads\Charles_uni\River_profile_data\DEM_data.tif"

# Sampling interval in meters
interval = 200

# LOAD DATA
river = gpd.read_file(river_file)
dem = rasterio.open(dem_file)

print(f"Number of features found: {len(river)}")

if len(river) == 0:
    print("Shapefile is empty")
    exit()
else:
    river = river.to_crs(dem.crs)
    line = river.geometry.iloc[0]
    print("Success: River geometry loaded.")

# SAMPLE POINTS ALONG RIVER
length = line.length
distances = np.arange(0, length, interval)
points = [line.interpolate(d) for d in distances]

# EXTRACT DEM ELEVATION
elevations = []

for pt in points:
    x, y = pt.x, pt.y
    row, col = dem.index(x, y)
    elev = dem.read(1)[row, col]
    elevations.append(elev)

elevations = np.array(elevations)

# Convert distance to km
dist_km = distances / 1000

# SMOOTH PROFILE
smooth_elev = gaussian_filter1d(elevations, sigma=2)

# CALCULATE GRADIENT
gradient = np.gradient(smooth_elev, interval)

# DETECT KNICKPOINTS
threshold = np.std(gradient) * 2
knickpoints = np.where(np.abs(gradient) > threshold)[0]

# PLOT PROFILE
plt.figure(figsize=(10,5))

# Raw profile
plt.plot(dist_km, elevations, linewidth=1, alpha=0.4, label="Raw elevation")

# Smoothed profile
plt.plot(dist_km, smooth_elev, linewidth=2, label="Smoothed profile")

# Mark knickpoints
plt.scatter(
    dist_km[knickpoints],
    smooth_elev[knickpoints],
    marker="o",
    label="Potential knickpoints"
)

plt.xlabel("Distance downstream (km)", fontsize=12.5)
plt.ylabel("Elevation (m)", fontsize=12.5)
plt.title("Longitudinal Profile of the Alaknanda River", fontsize=12.5)

plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)

plt.grid(True)

plt.legend(fontsize=12.5)

plt.tight_layout()

plt.show()