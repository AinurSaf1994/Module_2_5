# def say_hello(name):
#     print('Hello', name)
#
# say_hello('Ainur')
# say_hello('Vika')
# say_hello('Mars')

# import random
# def lottery(*args, **kargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
# win1, win2 = lottery(1,2,3)
# print(win1, win2)

# def test(a=2, b=True):
#     print(a, b)
#
# test(False, 'Ok')

def get_matrix(n, m, value):
 matrix = []
 for i in range(n):
     list_ = []
 for j in range(m):
     list_.append(value)
 matrix.append(list_)
 return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
