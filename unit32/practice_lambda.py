

# 확장자가 jpg, png인 이미지 파일만 출력되게 만들것
# 람다표현식을 사용, 출력 결과는 리스트 형태
# 확장자 검사는 문자열 메서드 활용할 것

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xlsx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('png') != -1, files)))