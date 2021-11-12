import random
import timeit

numb = 9999999
info = [str(random.randint(0, numb)) for i in range(numb)] # 86 MB
file = open('text_file.txt', 'w')
for number in info:
    file.write(number + '\n')

op = """
s2 = 0
f = open('text_file.txt', 'r')
"""

# variant 1
s = """ 
for line in f.readlines():
    s1 = line.strip().isdigit()
    if s1 is True:
        s2 += int(line.strip())
"""
print(timeit.timeit(op+s, number=10))

# variant 2
s = """
for line in f:
    s1 = line.strip().isdigit()
    if s1 is True:
        s2 += int(line.strip())
"""
print(timeit.timeit(op+s, number=10))

# variant 3
s = """
s1 = (int(line.strip()) for line in f if line.strip().isdigit())
s2 = sum(s1)
"""
print(timeit.timeit(op+s, number=10))
