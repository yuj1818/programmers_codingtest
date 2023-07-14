from itertools import permutations
def solution(k, dungeons):
    answer = []

    for case in list(permutations(dungeons, len(dungeons))):
        hp = k
        count = 0
        for need, reduce in case:
            if need > hp:
                continue
            else:
                hp -= reduce
                count += 1
        answer.append(count)
        
    return max(answer)
    
solution(80, [[80,20],[50,40],[30,10]])

# k	dungeons	result
# 80	[[80,20],[50,40],[30,10]]	3
