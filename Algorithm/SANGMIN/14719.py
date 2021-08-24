'''
https://www.acmicpc.net/problem/14719
빗물
[풀이]
1. h, w input은 딱히 사용하지 않음
2. 왼쪽에 있는 높은 블럭을 매번 기억 => left_block
3. rain은 쌓일 가능성이 있는, stagnant_rain은 무조건 쌓이는 빗물
4. 현재를 기준으로 오른쪽 블럭이 자신보다 높으면 빗물이 쌓인다
=> left_block 보다 높거나 같으면 최대로 쌓인다
=> left_block 보다 낮으면 현재 블럭과 right_block의 차이만큼 쌓인다
'''
import sys
input = sys.stdin.readline
input()
blocks = [i for i in map(int, input().strip().split())]
left_block = rain = stagnant_rain = 0
for idx, block in enumerate(blocks):
    left_block = max(block, left_block)
    rain = left_block - block
    if rain > 0:
        right_block = block
        for next_b in blocks[idx+1:]:
            right_block = max(right_block, next_b)
            if right_block >= left_block:
                break
        stagnant_rain += min(left_block, right_block) - block
print(stagnant_rain)
