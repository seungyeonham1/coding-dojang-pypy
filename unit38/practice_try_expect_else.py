

# maria.txt 파일이 있으면 파일 내용을 읽어서 출력, 없으면 '파일이 없습니다' 를 출력
# 파일이 없을 때 발생하는 예외는 FileNoFoundError

try:
    file = open('maria.txt', 'r', encoding = 'UTF-8')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    print(s)
    file.close()