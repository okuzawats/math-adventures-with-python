def average(a, b):
    return (a + b) / 2


def my_sum(sum):
    running_sum = 0
    for i in range(1, sum + 1):
        running_sum += i
    return running_sum


def my_sum_2(sum):
    running_sum = 0
    for i in range(sum + 1):
        running_sum += i ** 2 + 1
    return running_sum


def average_3(num_list):
    return sum(num_list) / len(num_list)


print(my_sum(100))
print(my_sum(1000))
print(average_3([8, 11, 15]))

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16,
     25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75, ]

print(average_3(d))
