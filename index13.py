def solu(userinput):
    answer_list = 0
    for check in range(0,int(userinput[2])):
        answer_list += int(userinput[0] * (check + 1))
    return answer_list - int(userinput[1])
if __name__ == "__main__":
    input1 = list(input().split(""))
    if solu(input1) <= 0:
        print("0")
    else:
        print(solu(input1))            