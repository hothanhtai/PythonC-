def inputData():
    n = int(input("n= "))
    return n
def giaiThua(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def tongLe(n):
    s=0
    for i in range(1,n+1,2):
        s+=i
    return s
def dieuKien(n):
      if n%2 != 0:
        k = giaiThua(n)
        print("%d"%n,"!"," =","%d"%k)
        return k
      else:
        ss = tongLe(n)
        print("Tong cac so le la: %d"%ss)
        return ss
def main():
    n = inputData()
    dieuKien(n)
  
if __name__ == "__main__":
    main()
