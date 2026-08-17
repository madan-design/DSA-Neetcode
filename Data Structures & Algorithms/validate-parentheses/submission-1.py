class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        array = []
        for char in s:
            if char in map:
                top_element = array.pop() if array else '#'
                if map[char]!=top_element:
                    return False
            else:
                array.append(char)
        return len(array)==0