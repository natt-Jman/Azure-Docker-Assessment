import os
counter_file = '/data/counter.txt'
with open(counter_file, 'r') as f:
    counter = int(f.read().strip())
print(f'Fetched counter value: {counter}')
