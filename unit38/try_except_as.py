

y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
# except ZeroDivisionError as e: # as 뒤에 변수를 지정하면 에러를 받아옴
#     print('숫자를 0으로 나눌 수 없습니다.', e) # e에 저장된 에러 메시지 출력
# except IndexError as e:
#     print('잘못된 인덱스 입니다.', e)



# 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
except Exception as e:
    print('예외가 발생했습니다.', e)