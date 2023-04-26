
# 표준 입력으로 문자열이 입력됩니다.  text = input('입력: ')
# 문자열이 회문이면 문자열을 그대로 출력  text != text[::-1]
# 회문이 아니면 '회문이 아닙니다.' 출력  try: except:
# 함수는 palindrome, 예외는 NotPalindromeError def palindrome, except NotPalindromeError





class NotPalindromeError(Exception): # 클래스 NotPalindromeError는 Exception을 기반으로 하는 파생 클래스
    def __init__(self): # 인스턴스 호출 함수
        super().__init__('회문이 아닙니다.') # 기반 클래스의 __init__ 메서드 호출 

def Palindrome(text): # 회문 함수
    if text != text[::-1]: # 만약 회문이 아닌 경우
        raise NotPalindromeError # 예외를 발생시킨다
    print(text) # 회문인 경우, 입력한 문자를 출력

try:
    text = input('문자를 입력하세요: ')
    Palindrome(text) # 회문 함수로 이동하여 회문 판별 시킴
except NotPalindromeError as e:
     print(e)