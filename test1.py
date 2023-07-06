-----1. 문자열 바꾸기
'a:b:c:d' -> 'a#b#c#d' 바꾸기

a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)

------2. + 와 extend
a = [1,2,3]
a = a + [4,5]
+ 기호를 사용하여 더한 경우 a의 주소값이 변함

a = [1,2,3]
a.extend([4,5])
extend를 사용하여 더한 경우 주소 값이 변하지 않고 그대로 유지

-----3. 리스트 총합 구하기
A = [20,55,67,82,45,33,90,87,100,25]

result = 0;
while A: #리스트에 값이 있는 동안
  mark = A.pop() #A리스트의 가장 마지막 항목을 하나씩 뽑아냄
  if mark >= 50: #50점 이상의 점수만 더함
      result += mark

print(result)

-----4. 피보나치 함수
def fib(n):
    if n == 0 : return 0 # n이 0일때는 0을 반환
    if n == 1 : return 1 # n이 1일때는 1을 반환
    return fib(n-2) + fib(n-1) # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(10):
    print(fib(i)) # 0부터 9까지의 피보나치 수열의 결괏값을 출력

-----5. 숫자의 총합 구하기
user_input = input("숫자를 입력하세요: ")
numbers = user_input.split(",")
total = 0
for n in numbers:
    total += int(n) # 입력은 문자열이므로 숫자로 변환해야 한다.
print(total)

-----6. 한 줄 구구단
user_input = input("구구단을 출력할 숫자를 입력하세요(2~9):")
dan = int(user_input)
for i in range(1,10):
    print(dan*i, end= ' ') # 한 줄로 입력하기 위해 줄 바꿈 문자 대신 공백 문자를 마지막에 출력한다.

----7. 평균 값 구하기
f = open("sample.txt")
lines = f.readlines() #sample.txt를 줄 단위로 모두 읽는다.
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average)) #평균 값 결과를 result.txt 파일에 쓴다. 숫자 값은 바로 쓸 수 없으므로 str함수를 사용하여 문자열로 변경한 후 쓴다.
f.close()

------8. 사칙연산 계산기
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def add(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.add()
        return total / len(self.numberList)

cal1 = Calculator([1,2,3,4,5])
print(cal1.add())
print(cal1.avg())

----9. DashInsert 함수
data = "4546793"
numbers = list(map(int, data)) #숫자 문자열을 숫자 리스트로 변경
result = []
for i, num in enumerate(numbers):
  result.append(str(num))
  if i < len(numbers)-1: #다음 수가 있다면
    is_odd = num % 2 == 1 #현재 수가 홀수
    is_next_odd = numbers[i+1] % 2 == 1 #다음 수가 홀수
    if is_odd and is_next_odd: #연속 홀수
        result.append("-")
    elif not is_odd and not is_next_odd: #연속 짝수
        result.append("*")

print("",join(result))

-----10. 문자열 압축하기
먼저 입력 문자열의 문자를 확인하여 동일한 문자가 들어올 경우 해당 문자의 숫자 값을 증가,
만약 다른 문자가 들어올 경우 해당 문자의 숫자 값을 1로 초기화

def compress_string(s):
  _c = ""
  cnt = 0
  result = ""
  for c in s:
      if c != _c: #다른 문자이면
          _c = c
          if cnt: result += str(cnt) #cnt가 true이면
          result += c
          cnt = 1 
      else:
        cnt += 1 
  if cnt: result += str(cnt)
  return result
print(compress_string("aaabbcccccca")) #a3b2c6a1 출력

----11. 중복 숫자 15



