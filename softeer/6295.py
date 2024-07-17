import sys

"""
연습문제 > A+B
문제 주소: https://softeer.ai/practice/6295
해설 주소:
프로그램 작성자: 공학코드(engineeringcode93@gmail.com)
"""

T = sys.stdin.readline()

for i in range(int(T)):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i+1) + ": " + str(a+b))

"""
Case 1
Input
5
1 1
2 3
3 4
9 8
5 2
Output
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
"""