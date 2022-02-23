def bin2dec(num):
    lst = list(num)
    # print(lst)
    dec = 0
    # for c in num:
    #     lst.append(c)
    pos = len(lst) - 1
    for i in lst:
        dec += int(i)*(2**pos)
        pos -= 1
    print(num, "in decimal =>", dec, '\n')


while True:
    num = input("Enter a binary number: ")
    if not num:
        break
    else:
        try:
            bin2dec(num)
        except:
            print("Invalid input")
