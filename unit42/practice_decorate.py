
# 데코레이터 type_check 작성
# type_check는 함수의 매개변수가 지정된 자료형(클래스)이면 함수를 정상적으로 호출 # 자료형 검사 isinstance() 함수 사용
# 지정된 자료형과 다르면 RuntimeError 예외를 발생 # raise RuntimeError 시키면서, '자료형이 다릅니다' 에러 메시지를 출력
# type_check에 지정된 첫 번째 int는 호출할 함수에서 첫 번째 매개변수 자료형을 뜻함
# 두 번째 int는 호출할 함수에서 두 번째 매개변수의 자료형을 뜻함


def type_check(x, y): # 데코레이터가 사용할 매개변수 지정
    def real_decorator(func): # 실제 데코레이터 역할을 하는 데코레이터
        def wrapper(a, b): # add 함수의 매개변수가 2개이기 때문에, wrapper에도 2개의 매개변수 지정
            if isinstance(a, x) and isinstance(b, y): # isisntance로 호출할 함수의 매개변수가 자료형(클래스)의 인스턴스인지 판별
                return func(a, b) # 
            else:
                raise RuntimeError('자료형이 다릅니다.')
        return wrapper
    return real_decorator


@type_check(str, str) # 매개변수가 있는 데코레이터
def add(a, b):
    return a + b

print(add('hello', 'world'))
print(add(10, 20))
