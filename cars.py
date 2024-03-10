def car_info(make, model, **car_options):
    """Build a car profile."""
    car_options['make'] = make
    car_options['model'] = model
    return car_options

car_profile = car_info('audi', 'etron', trim='prestige', color='grey')

print(car_profile)