

username = input("Enter the username : ") + "\n"

file = open('members.txt', "r")
saved_list = file.readlines()
file.close()

saved_list.append(username)

file = open('members.txt', 'w')
file.writelines(saved_list)
file.close()



