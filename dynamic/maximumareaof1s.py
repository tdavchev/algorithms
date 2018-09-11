class Solution(object):
    def getMaxArea(self, heights):
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)

            stack.append(i)
        heights.pop()
        return result

    def maximum(self, _input):
        temp = [0 for _ in range(len(_input[0]))]
        maxArea = 0
        area = 0
        for i in range(len(_input)):
            for j in range(len(temp)):
                if _input[i][j] == 0:
                    temp[j] = 0
                else:
                    temp[j] += 1
            area = self.getMaxArea(temp)
            if area > maxArea:
                maxArea = area

        return maxArea