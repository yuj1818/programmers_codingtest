def solution(dirs):
    visited = set()
    current = [0,0]
    for dir in dirs:
        prev = current.copy()
        if dir == 'U':
            if current[1] < 5:
                current[1] += 1
            else:
                continue
        elif dir == 'D':
            if current[1] > -5:
                current[1] -= 1
            else:
                continue
        elif dir == 'L':
            if current[0] > -5:
                current[0] -= 1
            else:
                continue
        elif dir == 'R':
            if current[0] < 5:
                current[0] += 1
            else:
                continue
        #좌 -> 우, 좌 <- 우 방향이 달라도 같은 길을 지나간걸로 치기 때문에 정렬 사용
        visited.add(tuple(sorted([tuple(prev) ,tuple(current)])))
    
    print(len(visited))

solution("LULLLLLLU")

# dirs	answer
# "ULURRDLLU"	7
# "LULLLLLLU"	7
