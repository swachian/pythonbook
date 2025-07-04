from pathlib import Path
import json

import plotly.express as px

path = Path('eq_data/eq_1_day_m1.geojson')
contents = path.read_text("UTF-8")

all_eq_data = json.loads(contents)

# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, eq_titles = zip(*[(eq_dict['properties']['mag'], eq_dict['geometry']['coordinates'][0], eq_dict['geometry']['coordinates'][1], eq_dict['properties']['title'] )for eq_dict in all_eq_dicts])

title = all_eq_data['metadata']['title'] # "Global Earthquakes"

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                    color=mags, color_continuous_scale='plasma',
                    labels={'color':'Magnitude'},
                    projection='natural earth',
                    hover_name=eq_titles,
        ) 
fig.show()