class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            letter_counts = [0] * 26

            for char in word:
                letter_counts[ord(char) - ord("a")] += 1

            key = tuple(letter_counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(words))
