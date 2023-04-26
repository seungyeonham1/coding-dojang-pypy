
def is_palindrome(word):

    if len(word) < 2: # 문자열 길이 절반 기준으로 해야하기 때문에 
        return True
    if word[0] != word[-1]: # 첫자리와 마지막자리 문자가 같지 않으면
        return False
    return is_palindrome(word[1:-1])


print(is_palindrome('hello'))
print(is_palindrome('level'))