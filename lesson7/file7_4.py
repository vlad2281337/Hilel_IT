def common_elements():
    a = {i for i in range(100) if i % 3 == 0}
    b = {i for i in range(100) if i % 5 == 0}
    return a & b

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print('OK, the result is:')
print(common_elements())
