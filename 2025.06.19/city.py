cities = {
    'Shanghai': {'country': 'China', 'population': 20_000_000, 'fact': 'The largest city in China'},
    'London': {'country': 'England', 'population': 18_000_000, 'fact': 'The old center of the world'}
}

for city, city_info in cities.items():
    print(f"\n{city} is in {city_info['country']}, she has about {city_info['population']:,} population")