def get_avg():
    with open('temperature.txt', 'r') as load_file:
        temperature = load_file.readlines()

    temperature = temperature[1:]
    temperature = [float(i) for i in temperature]
    return temperature


average = get_avg()
average = sum(average) / len(average)
print(average)
