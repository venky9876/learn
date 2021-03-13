# Write a program which takes as input a very long sequence of numbers and prints the numbers in sorted order. Each number is at most k away from its correcctly sorted position.

### Hint : How many  numbers must you read after reading the ith number to be sure you can replace it in the correct location ?
import itertools
import heapq

def sort_approx_array(sequence, k):
    result = []
    min_heap = []

    for x in itertools.islice(sequence,k):
        heapq.heappush(min_heap,x)

    for x in sequence:
        smallest = heapq.heappushpop(min_heap,x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

