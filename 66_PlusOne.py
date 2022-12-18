class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringOfDigits = map(str, digits)
        intOfDigits = (int(''.join(stringOfDigits)) + 1)
        return list(map(int, list(str(intOfDigits))))
