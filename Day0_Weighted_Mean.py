# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
line1 = input()
line2 = input()
xi = [int(x) for x in line1.split(' ')]
wi = [int(x) for x in line2.split(' ')]

wmean = 0
wsum = 0
for i in range(n):
    wmean += xi[i] * wi[i]
    wsum += wi[i]

ans = wmean / wsum

print('%0.1f' %ans)