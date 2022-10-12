# # spam = 42 # global variable
#
# def spam():
#     eggs = 99 # local variable
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0
#
# spam()
# #
# # # print('some code here. ')
# # # print('some code here. ')

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)