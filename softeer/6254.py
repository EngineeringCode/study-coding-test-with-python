import sys

"""
연습문제 > 근무시간
문제 주소: https://softeer.ai/practice/6254
해설 주소:
프로그램 작성자: 공학코드(engineeringcode93@gmail.com)
"""

work_sum = 0

for i in range(5):

    one_line = sys.stdin.readline()

    lh = int(one_line[0:2])
    lm = int(one_line[3:5])
    rh = int(one_line[6:8])
    rm = int(one_line[9:11])

    if rm - lm < 0:
        rh = rh - 1
        rm = rm + 60

    rm = rm - lm + (rh - lh) * 60

    work_sum = work_sum + rm

print(work_sum)

"""
Case 1
Input
10:00 19:00
09:00 15:00
10:00 11:00
11:00 22:00
09:00 15:00
Output
1980

Case 2
Input
10:00 19:00
09:00 15:00
10:00 11:00
11:00 22:00
09:00 15:00
Output
2785

Case 3
Input
09:17 19:24
10:11 18:45
09:34 18:27
10:47 15:33
08:47 18:32
Output
2525
"""