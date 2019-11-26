print("program no 5")
import time
def month(n):
    mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if n >= 13 or n == 0 :
        print("Value is not in month")
    else:
        print(mon[n-1])
    return
n = int(input("Enter the value: "))
month(n)