class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        x = 0
        total = 0
        letters = list(s)
        
        while x < len(letters):
            if (x + 1 < len(letters)) and (values.get(letters[x+1]) > values.get(letters[x])):
                total -= values.get(letters[x])
            else:
                total += values.get(letters[x])
            x += 1
                
        return total
            
