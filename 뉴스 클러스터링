import re
import math
def solution(str1, str2):
    answer = 0
    multi_sig = 0
    reg = re.compile('[a-zA-Z]')
    arr1 = []
    arr2 = []
    intersect = 0
    union = 0
    for i in range(len(str1)-1):
        if bool(reg.match(str1[i])) and bool(reg.match(str1[i+1])):
            pair = str1[i].upper()+str1[i+1].upper()
            if pair in arr1:
                multi_sig = 1
            arr1.append(pair)
    for j in range(len(str2)-1):
        if not(not(reg.match(str2[j]))) and not(not(reg.match(str2[j+1]))):
            pair = str2[j].upper()+str2[j+1].upper()
            if pair in arr2:
                multi_sig = 1
            arr2.append(str2[j].upper()+str2[j+1].upper())

    if multi_sig:
        result = []
        temp = arr1.copy()
        for i in arr2:
            if i in temp:
                temp.remove(i)
                result.append(i)
        intersect = len(result)
        union = len(arr1)+len(arr2)-intersect
    else:
        intersect = len(list(set(arr1) & set(arr2)))
        union = len(list(set(arr1) | set(arr2)))

    if intersect + union == 0:
        answer = 65536
    else:
        answer = int(intersect/union*65536)

    return answer

solution("aa1+aa2", "AA12")

# str1	str2	answer
# FRANCE	french	16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	43690
# E=M*C^2	e=m*c^2	65536
# aa1+aa2   AA12    32768
