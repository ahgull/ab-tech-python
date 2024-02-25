favorite_places = {
    'preston': ['chicago', 'kortrijk'],
    'cassie': ['spokane', 'ecuador', 'anaheim'],
    'joe': ['pittsburgh', 'snoqualmie', 'redlands']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")