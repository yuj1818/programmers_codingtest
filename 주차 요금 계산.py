import math

def solution(fees, records):
    answer = []
    arr = []
    rec_dict = dict()
    result = dict()
    for record in records:
        arr = record.split(" ")
        h, m = map(int, arr[0].split(":"))
        time = h*60 + m
        car_num = arr[1]
        inout = arr[2]
        if inout == "IN":
            if car_num in rec_dict:
                rec_dict[car_num]["total_time"] -= time
                rec_dict[car_num]["exist"] = 1
            else:
                rec_dict[car_num] = dict()
                rec_dict[car_num]["total_time"] = -1 * time
                rec_dict[car_num]["exist"] = 1
        else:
            rec_dict[car_num]["total_time"] += time
            rec_dict[car_num]["exist"] = 0
        
    for car in rec_dict:
        if rec_dict[car]["exist"] == 1:
            rec_dict[car]["total_time"] += 1439
        if rec_dict[car]["total_time"] > fees[0]:
            total_fee = fees[1] + math.ceil((rec_dict[car]["total_time"] - fees[0])/fees[2])*fees[-1]
        else:
            total_fee = fees[1]
        result[car] = total_fee

    result = sorted(result.items())

    for num, fee in result:
        answer.append(fee)

    return answer
            
solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])

# fees	records	result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
# [1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
