global w
w = False
def khayam(n):
    lst = []
    for i in range(n):
        lst.append([1] * (i + 1))
    for i in range(2, n):
        for j in range(1, i):
            lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
    for i in range(len(lst)):
        print(lst[i])
    input1()
    return lst
def input1():
    global w
    if w:
        while w:
            q = input("Do you want to continue? ")
            if q == "yes":
                w = False
                input1()
            if q == "no":
                exit()
            else:
                print(" Error ... try again")
    while True:
        try:
            n = int(input("Enter your Number: "))
            if (type(n) == int) & (n > 0):
                w = True
                khayam(n)
            else:
                print(" Error ... try again ")
        except ValueError:
            print(" \n ERROR >>>>> enter a digit :")
input1()
