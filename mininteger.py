"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solutionTimeconsuming(A):
    # write your code in Python 3.6
    
    mini = min(A)
    maxi = max(A)
   
    toReturn = 0
    if mini >1:
        return mini-1
    else: 
        if mini<0:
            mini = 1
        if maxi<0:
            return 1
        rangi = range(mini,maxi+1)
        for x in rangi:
            if x in A:
                continue
            else:
                return x
        return maxi+1
        

def solutionAttempt2(A): #77%, some wrong answers
    # write your code in Python 3.6
    
    maxi = max(A)+1
    if maxi<1:
        return 1
    mini = min(A)
    if mini >1:
        return mini-1
    hasN = [False]*maxi
    hasN[0]=True
    for x in A:
        if x > 0:
            hasN[x]=True
    j = 0
   # print(hasN)
    for y in hasN:
        if y == False:
            break
        j+=1
    return j
            
 
def solution(A): #perfect 100%
    # write your code in Python 3.6
    maxi = max(A)+1
    if maxi<=1:
        return 1
    mini = min(A)
    if mini >1:
        return 1
    hasN = [False]*maxi
    hasN[0]=True
    for x in A:
        if x > 0:
            hasN[x]=True
    j = 0
    for y in hasN:
        if y == False:
            break
        j+=1
    return j
           