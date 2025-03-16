def generate_square(n):
    list = []
    for i in range(n):
        list.append(str(n * '*'))

    return list

n = 5
print(generate_square(n))
