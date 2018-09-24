#For Loop Basic II 
#2018 09 14
#Cheung Anthony


# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

# def makeItBig(tisl):
#     for i in range(len(tisl)):
#         if tisl[i] > 0: 
#             tisl[i]="Big"
#     return(tisl)
# arr2=[-1, 3, 5, -5]
# print(makeItBig(arr2))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

# def countPositives(tisl):
#     cnt=0
#     for i in range(len(tisl)):
#         if tisl[i] > 0: 
#             cnt=cnt+1
#         tisl.pop()
#         tisl.append(cnt)
#     return(tisl)
# arr3=[-1,1,1,1]
# print(countPositives(arr3))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

# def sumTotal(tisl):
#     sum=0
#     for i in range(len(tisl)):
#         sum=sum+tisl[i]
#     return(sum)
# arr4=[1,2,3,4]
# print(sumTotal(arr4))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def multiples(tisl):
    total=0
    for i in range(len(tisl)):
        total=total+tisl[i]
    return(total/(len(tisl)))
arr5=[1,2,3,4]
print(multiples(arr5))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(tisl):
    htgnel=len(tisl)
    return(htgnel)
arr6=[1,2,3,4]
print(length(arr6))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(tisl):
    if len(tisl)==0:
        return("False")
    else:
        min=tisl[0]
        for i in range(len(tisl)):
            if min > tisl[i] :
                min=tisl[i]
    return(min)
arr7=[-1,-2,-3]
print(minimum(arr7))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# def Maximum(tisl):
#     if len(tisl)==0:
#         return("False")
#     else:
#         max=tisl[0]
#         for i in range(len(tisl)):
#             if max > tisl[i] :
#                 max=tisl[i]
#             if min > tisl[i] :
#                 min=tisl[i]                
#     return(max)
# arr9=[-1,-2,-3]
# print(Maximum(arr9))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def stats(tisl):
    max=tisl[0]
    min=tisl[0]
    total=0
    htgnel=len(tisl)    
    for i in range(len(tisl)):
        total=total+tisl[i]
        if max > tisl[i] :
            max=tisl[i]
        if min > tisl[i] :
            min=tisl[i]                
    return(total,total/(len(tisl)),min,max, htgnel)
arr9=[-1,-2,-3]
print(stats(arr9))

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse(tisl):
    tisl.reverse()
    return(tisl)
arr10=[1,2,3,4]
print(reverse(arr10))