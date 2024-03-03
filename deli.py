sandwich_orders = ['pastrami', 'cuban', 'tuna']
finished_sandiwches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Your {current_order} sandwich is being made.")
    finished_sandiwches.append(current_order)

print("\nThe following orders are ready for pickup:")
for finished_sandwich in finished_sandiwches:
    print(finished_sandwich.title())