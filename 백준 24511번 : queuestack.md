### 문제
https://www.acmicpc.net/problem/24511

### 내가 작성한 코드

```
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
stack = deque()

for i in range(n):
    if a[i] == 0: //큐일때만 삽입해줌
        stack.append(b[i])
else:
    if len(stack) == 0: //모두 스택일땐 
        print(*c)       //삽입하는거 그대로 출력
        sys.exit()
        
for i in range(m):
    stack.appendleft(c[i])
    print(stack.pop(), end=' ')
