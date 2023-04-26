

# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력
# 입력값 : 51900;83000;158000;367500;250000;59200;128500;1304000
# 각 가격은 세미클론(;)으로 구분
# 가격은 높은 가격 순으로 출력
# 가격의 길이 = 9, 오른쪽 정렬, 천단위, 콤마(,) 넣을 것


# 높은 가격 정렬 :  price.sort(reverse=true) 내림차순
# '{인덱스:>9}'.format(price)
# 천단위 format(price, ',') 
# 세미클론 기준으로 정렬

input_price = list(map(int, input().split(';'))) # 입력값을 리스트

input_price.sort(reverse = True)

for i in input_price:
    
    #print('{:>9,}'.format(i))
    print(format(i, ',').rjust(9)) # 메서드 체이닝으로 표현

