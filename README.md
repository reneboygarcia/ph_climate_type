# Climate Type Mapping in the Philippines

This project aims to visualize the climate types across different regions in the Philippines. It leverages geospatial data and climate classification to create an interactive map that highlights the varying climate conditions across the country.

## Data Sources

* Shapefile for Philippine Administrative Divisions (Level 2): PH_Adm2_ProvDists/PH_Adm2_ProvDists.shp.shp
* Climate Type Classification per Region: climate_type_region.csv

## Technologies Used

* Folium for interactive map visualization
* Geopandas for geospatial data handling
* Pandas for data manipulation and analysis
* Geopy for geocoding (not used in this project but available for future extensions)

## Map Features

* Interactive map centered on the Philippines
* Climate type classification per region (Type I to IV)
* Color-coded regions based on climate type
* MiniMap for easy navigation
* MeasureControl for distance and area measurements
* Tooltip with region name and climate type information
* Legend for climate type color reference

## How to Use

1. Ensure all required libraries are installed (folium, geopandas, pandas, geopy).
2. Run the script ph_climate_type.py to generate the interactive map.
3. Open the generated map in a web browser to explore climate types across the Philippines.

## Future Extensions

* Integrate additional climate-related data (e.g., temperature, rainfall) for more detailed analysis.
* Incorporate other geospatial data (e.g., elevation, land use) to enhance the map's context.
* Develop a user interface for selecting specific climate types or regions to focus on.

This project aims to provide a visual representation of climate types in the Philippines, facilitating better understanding and decision-making for climate-related initiatives.
