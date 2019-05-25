# import time
# stime = time.time()
# li = [3,3,2,2,1]
n = int(input())
values = input()
li = [int(a) for a in values.split(' ')]
details = []
cnt = 1
for i in range(len(li)):
    try: 
        if li[i] == li[i+1]:
            cnt += 1
    except IndexError:
        if li[-1] == li[-2]:
            details.append((li[-1],cnt))
        else:
            details.append((li[-1], 1))
        print('{} {}'.format(li[i], cnt))
    try:    
        if li[i] != li[i+1]:
            details.append((li[i],cnt))
            cnt = 1
    except IndexError:
        pass
print(details)

# etime = time.time()
# print(etime - stime)