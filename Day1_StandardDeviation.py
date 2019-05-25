# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lis = input()
li = [int(x) for x in lis.split(" ")]
mean = 0
for i in range(n):
    mean += li[i]
mean /= n
var = 0
for i in range(n):
    var += (mean - li[i]) ** 2
var /= n
import math
var = math.sqrt(var)
print('%0.1f' %(var))