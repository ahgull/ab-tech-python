from pathlib import Path
path = Path('guest_book.txt')

prompt = "\nWelcome! Enter your name in the guest book:"
prompt += "\n(Enter 'quit' to close the guest book.) "

guest_book = ""
while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        print(f"Welcome, {name.title()}!")
        guest_book += f"{name}\n"
        path.write_text(guest_book)