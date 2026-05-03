from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)


all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lats = [lat['geometry']['coordinates'][1] for lat in all_eq_dicts]
lons = [lon['geometry']['coordinates'][0] for lon in all_eq_dicts]
eq_titles = [eq_title['properties']['title'] for eq_title in all_eq_dicts]

title = "Global Earthquakes"
fig = px.scatter_geo(lat = lats, lon = lons, title = title, size=mags,
                    color=mags, # the color scheme will be based on the magnitude of each event
                    color_continuous_scale='aggrnyl', # theme for the color scheme
                    labels={'color':'Magnitude'}, # label based on the color scheme, with the name "Magnitude"
                    projection='natural earth',
                    hover_name=eq_titles,
                     )
fig.show()