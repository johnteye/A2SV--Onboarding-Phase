n = int(input())

for _ in range(n):
    input()
    chess = []
    for i in range(0, 8):
        chess.append(list(input()))
    
    for i in range(1, len(chess)- 1):# 0, 8
        if str(chess[i]).count("#") == 1 and (str(chess[i-1]).count("#") == 2 and str(chess[i + 1]).count("#") == 2):

            for index, val in enumerate(chess[i]):
                if val == "#":
                    print(i+ 1, index + 1)
            
      """
      Time complexity: O(N2)
      Space complexity:O(1)
      """
