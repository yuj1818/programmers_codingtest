def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            compare = land[i-1].copy()
            compare[j] = 0
            land[i][j] += max(compare)
    answer = max(land[-1])
    print(answer)

solution([[1,2,3,5],[5,6,7,100],[4,3,2,1]])

# land	answer
# [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16
# [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]  20
# [[1,5,3,5], [1,8,1,3], [2,7,3,5]] 18
# [[1,2,3,5],[5,6,7,100],[4,3,2,1]] 107
