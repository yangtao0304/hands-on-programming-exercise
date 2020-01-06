# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 归并排序 O(nlogn) 稳定
    # 1.快慢指针找中点；2.递归调用；3.合并两个链表
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        right_node = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(right_node)

        def merge2(l, r):
            if not l:
                return r
            if not r:
                return l

            if l.val <= r.val:
                l.next = merge(l.next, r)
                return l
            else:
                r.next = merge(l, r.next)
                return r

        def merge(l, r):
            head = ListNode(-1)
            tmp = head
            while l != None and r != None:
                if l.val <= r.val:
                    tmp.next = l
                    l = l.next
                else:
                    tmp.next = r
                    r = r.next
                tmp = tmp.next
            tmp.next = l if l else r
            return head.next

        return merge(l, r)

    # 链表快排 O(nlogn) 不稳定
    # 值交换
    def sortList2(self, head: ListNode) -> ListNode:
        def quick_sort(head, tail):
            # 链表范围为 [head,tail)
            if head != tail and head.next != tail:
                mid = partition(head, tail)
                quick_sort(head, mid)
                quick_sort(mid.next, tail)

        def partition(low, high):
            pivot = low.val
            loc = low
            cur = loc.next
            while cur != high:
                if cur.val < pivot:
                    loc = loc.next
                    # swap loc.val, cur.val
                    tmp = cur.val
                    cur.val = loc.val
                    loc.val = tmp
                cur = cur.next
            # swap low.val, loc.val
            low.val = loc.val
            loc.val = pivot
            return loc

        quick_sort(head, None)
        return head


# 补充：快排
def partition1(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low


def partition2(arr, low, high):
    pivot = arr[high]
    loc = low-1
    for i in range(low, high):
        if arr[i] < pivot:
            loc += 1
            # swap loc,i
            arr[i], arr[loc] = arr[loc], arr[i]
    # swap loc+1,high
    arr[loc+1], arr[high] = arr[high], arr[loc+1]

    return loc+1


def partition3(arr, low, high):
    pivot = arr[low]
    loc = low
    for i in range(low+1, high+1):
        if arr[i] < pivot:
            # swap i,loc+1
            loc += 1
            arr[i], arr[loc] = arr[loc], arr[i]
    # swap loc, low
    arr[loc], arr[low] = arr[low], arr[loc]
    return loc


def quick_sort(arr, low, high):
    if low < high:
        mid = partition3(arr, low, high)
        quick_sort(arr, low, mid-1)
        quick_sort(arr, mid+1, high)

# 补充堆排序


def heap_sort(nums):
    # 构建大顶堆
    for i in range(len(nums)//2-1, -1, -1):
        heap_adjust(nums, i, len(nums))

    for i in range(len(nums)-1, 0, -1):
        # swap
        nums[i], nums[0] = nums[0], nums[i]
        heap_adjust(nums, 0, i)


def heap_adjust(nums, i, length):
    tmp = nums[i]
    child = 2*i+1
    while child < length:
        if child+1 < length and nums[child+1] > nums[child]:
            child += 1
        if nums[child] > nums[i]:
            nums[i] = nums[child]
            i = child
            child = 2*i+1
        else:
            break
        nums[i] = tmp


if __name__ == "__main__":
    nums = [3, 5, -1, 2, 10, 2, 2]
    heap_sort(nums)
    print(nums)
