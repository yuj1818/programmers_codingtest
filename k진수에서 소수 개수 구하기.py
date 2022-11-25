def solution(n, k):
    answer = 0
    trans = ""
    arr = []
    if k == 10:
        trans = str(n)
    else:
        while n >= k:
            trans = str(n % k) + trans
            n = n // k
        trans = str(n) + trans
    
    arr = trans.split('0')
    
    for num in arr:
        if num != '':
            num = int(num)
            if num == 1:
                continue
            else:
                for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        break
                else:
                    answer += 1
    return answer

solution(437674, 3)

# n	k	result
# 437674	3	3
# 110011	10	2
