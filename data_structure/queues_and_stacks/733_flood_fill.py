class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = [(sr, sc)]
        color = image[sr][sc]
        visited = set()

        while queue:
            x, y = queue.pop()
            visited.add((x, y))
            image[x][y] = newColor
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and (new_x, new_y) not in visited and image[new_x][new_y] == color:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return image
