def parent(i):
    return (i - 1) // 2
def heapify(list,index, size):
    l=2*index+1
    r=2*index+2
    if l < size and list[l] > list[index]:
        largest = l
    else:
        largest = index
    if r < size and list[r] > list[largest]:
        largest = r
    if largest != index:
        list[largest], list[index] = list[index], list[largest]
        heapify(list, largest, size)
def build_max_heap(list):
    start = parent(len(list) - 1)
    while start >= 0:
        heapify(list, start, len(list))
        start = start - 1
def heapsort(list):
    build_max_heap(list)
    for i in range(len(list) - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        heapify(list, 0, i)
g=[54,7,2,9,85,3,0,38,456,31,41]
heapsort(g)
print(g)