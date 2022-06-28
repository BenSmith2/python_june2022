def generate_checkerboard(x, y):
    result = []
    for j in range(0, x):
        list_temp = []
        for i in range(0, y):
            list_temp.append((j+i) % 2)
        result.append(list_temp)

    return result