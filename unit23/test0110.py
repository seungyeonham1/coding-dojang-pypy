# 원본 시트
sheet = [
    ['id','location','type1','type2'],
    ['f-001', 'kr', 'fruits', 'apple'],
    ['f-002', 'en', 'fruits', 'orange'],
    ['m-001', 'au', 'meat', 'beef'],
    ['m-002', 'jp', 'meat', 'beef'],
    ['m-003', 'kr', 'meat', 'pork']
    ]

# 00 01 02 03  = 0
# 10 11 12 13  = 1
# 20 21 22 23  = 2 
# 30 31 32 33  = 3 
# 40 41 42 43  = 4 
# 50 51 52 53  = 5 

#print(sheet[1]) # f-001, kr, fruits, apple
#print(sheet[5][0]) # m-002
#print(len(sheet)) # 6 세로
#print(len(sheet[0])) # 4  가로
#print(sheet[0:6])
#print(sheet)
#print(sheet[0][1])

#category = sheet[0]
#print(category)

# i 인덱스 2번 요소가 meat인 경우 
# for i in sheet:
#     if i[2] == 'meat':
#         print(i)

user_input = input('컬럼 값을 입력 : ')

new_sheet = []

header = sheet[0]
target_col = header.index('type1') 
extract_id = header.index('id')
extract_location = header.index('location')
extract_type2 = header.index('type2')

for outer_index, outer_value in enumerate(sheet):
    if outer_index == 0 :
        continue
    else :
        if user_input == outer_value[target_col]: # 입력값이 meat인 경우
            row = [
                #outer_value는 m-001, au, beef ,meat // row는 outer_value에서 요소를 inner_value에 하나씩 뽑아서 리스트로 스택하고 그것을 row에 저장
                inner_value for inner_index, inner_value in enumerate(outer_value)
                # 다만 inner_index가 0, 1, 2 경우에만 저장한다
                    if inner_index in [extract_id, extract_location, extract_type2] 
                    ]
            new_sheet.append(row) # 리스트가 저장된 row를 new_sheet에 추가해준다.

for i in new_sheet:
    print(header[3] + ': ' + user_input)
    #print(f'{header[2]}: {user_input}')

    print(i)
    print()



# for i in range(len(sheet)): # 0 1 2 3 4 5 (6)
#     for j in range(len(sheet[i])): # 0 1 2 3 (4)
#         if sheet[i][j] == user_input: # 인덱스 요소가 입력한 값과 동일하다면
            
#             # 입력한 값이 들어간 리스트를 new_sheet 리스트에 가져온다.
#             new_sheet.append([])
        
#         for index, value in enumerate(new_sheet):

#             index

           
        # 입력 값인 인덱스 요소를 제거 한 뒤

        # 나머지는 new_sheet에 다시 저장 

        # 그리고 출력
        


            
           
            
            
            # 인덱스 제거 
     
            
            
            #print(sheet[i])


# # 유저 input. type1 컬럼의 값을 입력 받는다.


# #user_input = input()

# # 원본 시트에서 조건에 맞는 값들을 옮겨놓을 빈 리스트.
# #new_sheet = []



# for, if 등을 사용하여 user_input과 type1 column의 값이 같은 row만 new_sheet에 스택해야 한다.
# 단, type1 컬럼에 해당하는 값은 new_sheet에 포함되지 않아야 한다.
# 가져오는 예시 : ['m-002', 'jp', 'beef']



# 자료가 스택된 new_sheet에서 값을 출력하는 코드. 아래와 같은 규칙으로 출력되어야 한다.
# type1: (유저입력)
# [id 컬럼값, location 컬럼값, type2 컬럼값]


# for i in new_sheet:
    

#     print(i)
#     print()