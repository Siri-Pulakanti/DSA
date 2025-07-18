https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s=list(columnTitle)
        s.reverse()
        count=0
        for i in range(len(s)):
            count+=(ord(s[i])-64)*26**i
        return count
        
        


        