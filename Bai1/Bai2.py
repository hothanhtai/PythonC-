#======Giai phuong trinh bac 1==========
import math;
#-------Ham input data------------------
def inputData():
    a = float(input("Nhap a= "))   
    b = float(input("Nhap b= "))
    return a,b
    
#------------Ham tinh nghiem-----------------------
def solveEqual(a,b):
    if a==0:
        if b==0:
            print("phuong trinh vo so nghiem")
        else: 
            print("phuong trinh vo nghiem")
    else:
        x = -b/a
        print("Nghiem x= %.3lf"%x,end = "\n")
#-------------Ham Main-------------------------
def main():
    a,b = inputData()
    solveEqual(a,b)

if __name__=="__main__":
        main()