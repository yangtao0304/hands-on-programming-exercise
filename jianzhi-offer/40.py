from typing import List


class Solution:
    # heap sort
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k <= 0 or k > len(arr):
            return []

        def build_heap(arr):
            for i in range(len(arr)//2-1, -1, -1):
                heap_adjust(arr, i)
            return arr

        def heap_adjust(arr, i):
            child = 2*i+1
            length = len(arr)
            while child < length:
                if child+1 < length and arr[child+1] > arr[child]:
                    child += 1
                if arr[child] > arr[i]:
                    arr[i], arr[child] = arr[child], arr[i]
                    i = child
                    child = 2*i+1
                else:
                    break

        heap = build_heap(arr[:k])
        for i in range(k, len(arr)):
            if heap[0] > arr[i]:
                heap[0] = arr[i]
                heap_adjust(heap, 0)
        return heap

    # quick sort
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, left, right):
            pivot = arr[right]
            loc = left-1
            for i in range(left, right):
                if arr[i] < pivot:
                    loc += 1
                    arr[loc], arr[i] = arr[i], arr[loc]
            arr[loc+1], arr[right] = arr[right], arr[loc+1]
            return loc+1

        if k == 0:
            return []

        left = 0
        right = len(arr)-1
        idx = partition(arr, left, right)
        while idx != k-1:
            if idx < k-1:
                left = idx+1
                idx = partition(arr, left, right)
            elif idx > k-1:
                right = idx-1
                idx = partition(arr, left, right)
        # print(arr[:k])
        return arr[:k]


if __name__ == "__main__":
    s = Solution()
    s.getLeastNumbers2([3, 2, 1], 2)
