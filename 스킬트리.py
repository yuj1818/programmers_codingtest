def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        stack = ""
        for i in tree:
            if i in skill:
                stack += i
                if stack[0] != skill[0]:
                    break
        else:
            if stack in skill:
                answer += 1
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])

# skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
