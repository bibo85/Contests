# time complexity - O(n)
# space complexity - O(1)

class Solution:
    def romanToInt(self, s: str) -> int:

        letter_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        answer = 0
        prev = 0
        for letter in s[::-1]:
            if letter_dict[letter] < prev:
                answer -= letter_dict[letter]
            elif letter_dict[letter] >= prev:
                answer += letter_dict[letter]
            prev = letter_dict[letter]

        return answer
