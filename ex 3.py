print("Program no 3")
def even(n):
    for i in range(1,n):
        if ( i % 2 == 0 ) or (i % 3 == 0 ):
            print(i,end=" ")
    return
n = eval(input("Enter the Value: "))
even(n)
