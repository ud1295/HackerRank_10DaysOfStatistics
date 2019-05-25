# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

nos = input()
# freq = input()
freq_li = [int(x) for x in input().split(' ')]

li_no = [int(x) for x in nos.split(' ')]

lis = []
cnt = 0
for i in freq_li:
    for z in range(i):
        lis.append(li_no[cnt])
    cnt += 1

#code taken from quartiles problem
li = sorted(lis)

# print(li)
n = len(li)
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
# print(q3)
# print(q1)
print('%0.1f'%(q3 - q1))


