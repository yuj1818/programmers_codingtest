from itertools import product

def solution(input):
    ch = ['A','E','I','O','U']
    word = ''
    count = 0

    for c1 in ch:
        word = c1
        count += 1
        if word == input:
            return count
        for c2 in ch:
            prev1 = word
            word += c2
            count += 1
            if word == input:
                return count
            for c3 in ch:
                prev2 = word
                word += c3
                count += 1
                if word == input:
                    return count
                for c4 in ch:
                    prev3 = word
                    word += c4
                    count += 1
                    if word == input:
                        return count
                    for c5 in ch:
                        prev4 = word
                        word += c5
                        count += 1
                        if word == input:
                            return count
                        word = prev4
                    word = prev3
                word = prev2
            word = prev1

solution("AAAAE")

# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189
