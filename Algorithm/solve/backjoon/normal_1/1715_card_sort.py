import sys
import heapq

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_heap = []
    for _ in range(n):
        heapq.heappush(n_heap, int(sys.stdin.readline()))

    if n != 1:
        compare_count = 0
        while len(n_heap) > 1:
            min_sum = heapq.heappop(n_heap) + heapq.heappop(n_heap)
            compare_count += min_sum
            heapq.heappush(n_heap, min_sum)
        print(compare_count)
    else:
        print(0)
