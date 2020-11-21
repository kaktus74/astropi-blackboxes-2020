files = []
path = '/home/kaktus74/astropi2021/2020-11-14/test.csv'
n = 1000

for i in range(0,n):
    #f = open(path,mode='r')
    with open(path,mode='r') as f:
        files.append(f)
        line = f.readline()
        line2 = f.readline()
        print(line)
        print(line2)
        if i == n - 1:
            x = 1 / 0        

input('Enter aby zakończyć')

# line = files[0].readline() 

 

print(line)

