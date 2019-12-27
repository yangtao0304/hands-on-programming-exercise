from typing import List

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）


class Solution:
    # 暴力
    # 每个柱子装水的高度= min(max(left_part),max(right_part))-cur_height
    # 提前储存高度List
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]

        max_left = 0
        for i in range(len(height)):
            left_max[i] = max_left
            if height[i] > max_left:
                max_left = height[i]

        max_right = 0
        for i in reversed(range(len(height))):
            right_max[i] = max_right
            if height[i] > max_right:
                max_right = height[i]

        res = 0
        for i in range(len(height)):
            tmp = min(left_max[i], right_max[i]) - height[i]
            # 这里的left_max, right_max的计算方法，需要过滤掉tmp为负的情况
            if tmp > 0:
                res += tmp

        return res

    # 暴力，超时 O(n^2) + O(1)
    def trap2(self, height: List[int]) -> int:
        # 最左，最右不可能存到水，可以不考虑
        ans = 0
        for i in range(1, len(height)-1):
            max_left, max_right = 0, 0
            # search the left part
            for j in range(i+1):
                max_left = max(max_left, height[j])
            # search the right part
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])

            ans += min(max_left, max_right) - height[i]
        return ans

    # 改进 方法0+方法1 O(n) + O(n)
    def trap3(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]

        # max_left = height[0]
        # for i in range(1, len(height)-1):
        #     max_left = max(height[i], max_left)
        #     left[i] = max_left

        # 由于left数组是递增的，所以可以不实用max_left这一变量
        left[0] = height[0]
        for i in range(1, len(height)-1):
            left[i] = max(height[i], left[i-1])

        # max_right = height[-1]
        # for i in reversed(range(1, len(height)-1)):
        #     max_right = max(height[i], max_right)
        #     right[i] = max_right

        # right数组,同
        right[-1] = height[-1]
        for i in reversed(range(1, len(height)-1)):
            right[i] = max(height[i], right[i+1])

        ans = 0
        for i in range(1, len(height)-1):
            ans += min(left[i], right[i])-height[i]
        return ans

    # 栈的应用

    # 我们可以不用存储最大高度，而是用栈来跟踪可能储水的最长的条形块
    # 使用栈就可以在一次遍历内完成计算

    def trap4(self, height: List[int]) -> int:
        pass

    # 双指针 O(n) + O(1)

    # 我们注意到，只要right_max[i]>left_max[i]，积水高度将由left_max决定
    # 类似的，left_max[i]>right_max[i]，由right_max决定

    # 所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）
    # 当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）
    # 我们必须在遍历时维护 left_max 和 right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成

    def trap5(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = right_max = 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max-height[left]
                left +=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap5([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
