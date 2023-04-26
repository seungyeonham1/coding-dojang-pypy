
# 파일을 한 줄씩 읽은 뒤 내용을 함수 바깥에 전달하는 제너레이터를 작성하세요.
# 파일의 내용을 출력할 때 파일에서 읽은 \n은 출력되지 않아야 함.


def file_read():
    with open('wordss.txt') as file:
        while 1:
            line = file.readline()
            if line == '': # 내용이 빈 문자열이면
               break  # 반복을 끝냄
            yield line.strip('\n')  # 파일에서 읽어온 문자열에서 \n를 삭제하여 바깥으로 전달

for i in file_read():
    print(i)