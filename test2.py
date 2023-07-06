----10. 중복된 숫자

def chkDupNum(s)
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
  리스트 자료형을 사용하여 중복된 값이 있는지 먼저 조사한다.
  중복된 값이 없을 경우 0~9까지의 숫자가 모두 사용되었는지 판단하기 위해 총 개수가 10인지 조사


----11. 모스 부호 해독

dic = {
    '._':'A','-...':'B','-.-.':'C', ... }

def morse(src):
    result = []
    for word ind src.split("  "): #공백 2개로 쪼갬
        for char in word.split(" "): #공백 1개로 쪼갬
            result.append(dic[char]) #dic[char]을 사용하여 값을 찾은걸 result에 추가
        result.append(" ") #바로 위 for문을 빠져나오면 한칸 띄어쓰기
    return "".join(result) #배열의 형태로 되어있는 것을 하나로 합치기


----12. 기초 메타 문자

다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
1. acccb
2. a....b
3. aaab
4. a.cccb
정답 2번.

  
----13. 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성
  
전화번호 패턴은 다음과 같이 작성할 수 있다.
  pat = re.compile("\d{3}[-]\d{4}[-]\d{4}")
이 전화번호 패턴 중 뒤에 숫자 4개를 변경할 것이므로 필요한 앞부분을 다음과 같이 그루핑한다.
  pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")                
컴파일된 객체 pat에 sub 함수를 사용하여 다음과 같이 문자열을 변경한다.
  result = pat.sub("\g<1>-####", s)
