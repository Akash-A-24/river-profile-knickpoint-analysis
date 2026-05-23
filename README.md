# River Profile & Knickpoint Analysis using DEM and Geospatial Python

## Overview

This repository contains a Python-based geospatial workflow for extracting longitudinal river profiles from Digital Elevation Models (DEMs) and identifying potential knickpoints using gradient-based geomorphometric analysis.

The workflow integrates vector river networks and raster elevation datasets to generate smoothed elevation profiles, compute longitudinal gradients, and automatically identify geomorphic discontinuities along river channels.

This project is designed for applications in:

- Fluvial geomorphology
- River morphodynamics
- Terrain analysis
- Hydro-geomorphic studies
- Watershed analysis
- Longitudinal river profile extraction

---

## Features

- Extract river elevation profiles from DEM data
- Sample elevation points along river centerlines
- Smooth longitudinal profiles using Gaussian filtering
- Calculate downstream channel gradients
- Detect potential knickpoints automatically
- Visualize raw and smoothed river profiles
- Fully Python-based and reproducible workflow

---

## Technologies Used

- Python
- GeoPandas
- Rasterio
- NumPy
- SciPy
- Matplotlib
- Shapely

---

## Workflow

1. Load river centerline shapefile
2. Load DEM raster
3. Reproject vector data to DEM coordinate system
4. Sample elevation values along the river at fixed intervals
5. Smooth elevation profile using Gaussian filtering
6. Compute longitudinal gradient
7. Detect potential knickpoints using gradient thresholds
8. Visualize river longitudinal profile and detected knickpoints

---

## Input Data

### Required Inputs

#### 1. River Shapefile
- Polyline river centerline
- Format: `.shp`

#### 2. DEM Raster
- Digital Elevation Model
- Format: `.tif`

---

## Example Output

The script generates:

- Raw longitudinal elevation profile
- Smoothed elevation profile
- Automatically detected potential knickpoints
- River distance vs elevation visualization

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/river-profile-knickpoint-analysis.git
cd river-profile-knickpoint-analysis
```

Install required packages:

```bash
pip install geopandas rasterio numpy matplotlib scipy shapely
```

---

## Usage

Update the file paths inside the script:

```python
river_file = r"path_to_river_shapefile.shp"
dem_file = r"path_to_dem.tif"
```

Run the script:

```bash
python river_profile_analysis.py
```

---

## Methodology

### River Sampling
The river centerline is sampled at fixed downstream intervals to extract elevation values from the DEM.

### Profile Smoothing
Gaussian filtering is applied to reduce noise and improve geomorphic interpretation.

### Gradient Analysis
Longitudinal slope gradients are calculated using:

```math
Gradient = \frac{dZ}{dX}
```

### Knickpoint Detection
Potential knickpoints are identified where local gradient magnitude exceeds a statistical threshold.

---

## Applications

- River incision analysis
- Tectonic geomorphology
- Channel evolution studies
- Floodplain assessment
- Sediment transport investigations
- Mountain river profile analysis

---

## Future Improvements

- Interactive GIS visualization
- Multi-river batch processing
- Chi-profile analysis
- Stream power calculations
- Automated watershed extraction
- Machine learning-based knickpoint classification

---

## Repository Structure

```bash
river-profile-knickpoint-analysis/
│
├── data/
│   ├── river_shapefile/
│   └── dem/
│
├── outputs/
│   ├── figures/
│   └── profiles/
│
├── river_profile_analysis.py
├── requirements.txt
└── README.md
```

---

## Author

Akash A  
M.Tech Remote Sensing Student  
Indian Institute of Technology Roorkee

---

## License

This project is released under the MIT License.

---

## Citation

If you use this workflow in research or academic work, please cite this repository appropriately.

```bibtex
@software{river_profile_knickpoint_analysis,
  author = {Akash A},
  title = {River Profile and Knickpoint Analysis using DEM and Geospatial Python},
  year = {2026},
  url = {https://github.com/yourusername/river-profile-knickpoint-analysis}
}
```
