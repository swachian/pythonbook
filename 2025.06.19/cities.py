cities = {
    'Shanghai': {'country': 'China', 'population': 20_000_000, 'fact': 'The largest city in China'},
    'London': {'country': 'England', 'population': 18_000_000, 'fact': 'The old center of the world'}
}

for city, city_info in cities.items():
    print(f"\n{city} is in {city_info['country']}, she has about {city_info['population']:,} population")

def describe_city(city, country = "China"):
    print(f"{city.title()} is in {country.title()}")

describe_city("beijing")
describe_city("shanghai")
describe_city("London", "England")

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("beijing", "China"))
print(city_country("Santiago", "Chile"))