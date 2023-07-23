feet_inches = input("Enter the feet and inches input : ")
print(feet_inches)


def convert(feet_inches_arg):
    list_arg = feet_inches_arg.split(" ")
    feet = int(list_arg[0])
    inches = int(list_arg[1])

    meter = feet * 0.304 + inches * 0.0254

    return meter


height = convert(feet_inches)
print(height)
if height < 1:
    print("Kid is too small")
else:
    print("Kid id highted")
