import heapq
def heap_sort(items):
    heapq.heapify(items)
    items[:]=[heapq.heappop(items) for i in range(len(items))]
items=[2,5,7,9,11,55,44]
print(heap_sort)
print(heapq)
