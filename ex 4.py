print("Program no 4")
first = str(input("Enter your first name: "))
last = str(input("Enter your last name: "))
street = str(input("Enter your street no: "))
number = int(input("Enter your Number: "))
city = str(input("Enter your city name: "))
zip_code = str(input("Enter your zip code: "))
def mailaddress(first, last, street, number, city, zip_code):
    print("{0} {1}\n{2}\n{3}\n{4} {5}".format(first, last, street, number, city, zip_code))
    return
mailaddress(first, last, street, number, city, zip_code)
