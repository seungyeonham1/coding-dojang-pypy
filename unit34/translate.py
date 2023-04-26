
# 구글 번역기 
# 구글 번역 대상 언어 코드가 fr인 경우엔 번역 결과를 반환하지 않고 예외를 raise 

# client = 번역 엔진을 의미
# sl = 원본 언어의 국가 코드 
# tl = 어떤 언어로 번역할건지 의미하는 파라미터
# dt = 어떤 번역 알고리즘을 거칠 것인가
# q = 번역을 요청할 원본 문장

# https://translate.googleapis.com/translate_a/single(
#     client=gtx,
#     sl=en,
#     tl=ko,
#     dt=t,
#     q=Hello+World
# )
 



import requests # HTTP 웹 사이트 요청을 위해 requests 모듈 사용

class Google_Translator:

    def __init__(self, source_lang, target_lang): 
        '''인스턴스를 초기화 하는 메서드'''
        self.url = 'https://translate.googleapis.com/translate_a/single' 
        self.source_lang = source_lang # 출발 언어 매개변수를 속성 1에 지정
        self.target_lang = target_lang # 도착 언어 매개변수를 속성 2에 지정

    def translate(self, text):
        '''번역 해주는 메서드'''
        
        params = { # 매개변수에 키워드: 값 형식으로 인수를 저장 (키워드는 문자열 형태여야만 함)
            'client': 'gtx',
            'sl': self.source_lang,
            'tl': self.target_lang,
            'dt': 't',
            'q': text
        }

        response = requests.get(self.url, params=params) # HTTP 요청 메서드를 get 방식으로 url과 매개변수 호출
        result = response.json()[0][0][0] # 요청했던 파싱한 json 데이터 결과를 응답해준다. (json은 딕셔너리에 key-value 형식으로 이루어짐)
        return result # 나온 결과를 반환한다.
     



translator = Google_Translator('ko', 'en') # 번역기 함수를 설정한 값으로 번역한다.
text = input('번역할 문장을 입력하세요:') # source_lang에 설정한 언어로 텍스트를 입력한다.
result = translator.translate(text) # target_lang에 설정한 언어로 입력한 텍스트를 번역한다.
print(result) # 번역된 문장을 출력한다.
