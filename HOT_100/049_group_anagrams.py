# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串

from typing import List
import collections


class Solution:
    # key-value
    # 字符串排序后，存储为散列化元组
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i in strs:
            d[tuple(sorted(i))].append(i)
        return d.values()

    # 按计数分类
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            d[tuple(count)].append(s)

        return d.values()


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
