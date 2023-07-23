password = input("Entert the password : ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["Upper"] = upper

if all(result.values()):
    print("Strong Password")
else:
    print("Week password")

print(result)
print(result.values())