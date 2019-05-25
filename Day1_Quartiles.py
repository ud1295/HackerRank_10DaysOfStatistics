# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
strq = input()

lis = [int(x) for x in strq.split(' ')]
li = sorted(lis)

# print(li)
def fun(__li):
    leng = len(__li)
    if leng % 2 == 0:
        v1 = (__li[(leng//2) - 1] + __li[leng//2]) / 2
    else:
        v1 = __li[leng//2]
    return v1

q2 = fun(li)
q1 = fun(li[0:n//2])
if n % 2 == 0:
    q3 = fun(li[(n//2):n])
else:
    q3 = fun(li[(n//2 +1) :n])
# print(len(li[(n//2 +1) :n]))
# print(li[(n//2 +1) :n-1])
print(int(q1))
print(int(q2))
print(int(q3))