from calendar import prweek
from curses import halfdelay
from hashlib import algorithms_available
import numbers
from re import I
from signal import pthread_kill
from turtle import position
from importlib_metadata import version


MIT - 파이썬을 이용한 알고리즘 이해 강의

알고리즘

https://courses.csail.mit.edu/6.006

Course Overview

"큰 입력을 받는 문제를 처리하기 위한 효율적인 방법"

큰 입력 예시 human genes, USA highway system

Efficient procedures for solving large scale problems
Scalability(확장성)
Clssic data structures & classical algorithms
real implementations in Python

Content
8 modiles:
    1) Algorithmic thinking: peak finding
    2) Sorting & trees : Event simulation
    3) Hashing: genome comparison
    4) Numerics: RSA encryption
    5) Graphs: Rubik's cube
    6) Shortest paths: Caltech -> MIT
    7) Dynamic programming: Image comparison
    8) Advanced topics


Peak finding

One-dimensional version

a b c d e f g h i
1 2 3 4 5 6 7 8 9

a-i are numbers

Position 2 is a peek
if and only if b>=a and b>=c

Position 9 is a peek
if i >= h

problem : find a peek if it exists

straightforward algorithm
start from left

1 2 ... n/2   n-1 n 

if it is right in the middle 

worst case complexity: theta(n)

##################################
이 때 복잡도를 낮추려면 절반으로 잘라가면서 할 수 있겠지
==> binary search algo
recursive algorithm

1 2   n/2-1 n/2 n/2+1   n-1 n Divide & Conquer

1) look at n/2 position

if a[n/2] < a[n/2 -1] then only look at left half
1   n/2-1 to look for a peek

else if a[n/2] < a[n/2+1] then only look at right half 
n/2+1 ...n 

else n/2 position is a peek 

##################################
걸리는 시간을 계산하자 => 복잡도

 # "work" algorithm does on input of size n
T(n) = T(n/2) + theta(1) # theta(1) 1차원 에서 양쪽 비교 2번 => 값 : 2(상수)

base case : T(1) = theta(1)
T(n) = theta(1) + .... + theta(1) = theta(log2n) log 2 의 n

theta(n) theta(log2n)



#####################################

2D

2D version

(n x m) matrix 
   c 
b  a  d 
   e

greedy ascent algo : 
theta(nm) complexity 
theta(n**2) if m=n

attempt # 1
binary search 로 풀기

prick middle column j = m/2
find a 1D-peek at (i,j)
use (i,j) as a start to find a 1D-peak on row i 

theta(log2m)

이거 incorrect !!! 

Problem : 2D peak may not exist on row i 

attempt # 2

prick middle column j = m/2
find global max on column j at(i,j)
compare (i,j-1),(i,j),(i,j+1)
pick left cols if (i,j-1) > (i,j) similarly for right

if (i,j) >= (i,j-1),(i,j+1) => (i,j) is 2D peak

solve the new problem with half the num of cols

when you have a single col, find the global max <- done

T(n,m) = T(n,m/2) + theta(n)










































