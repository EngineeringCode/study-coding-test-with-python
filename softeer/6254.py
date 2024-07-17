"""

연습문제 > 근무시간
문제 주소: https://softeer.ai/practice/6254
해설 주소:

프로그램 작성자: 공학코드(engineeringcode93@gmail.com)

"""

import sys

work_sum = 0

for i in range(5):

    one_line = sys.stdin.readline()

    lh = int(input[0:2])
    lm = int(input[3:5])
    rh = int(input[6:8])
    rm = int(input[9:11])

    if rm - lm < 0:
        rh = rh - 1
        rm = rm + 60

    rm = rm - lm + (rh - lh) * 60

    work_sum = work_sum + rm

print(work_sum)
