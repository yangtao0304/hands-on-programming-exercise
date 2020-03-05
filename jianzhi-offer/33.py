class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        if len(postorder) == 1:
            return True

        root = postorder[-1]
        idx = -1
        for i in range(len(postorder)):
            if postorder[i] > root:
                idx = i
                break

        if idx != -1:
            print(idx)
            for i in postorder[idx:-1]:
                if i < root:
                    return False

        left = True if idx == 0 else self.verifyPostorder(postorder[:idx])
        right = True if idx == -1 else self.verifyPostorder(postorder[idx:-1])

        return left and right
