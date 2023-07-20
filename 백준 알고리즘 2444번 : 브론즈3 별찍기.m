<h3>입력</h3>
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

<h3>출력</h3>
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

<h3>예제 입력 1</h3>
5
<h3>예제 출력 1</h3>

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

<h3>내가 작성한 코드</h3>

```
N = int(input())
for i in range(1,N+1):
    for j in range(N-i):
        print(" ", end='')
    for j in range(2*i-1):
        print("*", end='')
    print('')
for i in range(1,N):
    for j in range(i):
        print(" ", end='')
    for j in range((2*N-1)-2*i):
        print("*", end='')
    print('')
```
