import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print('{} {}'.format(min(nums), max(nums)))