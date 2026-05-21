# Florida Scenic Highway Corridor Analysis

A Power BI dashboard analyzing Florida's 27 designated scenic highways by traffic volume and points of interest.

## Live dashboard
https://app.powerbi.com/groups/me/reports/be6ae089-d04c-4eba-8685-4f91af2ba457/1e29b6435f9494256d6e?experience=power-bi
## Overview
Helps FDOT planners and Florida residents identify scenic highway corridors balancing traffic volume with experiential quality. The Chill Rating categorizes routes by daily traffic density to support trip planning and corridor preservation.

## Tech stack
- Power BI Desktop
- Azure Maps visual
- DAX measures for dynamic filtering
- Custom bookmarks for state management

## Data sources
- FDOT Roadway Characteristics Inventory (AADT, 2024) from https://ftp.fdot.gov/file/d/FTP/FDOT/co/planning/transtat/gis/shapefiles/
- FDOT Scenic Highways Program from https://ftp.fdot.gov/file/d/FTP/FDOT/co/planning/transtat/gis/shapefiles/
- Hand-curated POI dataset (27 stops, created manually)

## Data pipeline

FDOT distributes scenic highway and AADT data as ESRI shapefiles, which include `.dbf` (dBASE) attribute tables that Power BI  cannot natively read.

To get this data into Power BI, I wrote a small Python utility  (`convert_dbf.py`) using the `dbfread` library to convert the DBF attribute tables to CSV. Power BI then ingests the CSVs via Power Query, where they're cleaned, joined, and shaped into the final model.

### Pipeline:
1. Download shapefile bundle from FDOT GIS portal
2. Extract `.dbf` files
3. Run `convert_dbf.py` → produces `.csv`
4. Import CSVs into Power BI via Power Query
5. Clean, join, and shape into final 3-table model

## Key features
- Interactive county and chill rating filters
- Cross-filtered POI recommendations per highway
- Direct Google Maps navigation per stop
- Colorblind-safe visual encoding

## Design decisions
- Consolidated 10 source tables → 3 for performance
- Azure Maps over ArcGIS (faster load times)
- Blue-to-orange palette for accessibility
- Emoji icons as secondary visual channel

## How to run locally
1. Download the .pbix file
2. Open in Power BI Desktop (free)
3. Data refreshes from local cache

## Author
Sara Khan | https://linkedin.com/in/sarakha
Tallahassee, FL
