def my_function(x, y, z):
    consistency = [x, y, z]
    absolute = []
    max_1 = max(consistency)
    absolute.append(max_1)
    consistency.remove(max_1)
    max_2 = max(consistency)
    absolute.append(max_2)
    print(sum(absolute))


my_function(-4, 2, 0)
