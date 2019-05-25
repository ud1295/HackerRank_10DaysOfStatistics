# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact (n - 1)

def ncr(n,r):
    return fact(n)/(fact(r) * fact(n-r))


def probRways(probablility,N, R):
    p = probablility
    q = 1 - p
    prob = ncr(N,R) * (p ** R) * (q ** (N - R))
    return prob



if __name__ == '__main__':
    s = input()
    p = float(s.split(' ')[0])
    p /= 100
    n = float(s.split(' ')[1])
    ans1 = probRways(p,n,0) + probRways(p,n,1) + probRways(p,n,2)
    ans2 = 0
    for i in range(2,11):
        ans2 += probRways(p,n,i)
    print('%0.3f' %(ans1))
    print('%0.3f' %(ans2))