todos = []

while True:
    prompt = "Enter the input add or show or edit or clear or exit: "
    user_input=input(prompt)
    match user_input:
        case 'add':
            todo = input("Enter the item : ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                index = int(index) + 1
                print (f"{index}-{item}")
        case 'edit':
            number = int(input("Enter the item number : "))
            number = number - 1
            new_todo: str = input("Enter new todo : ")
            todos[number] = new_todo
        case 'remove':
            index = int(input("Enter item to be removed : "))
            index = index - 1
            todos.pop(index)
            print (todos)
        case 'clear':
            todos.clear()
        case 'exit':
            break
            print ("Bye")