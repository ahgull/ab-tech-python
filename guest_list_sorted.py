guests = ['jane goodall', 'henry cavill', 'brandon sanderson']
table_message = f"Dear guests, I have found a larger table and shall thus be inviting a few more distinguished individuals."
print(table_message)
guests.insert(0, 'frank herbert')
guests.insert(2, 'neil gaiman')
guests.append('bernard cornwell')
guests.sort()
message = f'Dear {guests[0].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)
message = f'Dear {guests[1].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)
message = f'Dear {guests[2].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)
message = f'Dear {guests[3].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)
message = f'Dear {guests[4].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)
message = f'Dear {guests[5].title()}, I would be honored if you would join me for a dinner party on a date to be determined in the future.'
print(message)