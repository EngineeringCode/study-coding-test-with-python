import sys

"""
연습문제 > 위험한 효도
문제 주소: https://softeer.ai/practice/7368
해설 주소:
프로그램 작성자: 공학코드(engineeringcode93@gmail.com)
"""

a, b, d = sys.stdin.readline().split()

a = int(a)
b = int(b)
d = int(d)

n_forward = int(d / a if d > a else 0)
n_reverse = int(d / b if d > b else 0)

t = 2 * d + a * n_reverse + b * n_forward

print(t)

"""
Case 1
Input
7 3 10
Output
44

Case 2
Input
10 3 10
Output
50
"""