import os
counter_file = '/data/counter.txt'
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        f.write('0')
with open(counter_file, 'r') as f:
    counter = int(f.read().strip())
counter += 1
with open(counter_file, 'w') as f:
    f.write(str(counter))
# print(f'Counter value: {counter}')
