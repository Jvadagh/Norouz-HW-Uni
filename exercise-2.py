def GCD(first, second):  # GCD : greatest common divisor
    if first > second:
        BMM = second
    elif second >= first:
        BMM = first
    while BMM >= 1:
        if first % BMM == 0 and second % BMM == 0:
            print("G.C.D is ", BMM)
            break
        else:
            BMM -= 1
            if first % BMM == 0 and second % BMM == 0:
                return print("B.M.M is", BMM)
if __name__ == '__main__':
    FirstNum=int(input("insert first number : "))
    SecondNum=int(input("insert second number : "))
    GCD(FirstNum,SecondNum)