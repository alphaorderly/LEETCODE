class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            rev_row = [1 if n == 0 else 0 for n in row]

            print(row, rev_row)

            patterns[str(row)] += 1
            patterns[str(rev_row)] += 1
        
        return max(patterns.values())