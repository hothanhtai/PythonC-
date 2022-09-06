def inputData():
    print("Nhap 2 so a,b\n")
    a = float(input("a= "))
    b = float(input("b= "))
    return a,b
def Sum(a,b):
    c=a+b
    return c
def main():
    a,b = inputData()
    c = Sum(a,b)
    print("%.2f"%a,"+","%.2f"%b,"="," %.2f"%c)
if __name__ == "__main__":
    main()