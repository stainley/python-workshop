employees = [{
    'name': 'John Mckee',
    'age': 38,
    'department': 'sales'
}, {
    'name': 'Lisa Crawford',
    'age': 29,
    'department': 'marketing'
}, {
    'name': 'Sujan Patel',
    'age': 33,
    'department': 'hr'
}]

print(employees[1])

items = ['apple', 'orange', 'banana']

quantity = [5, 3, 2]

orders = zip(items, quantity)
print(list(orders))

orders = zip(items, quantity)
print(tuple(orders))

orders = zip(items, quantity)
orders = dict(orders)

print(list(orders.keys()))

for tuple in list(orders.items()):
    print(tuple)