# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution(object):
    def convertRus(self, word, nb_rows):
        i = 0 # row
        is_diagonal = False
        rows = [[] for _ in range(nb_rows)]
        for l in word:
            rows[i].append(l)
            if not is_diagonal:
                is_diagonal = i + 1 >= nb_rows
            else:
                is_diagonal = i != 0
            i += -1 if is_diagonal else 1
                
        ans = ''.join([''.join(row) for row in rows])
        return ans

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows:
            return s

        s = list(s)
        first = numRows - 1
        second = numRows - 2
        jump = first + second
        output = []
        # P A Y P A L I S H I R I N G
        while second >= 0:
            output.append(s.pop(0)) # P, A
            curr = jump # 7, 5
            while curr < len(s):
                output.append(s.pop(curr))# H, S ---> add offset instead
                if first < numRows - 1 and len(s) > curr:
                    output.append(s.pop(curr)) # I
                curr = curr + jump # 14

            first -= 1
            second -= 1
            jump = first + second # 5

        for rest in s:
            output.append(rest)

        ans = ""
        for ch in output:
            ans += ch

        return ans

solution = Solution()

assert str((solution.convertRus("PAYPALISHIRING", 4))) == "PINALSIGYAHRPI"
assert str((solution.convertRus("GOOG", 4))) == "GOOG"
assert str((solution.convertRus("A", 5))) == "A"