class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                last_open = stack.pop()
                if last_open != matching_open[char]:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    examples = ["()", "()[]{}", "(]", "([)]", "{[]}"]

    for example in examples:
        print(f"{example!r} -> {solution.isValid(example)}")
