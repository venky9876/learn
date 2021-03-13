# Design an algorithm for computing the running median of a sequence.

### Hint : Avoid looking at all values each time you read a new value.
import heapq

def online_median(sequence):

    min_heap  = []
    max_heap = []

    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5*(min_heap[0] + (-max_heap[0])) if len(min_heap)== len(max_heap) else min_heap[0])

    return result

