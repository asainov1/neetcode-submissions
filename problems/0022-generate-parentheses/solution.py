class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, substring):
            # Использовали n открывающих и n закрывающих
            if open_count == n and close_count == n:
                res.append(substring)
                return

            # Можно добавить "(" пока их меньше n
            if open_count < n:
                backtrack(
                    open_count + 1,
                    close_count,
                    substring + "("
                )

            # Можно добавить ")" только если есть незакрытая "("
            if close_count < open_count:
                backtrack(
                    open_count,
                    close_count + 1,
                    substring + ")"
                )

        backtrack(0, 0, "")
        return res
