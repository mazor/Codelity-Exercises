"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

def solutionAttempt1(A, B, K): #got 87%, O(N) Got wrong answer for A = 11, B = 345, K = 17 (got 19 expected 20)
    # write your code in Python 3.6
    numDiv = 0
    
    if A%K==0 or B % K == 0:
        numDiv+=1
        
    diff = B-A
    
    numDiv += int(diff/K)
    
    return numDiv


def solutionAttempt2(A, B, K): #still 87%, different wrong answer A = 101, B = 123M+, K = 10K got 12346 expected 12345

    # write your code in Python 3.6
    numDiv = 0
    
    if A%K==0 or B % K == 0:
        numDiv+=1
        
    diff = B-A
    if (numDiv == 0):
        numDiv = round(diff/K)
    else:
        numDiv = int(diff/K)+1
    
    return numDiv

def solution(A, B, K): #100% :)
    numDiv = 0
    
    if A%K==0:
        numDiv+=1
        
    diff = B-A
    
    numDiv += int(B/K) - int(A/K)
    
    return numDiv