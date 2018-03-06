# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import random

#import pyhook

num = random.randrange(1,1000)
print(num)

running = True
i = 0
#while running:
while i < 5:
    #print(num)
    try:
        input_info = int(input("Please enter a number of your guesses : "))
    except ValueError as error_value:
        print(error_value)
        print (" sorry,Please enter a number of your guesses and do not enter any other characters")

    # if not input_info.isdigit():
    #     print (" sorry,Please enter a number of your guesses and do not enter any other characters")
    else:
        input_info = int(input_info)
        if input_info == num:
            print ('\033[1;94m'+"Wow, you are so great! The answer is right")
            running = False
        elif input_info > num:
            print("Your guess is too big  ")

        elif input_info < num:
            print("Your guess is too small")
    i += 1
    if i >= 5:
        print('game over')