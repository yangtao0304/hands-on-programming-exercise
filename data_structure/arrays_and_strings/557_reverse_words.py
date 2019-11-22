class Solution(object):
    def reverse_words(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([''.join(reversed(i)) for i in s.split()])

    # 'str' object does not support item assignment
    #  just show the idea

    # def reverse_words_2(self, s):
    #     # reverse str
    #     def reverse(front, tail, s):
    #         while front < tail:
    #             s[front], s[tail] = s[tail], s[front]
    #             front += 1
    #             tail -= 1
    #     # find the space
    #     front = 0
    #     for i in range(len(s)):
    #         if s[i] == ' ':
    #             reverse(front, i-1, s)
    #             front = i+1
    #     reverse(front, len(s)-1, s)
    #     return s

if __name__ == "__main__":
    s = Solution()
    print(s.reverse_words("Let's take LeetCode contest"))

            
