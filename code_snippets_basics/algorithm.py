#%%
# 00_Special

# Unpacking
"""
a, b = map(int, input().split())
"""
_list = [1, 2, 3, 4, 5]
first_index, *rest, _last_index = _list
print(rest)
# %%
_list = [1, 2, 3, 4, 5]
for num in _list:
    print(num, end =  ' ')

_list = [1, 2, 3, 4, 5]
print(*_list)


# Packing
a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)
# %%
# List Comprehension
_list = [i for i in range(10)]

# %%
## 백준 온라인 저지 1920번 "수 찾기" (http://boj.kr/1920)
import sys
input = sys.stdin.readline

_ = input()
_set = set(map(int, input().split()))
q = input()
_list = list(map(int, input().split()))

print(*[1 if dt in _set else 0 for dt in _list], sep = '\n')


# %%
square = [[x ** 2 for x in range(3)] for _ in range(3)]
print(square)
# %%
_list = [i for i in range(10)]
_list = [2 * i for i in range(10)]
tmp = [random.randragne(1, 200) for i in range(100)]
