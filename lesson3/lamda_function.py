import math

add_up = lambda x, y: x + y

print(add_up(2, 5))

first_time = lambda my_list: my_list[0]

print(first_time(['cat', 'dog', 'mouse']))

names = ['Magda', 'Jose', 'Anne']
lengths = []

lengths = list(map(len, names))

print(sum(lengths) / len(lengths))

nums = [-3, -5, 1, 4]

print(list(map(lambda x: 1 / (1 + math.exp(-x)), nums)))

names = ['Karen', 'Jin', 'Kim']

print(list(filter(lambda name: len(name) == 3, names)))

nums = list(range(1000))

filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)

print(sum(filtered))

names = ['Ming', 'Jennifer', 'Andrew', 'Boris']

print(sorted(names, key=lambda x: len(x)))
