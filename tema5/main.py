import os
from utils import get_input, parse_to_json, get_cars_by_criteria

if __name__ == '__main__':
    header, data = get_input('input.csv')
    data = parse_to_json(header, data)
    print('data', data)


    os.makedirs(os.path.join('output_data'), exist_ok=True)

    slow_cars = get_cars_by_criteria(data, key= 'hp', max_=120)
    fast_cars = get_cars_by_criteria(data, key='hp', min_=120, max_=180)
    sport_cars = get_cars_by_criteria(data, key='hp', min_=180)

    cheap_cars = get_cars_by_criteria(data, key= 'price', max_=1000)
    medium_cars = get_cars_by_criteria(data, key='price', min_=1000, max_=5000)
    expensive_cars = get_cars_by_criteria(data, key='price', min_=5000)

    print('slow cars', slow_cars)
    print('fast cars', fast_cars)
    print('sport_cars', sport_cars)
    print('cheap cars', cheap_cars)
    print('medium cars', medium_cars)
    print('slow cars', slow_cars)


