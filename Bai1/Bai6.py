def inputData():
    n = int(input("n= "))
    return n

def giaiThua(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

def main():
    n = inputData()
    s = giaiThua(n)
    print("%d"%n,"!"," = ","%d"%s)

if __name__ =="__main__":
    main()
