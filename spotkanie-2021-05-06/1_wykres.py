from csv import reader

with open('oceny.csv','r') as f:
    data = list(reader(f))

    only_data = data[1:]
    print(data)
    #print(only_data)
    oceny = [wiersz[1] for wiersz in data[1:]]

    print(oceny)
    #for row in reader(f):
        #print(row)
    #it = reader(f)
    #row = next(it)
    #print(row)
    
    #row = next(it)
    #print(row[0])
    #print(row[1])

    
#only_data = data[1:]

#osoby = [ row[0] for row in only_data]
#oceny = [ row[1] for row in only_data]


#print(osoby)
#print(oceny)

#print(type(data))


#import matplotlib 


#from matplotlib import pyplot

#pyplot.plot(osoby,oceny)
#pyplot.xlabel('Osoby')
#pyplot.ylabel('Ocena')
#pyplot.title('Oceny')

#pyplot.show()
