1. 문자열 바꾸기
'a:b:c:d' -> 'a#b#c#d' 바꾸기

a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)

2. + 와 extend
a = [1,2,3]
a = a + [4,5]
+ 기호를 사용하여 더한 경우 a의 주소값이 변함

a = [1,2,3]
a.extend([4,5])
extend를 사용하여 더한 경우 주소 값이 변하지 않고 그대로 유지

3. 리스트 총합 구하기
A = [20,55,67,82,45,33,90,87,100,25]

result = 0;
while A: #리스트에 값이 있는 동안
  mark = A.pop() #A리스트의 가장 마지막 항목을 하나씩 뽑아냄
  if mark >= 50: #50점 이상의 점수만 더함
      result += mark

print(result)
