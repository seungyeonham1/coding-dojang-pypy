

path = 'C:\\Users\\dojang\\Appdata\\Local\\Programs\\Python\\Python36-32\\python.exe'

# a = path.split('\\') # '\\' 기준으로 문자열을 분리하여 리스트로 만듬
# filename = a[-1] # 리스트에서 마지막 요소 인덱스를 호출함
# print(filename)

filename = path[path.rfind('\\') + 1:]  # path의 오른쪽 문자열 '\\'의 다음 문자열을 전부 출력한다.
print(filename)

