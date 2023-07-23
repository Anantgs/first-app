length = input("Enter the length : ")
width = input ("Enter the width : ")

try:
    if length == width:
        exit("looks like square")

    area = length*width
    print (area)
except ValueError:
    print("Please enter the number")

