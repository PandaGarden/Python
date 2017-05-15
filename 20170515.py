#-*- coding: utf-8 -*-
#Use index to get designated elements from the list
# L = [
#     ['Apple','Google','Microsoft'],
#     ['Java','Python','Ruby','PHP'],
#     ['Adam','Bart','Lisa']
# ]
# #Print Apple
# print (L[0][0])
# #print Python
# print (L[1][1])
# #print List
# print (L[2][2])

#-----------------------------------
# 2. Tom is 1.75 height and 80.5 kg weight.  please print result according to following BMI formula
# Height / Weight squared
# < 18.5     underweight
# 18.5 - 25 Normal
# 25-28      overweight
# 28-32      obese
# >32         Severely Obese
#-----------------------------------
# height = input ('How tall you are?')
# height = float(height)
# weight = input ('What is your weight?')
# weight = float(weight)
# bmi = 10000*weight/(height*height)
# print ('Your BMI is ', bmi)
# if bmi > 32:
#     print ('Severely Obese')
# elif bmi <= 32 and bmi > 28:
#     print ('obese')
# elif bmi <= 28 and bmi > 25:
#     print ('overweight')
# elif bmi <= 25 and bmi > 18.5:
#     print ('Normal')
# else:
#     print ('underweight')

#-----------------------------------
#use for ... in
#-----------------------------------
# sum = 0
# for x in range (101):
#     sum =  sum + x
# print (sum)

#-----------------------------------
#use while loop
#-----------------------------------
# sum = 0
# n = 99
# while n > 0:
#     sum = sum+n
#     n = n -2
# print (sum)

#-----------------------------------
#3. Print "Hello, xxx!" at each name in the list
#L = ['Bart', 'Lisa', 'Adam']
#-----------------------------------
# L = ['Bart', 'Lisa', 'Adam']
# for l in L:
#     print ('Hello,',l)


# ----------break---------------
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# ----------continue---------------
# n = 0
# while n < 10:
#     n = n + 1
#     if n%2 == 0 : # if n is even number, execute continue
#         continue # jump into next loop.
#     print (n)

#-----------------------------------
#use import function
#-----------------------------------
from abstest import my_abs
