def solution(numbers, target):
    answer = 0
    def calcul(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return answer
        else:
            calcul(idx+1, result+numbers[idx])
            calcul(idx+1, result-numbers[idx])
    calcul(0,0)
    return answer                

solution([4, 1, 2, 1], 4)

# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2
