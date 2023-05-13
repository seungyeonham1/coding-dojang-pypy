

# 표준 입력으로 HTML 태그 2개가 입력  # input().split()
# 소스 코드에서 반환값을 HTML태그로 감싸는 데코레이터를 만드세요.
# HTML 태그는 웹 페이지에 사용하는 문법, <span> 문자열 </span>, <p> 문자열 </p> 처럼 <태그 이름>으로 시작하며 </태그 이름>으로 끝남


# def html_tag(tag_name):
#   def real_decorator(func):
#     def wrapper():
#       return '<{0}>{1}</{0}>'.format(tag_name,func())
#     return wrapper
#   return real_decorator


class html_tag:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(self.x, func())
        return wrapper

a, b = input().split()

@html_tag(a) # p 
@html_tag(b) # span
def hello(): # hello 함수를 
    return 'Hello, world!'

print(hello())