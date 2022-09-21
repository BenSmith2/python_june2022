def generate_checkerboard(x, y):
    result = []
    for j in range(0, x):
        list_temp = []
        print(f'result list {result}')
        for i in range(0, y):
            print(f'j {j}')
            print(f'i {i}')
            list_temp.append((j+i) % 2)
            print(f'list_temp {list_temp}')
        result.append(list_temp)

    return result

print(generate_checkerboard(4,4))