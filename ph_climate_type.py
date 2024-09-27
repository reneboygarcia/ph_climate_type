import folium
from folium.plugins import MiniMap, MeasureControl
from geopy.geocoders import Nominatim
import pandas as pd
import geopandas as gpd

shapefile_path = "PH_Adm2_ProvDists/PH_Adm2_ProvDists.shp.shp"
ph_shapefile = gpd.read_file(shapefile_path)

# 2. Select only ADM2_EN and geometry columns
ph_shapefile = ph_shapefile[["adm2_en", "geo_level", "geometry"]]

# 3. Create a DataFrame for climate type per region
# Read the CSV file
climate_type_df = pd.read_csv("climate_type_region.csv")
climate_type_df = climate_type_df[["region_name", "climate_type"]]
# Drop the whole row if there are missing values in any column
climate_type_df = climate_type_df.dropna(how="all")

# 4. Merge the shapefile GeoDataFrame with the climate type per pregion
# Assuming the 'region_name' column in rainfall_df matches a column in the shapefile (like 'NAME_1' or 'region')
merged_data = ph_shapefile.merge(
    climate_type_df, left_on="adm2_en", right_on="region_name", how="left"
)

# 5. Define the color mapping for climate types
climate_type_colors = {
    "Type I": "#A6D0E4",  # Pastel blue
    "Type II": "#B8E6B8",  # Pastel green
    "Type III": "#FFB3BA",  # Pastel red
    "Type IV": "#FFFFD1",  # Pastel yellow
}

# 6. Create a column in the GeoDataFrame to hold the color based on climate type
merged_data["color"] = merged_data["climate_type"].map(climate_type_colors)

# 7. Create the base map centered on the Philippines
map_center = [12.8797, 121.7740]  # Center of the Philippines
climate_map = folium.Map(location=map_center, zoom_start=5.5, tiles="cartodbpositron")

# add MiniMap and MeasureControl (combined for slight efficiency gain)
climate_map.add_child(MiniMap())
climate_map.add_child(MeasureControl())


# Function to style the GeoJson features (no changes needed)
def style_function(feature):
    climate_type = feature["properties"]["climate_type"]
    return {
        "fillColor": climate_type_colors.get(climate_type, "gray"),
        "color": "black",
        "weight": 1.5,
        "fillOpacity": 0.7,
    }

# Convert merged_data to GeoJSON once (already efficient)
geojson_data = merged_data.to_crs(epsg=4326).__geo_interface__

# Create the GeoJson layer once and reuse it
geojson_layer = folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=["region_name", "climate_type"]),
)

# Add GeoJson to the map
geojson_layer.add_to(climate_map)

# Fit map bounds using the pre-created layer
climate_map.fit_bounds(geojson_layer.get_bounds())

# Add a legend (no changes needed, already efficient)
legend_html = """
<div style="position: fixed; bottom: 50px; left: 50px; width: 220px; height: 120px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color:white;
            ">&nbsp; Climate Types <br>
    &nbsp; <i class="fa fa-square fa-1x" style="color:{}"></i> Type I <br>
    &nbsp; <i class="fa fa-square fa-1x" style="color:{}"></i> Type II <br>
    &nbsp; <i class="fa fa-square fa-1x" style="color:{}"></i> Type III <br>
    &nbsp; <i class="fa fa-square fa-1x" style="color:{}"></i> Type IV
</div>
""".format(
    climate_type_colors["Type I"],
    climate_type_colors["Type II"],
    climate_type_colors["Type III"],
    climate_type_colors["Type IV"],
)

climate_map.get_root().html.add_child(folium.Element(legend_html))

