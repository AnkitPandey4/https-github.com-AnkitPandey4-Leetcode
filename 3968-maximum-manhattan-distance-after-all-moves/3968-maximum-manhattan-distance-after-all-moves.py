class Solution:
    def maxDistance(self, moves: str) -> int:
        x = 0
        y = 0
        wildcards = 0
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1  
            elif move == '_':
                wildcards += 1
        return abs(x) + abs(y) + wildcards                      
        