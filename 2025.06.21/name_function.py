def get_formatted_name(first, last, middle = ''):
    full_name = ''
    if not middle:
        full_name = f"{first} {last}"
    else:
        full_name = f"{first} {last} {middle}"
    return full_name.title()

def get_city_country(city, country, population = 0):
    if population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"