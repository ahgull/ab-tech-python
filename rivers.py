rivers = {
    'amazon' : 'brazil',
    'yangtze' : 'china',
    'danube' : 'germany',
}
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}."),
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())