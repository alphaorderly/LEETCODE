class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            # 기준 패턴: 첫 번째 값에 따라 0 또는 1로 시작
            pattern = tuple(n ^ row[0] for n in row)  
            patterns[pattern] += 1

        return max(patterns.values())
