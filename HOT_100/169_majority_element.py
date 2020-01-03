class Solution:
    # 摩尔投票法
    # O(n) O(1)
    def majorityElement(self, nums):
        majority = nums[0]
        count = 1
        for i in nums[1:]:
            if i == majority:
                count += 1
            elif count > 0:
                count -= 1
            else:
                majority = i
                count = 1
        return majority


# 扩展：找出>n/3的最多两个数 [229]求众数2

def major(nums):
    c1 = c2 = 0
    major1 = major2 = None
    for i in nums:
        if i == major1:
            c1 += 1
        elif i == major2:
            c2 += 1
        elif c1 == 0:
            c1 = 1
            major1 = i
        elif c2 == 0:
            c2 = 1
            major2 = i
        else:
            c1 -= 1
            c2 -= 1

    return [m for m in (major1, major2) if m is not None and nums.count(m) > len(nums)/3]


print(major([0, 0, 0]))
