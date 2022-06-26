
# 중첩 루프
# 
# for i in range(5): # 5번 반복, 바깥쪽
#    for j in range(5): # 5번 반복, 안쪽
#        print('j:', j, sep='', end=' ') # j값 출력

#    print('i:', i, '\\n', sep='') #i값 출력

    # j:0 j:1 j:2 j:3 j:4 i:0\n
    # j:0 j:1 j:2 j:3 j:4 i:1\n



#for i in range(5):
#    for j in range(5):
#        print('*', end='')
#    print() # j문의 5번 반복이 끝나면 i값을 출력  j가 5번일 때, i는 1번 

    #j: *****
    #j: *****
    #j: *****
    #j: *****
    #j: *****


#for i in range(3):
#    for j in range(7):
#        print('*', end='')
#    print()

#j: *******
#j: *******
#j: *******



# for i in range(5): # 0 1 2 3 4
#    for j in range(5): # 0 1 2 3 4
#        if j <= i: #i가 j보다 크거나 같으면
#            print('*', end='') # 별을 출력함
#    print()


# j: *
# j: **
# j: ***


#for i in range(5): # 0 1 2 3 4 
#    for j in range(5): # 0 1 2 3 4
#        if j == i: # j가 i값과 동일하다면
#            print('*', end='') # 별을 출력
#    print() # i값 출력

# *
# *
# *
# *
# *
# *


# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# *
#  *
#   *