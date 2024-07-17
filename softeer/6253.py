import sys

"""
연습문제 > 주행거리 비교하기
문제 주소: https://softeer.ai/practice/6253
해설 주소:
프로그램 작성자: 공학코드(engineeringcode93@gmail.com)
"""

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("same")

"""
Case 1
Input
3500 2000
Output
A

Case 2
Input
1500 1800
Output
B

Case 3
Input
5000 5000
Output
same
"""