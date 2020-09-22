"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solutionAttempt1(N, A): #o(N*M) complexity, too slow 
    # write your code in Python 3.6
    counters = [0]*N
    k = 0
    maxN = N+1
    for X in A:
        if X==maxN:
            n = max(counters)
            counters = [n]*N
        else:
           counters[X-1]+=1
    
    return counters

def solutionAttempt2(N, A): #Detected time complexity: O(N + M), much faster, only failed time for all max operations in a large array

  # write your code in Python 3.6
    counters = [0]*N
    k = 0
    maxN = N+1
    currentMax = 0
    for X in A:
        if X==maxN:
            counters = [currentMax]*N
        else:
           counters[X-1]+=1
           if (counters[X-1]>currentMax):
               currentMax = counters[X-1]
    
    return counters
    
def solution(N, A): #100% success
   
   # write your code in Python 3.6
    counters = [0]*N
    k = 0
    maxN = N+1
    currentMax = 0
    prevMax = 0
    for X in A:
        if X==maxN:
            prevMax = currentMax
        else:
           counters[X-1] = max(counters[X-1]+1, prevMax+1)
           if (counters[X-1]>currentMax):
               currentMax = counters[X-1]
    index = 0
    for y in counters:
        if y < prevMax:
            counters[index] = prevMax
        index+=1
        
    return counters