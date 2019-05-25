# Enter your code here. Read input from STDIN. Print output to STDOUT

def FirstDefectAtX(prob,x):
    res = ((1-prob)**(x-1)) * prob
    #p = prob
    #q = 1-p
    #prob of defect at x = q^(x-1) * p
    return res

if __name__=='__main__':
    s = input()
    pn = int(s.split(' ')[0])
    pd = int(s.split(' ')[1])

    p = pn / pd
    q = 1- p
    n = int(input())

    #prob that first defect is found during first five trails defect0 + defect 1 + ...+\
    #defect5
    x = 1
    ans = 0
    while x <= n:
        ans += FirstDefectAtX(p,x)
        x += 1
    print('%0.3f' %ans)