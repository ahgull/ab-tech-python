guests = ['jane goodall', 'henry cavill', 'brandon sanderson']
guests.insert(0, 'frank herbert')
guests.insert(2, 'neil gaiman')
guests.append('bernard cornwell')
guests.sort()
print("The first three items on the list are:")
for guest in guests[:3]:
    print(guest.title())
print("Three items in the middle of the list the list are:")
for guest in guests[2:5]:
    print(guest.title())
print("The last three items on the list are:")
for guest in guests[3:]:
    print(guest.title())