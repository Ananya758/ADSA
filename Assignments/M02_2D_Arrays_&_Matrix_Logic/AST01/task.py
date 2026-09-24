#Task
from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = []
    
    r, c = rStart, cStart
    result.append([r, c])
    
    steps = 1
    
    while len(result) < rows * cols:
        # Move East
        for _ in range(steps):
            c += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        # Move South
        for _ in range(steps):
            r += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        steps += 1
        
        # Move West
        for _ in range(steps):
            c -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        # Move North
        for _ in range(steps):
            r -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        steps += 1
    
    return result


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))