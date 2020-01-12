# 需要安排最少的会议室

'''
贪婪思想：
1.会议按照起始时间进行
2.要给新的即将开始的会议找会议室时，先看当前有无空的会议室
3.有则在空会议室开会，没有则开一间新的会议室

'''


def min_meeting_rooms(intervals):
    # 按照起始时间排序
    intervals.sort(key=lambda x: x[0])

    # 优先队列，按照会议的结束时间排序
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put(intervals[0][::-1])

    for i in range(2, len(intervals)):
        # 优先队列会保证，在顶部的元素是结束时间最早的
        interval = q.get()
        # 最近的会议结束时间和当前会议要开始的时间进行比较
        if intervals[i][0] >= interval[0]:
            interval[0] = intervals[i][0]
        else:
            q.put(intervals[i][::-1])
        q.put(interval)
    return q.qsize()


if __name__ == "__main__":
    intervals = [[7, 10], [2, 4]]
    # check if the result is 1
    print(min_meeting_rooms(intervals))
