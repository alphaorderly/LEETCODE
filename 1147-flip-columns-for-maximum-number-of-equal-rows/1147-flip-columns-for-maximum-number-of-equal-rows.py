class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            rev_row = "".join('1' if n == 0 else '0' for n in row)
            nor_row = "".join(str(n) for n in row)

            patterns[nor_row] += 1
            patterns[rev_row] += 1


        return max(patterns.values())