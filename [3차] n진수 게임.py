def solution(n, t, m, p):
    answer = ''
    count = 0
    total = ''
    i = 0
    num = 0
    while True:
        trans = ''
        i = num
        while i >= n:
            if i % n >= 10:
                trans = chr(65+(i % n)-10) + trans
            else:
                trans = str(i % n) + trans
            i = i // n
            count += 1
        if i >= 10:
            total += chr(65 + i - 10) + trans
        else:
            total += str(i) + trans
        count += 1
        if count >= m * t:
            break
        num += 1

    for i in range(p-1, m * t, m):
        answer += total[i]
    
    return answer

solution(16,16,2,2)

# n	t	m	p	result
# 2	4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"
