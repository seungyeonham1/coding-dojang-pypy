


# 예외 처리 사용하기
# 예외: 코드를 실행한 중에 발생한 에러를 뜻함
# 에외 처리는 에러가 발생하더라도 스크립트의 실행을 중단시키지 않고 계속 실행하고자 할 때 사용함

# try:
    # 실행할 코드
# except:
    # 예외가 발생했을 때 처리하는 코드


# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except:
#     print('예외가 발생했습니다.')


# 특정 예외만 처리하기

# try:
    # 실행할 코드
# except:
    # 예외가 발생했을 때 처리하는 코드

# y = [10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
#     print('잘못된 인덱스입니다.')


# 예외의 에러 메시지 받아오기
# try:
    # 실행할 코드
# except 예외 as 변수:
    # 예외가 발생했을 때 처리하는 코드


# 예외가 여러 개 발생하더라도 먼저 발생한 예외의 처리 코드만 실행됨
# 혹은 예외중에서 높은 계층의 예외부터 처리됨. ex) 기반 클래스 > 파생 클래스 순

# 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
# except Exception as e:
    # print('예외가 발생했씁니다.', e)


# else, finally
# 예외가 발생하지 않았을 때 코드를 실행하는 else
# else는 except 바로 다음에 와야하며 except를 생략할 수 없음

# try:
    # 실행할 코드
# except:
    # 예외가 발생했을 때 처리하는 코드
# else:
    # 예외가 발생하지 않을 때 실행할 코드 


# 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally
# finally는 except와 else를 생략할 수 있음

# try:
    # 실행할 코드
# except:
    # 예외가 발생했을 때 처리하는 코드
# else:
    # 예외가 발생하지 않았을 때 실행할 코드
# finally:
    # 예외 발생 여부와 상관없이 항상 실행할 코드


# try 안에서 만든 변수는 바깥에서 사용할 수 있는가?
# try는 함수가 아니기 때문에 스택 프레임을 만들지 않음. 그렇기 때문에 사용할 수 있음.(except, else, finally에서도 가능)


# 예외 발생시키기
# rasie 예외('에러메시지')

# try:
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)
# except Exception as e:
#     print('예외가 발생했습니다.', e)


# 현재 예외를 다시 발생시키기
# raise

# def three_multiple():
#     try:

#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0 : # 3의 배수가 아니면 
#             raise Exception('3의 배수가 아닙니다.') # 예외를 발생시킴
#         print(x)
#     except Exception as e: # 함수 안에서 예외를 처리함
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김

# try:
#     three_multiple()

# except Exception as e: # 하위 코드 블록에서 예외가 발생해도 실행함
#     print('스크립트 파일에서 예외가 발생했습니다.', e)


# 예외 발생시키기
# raise에 다른 예외를 지정하고 에러 메시지를 넣을 수도 있음
# raise 예외('에러메시지')

# if x % 3 != 0 : # 3의 배수가 아니면 
#             raise Exception('3의 배수가 아닙니다.') # 예외를 발생시킴
#         print(x)
#     except Exception as e: # 함수 안에서 예외를 처리함
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')


# assert로 예외 발생시키기
# 지정된 조건식이 거짓일 때 AssertError 예외를 발생시키며 조건식이 참이면 그냥 넘어감
# assert는 디버깅 모드에서만 실행됨.

# assert 조건식
# assert 조건식, 에러메시지

# x = int(input('3의 배수를 입력하세요: '))
# assert x % 3 == 0, '3의 배수가 아닙니다.'
# print(x)



# 예외 만들기
# 프로그래머가 직접 만든 예외를 사용자 예외라 부름

# class 예외이름(Exception):
    # def __init__(self):
        #super().__init__('에러메시지')


# class NotThreeMultipleError(Exception): # Excpetion을 상속받아 새로운 예외를 만듦
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.')


# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0: # x가 3의 배수가 아니면
#             raise NotThreeMultipleError # NotThreeMultiple 예외를 발생시킴
#         print(x)
#     except Exception as e:
#         print('예외가 발생했습니다.', e)

# three_multiple()

