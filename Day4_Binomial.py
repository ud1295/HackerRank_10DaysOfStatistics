# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()
B = float(s.split(' ')[0])
G = float(s.split(' ')[1])

p = B/(B+G)
q = 1 - p 

ans3 = 20* (p * p * p) * (q * q * q)
ans4 = 15 * (p * p * p * p) * (q * q)
ans5 = 6 * (p ** 5) * q
ans6 = p ** 6
print( '%0.3f' %(ans3 + ans4 + ans5 + ans6))
