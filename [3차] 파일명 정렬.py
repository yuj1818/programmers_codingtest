def solution(files):
    answer = []
    file_dict = dict()
    for file in files:
        file_dict[file] = dict()
        head = 0
        number = 0
        for c in file:
            if str.isdigit(c):
                break
            else:
                head += 1
        file_dict[file]["head"] = file[:head].upper()
        for c in file[head:]:
            if str.isdigit(c):
                number += 1
            else:
                break
        file_dict[file]["number"] = int(file[head:head+number])
        file_dict[file]["tail"] = file[head+number:]
    file_dict = sorted(file_dict.items(), key=lambda x:(x[1]["head"], x[1]["number"]))
    
    for file in file_dict:
        answer.append(file[0])

    print(answer)
        
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

# 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
