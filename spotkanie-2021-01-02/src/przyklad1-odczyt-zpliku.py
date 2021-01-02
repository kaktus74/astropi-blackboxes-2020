from os.path import dirname

with open(dirname(__file__) + '/../stations.txt') as stations_file:
    #lines = stations_file.readlines()
    #print(len(lines))
    line = stations_file.readline()
    print(line)
