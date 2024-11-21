class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        ans = m * n - len(guards) - len(walls)

        for r, c in guards:
            grid[r][c] = -1

        for r, c in walls:
            grid[r][c] = -1

        rd = [-1, 1, 0, 0]
        cd = [0, 0, -1, 1]

        for r, c in guards:
            for i in range(4):
                ml = 1
                while True:
                    rt = r + rd[i] * ml
                    ct = c + cd[i] * ml
                    if rt < 0 or rt >= m or ct < 0 or ct >= n or grid[rt][ct] == -1:
                        break
                    else:
                        if grid[rt][ct] != -2:
                            grid[rt][ct] = -2
                            ans -= 1
                    ml += 1

        return ans