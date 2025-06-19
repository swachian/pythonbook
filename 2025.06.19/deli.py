sandwich_orders = ['tuna', 'italy', 'fish', 'tuna']
finished_sandwiches = []

print("tuna is sold out")
while 'tuna' in sandwich_orders:
    sandwich_orders.remove('tuna')
    print("remove tuna")

while sandwich_orders:
    sandwich = sandwich_orders[0]
    print(f"Finish {sandwich}")
    finished_sandwiches.append(sandwich)
    del sandwich_orders[0]

print("\nWe have made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")