
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

#print((a+b+c+d)//4)

a,b,c,d = map(int, input().split()) #a,b,c,d를 map으로 언패킹해서 값을 받음 / 받는 값은 int형

print((a+b+c+d)//4) # 점수로 출력되게끔 연산자 사용, a,b,c,d의 더한 값을 평균으로 구한다
