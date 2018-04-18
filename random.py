import random

random_items = [random.randint(-50, 100) for c in range(32)]

print( 'Before: ', random_items)
insertion_sort(random_items)
print ('After : ', random_items)
