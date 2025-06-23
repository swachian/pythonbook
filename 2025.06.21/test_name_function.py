from name_function import get_formatted_name, get_city_country

def test_first_last_name():
    formatted_name = get_formatted_name('hans', 'Jenkins')
    assert formatted_name == "Hans Jenkins"

def test_first_middle_last_name():
    formatted_name = get_formatted_name('hans', "don", 'jenkins')
    assert formatted_name == "Hans Don Jenkins"

def test_city_country():
    assert get_city_country('Santiago', 'Chile') == 'Santiago, Chile'

def test_city_country_with_population():
    assert get_city_country('Santiago', 'Chile', 5_000_000) == 'Santiago, Chile - population 5000000'