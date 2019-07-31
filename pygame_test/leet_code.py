class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()

        vowel = ('a', 'e', 'i', 'o', 'u')

        for i in range(len(words)):

            if words[i][0].lower() in vowel:
                words[i] += "ma"
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"

            for j in range(i + 1):
                words[i] += 'a'

            words[i] += ' '

        words[-1] = words[-1][:-1]

        return ''.join(words)


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))