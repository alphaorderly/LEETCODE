class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            rev_row = tuple(1 if n == 0 else 0 for n in row)

            patterns[tuple(row)] += 1
            patterns[rev_row] += 1


        return max(patterns.values())