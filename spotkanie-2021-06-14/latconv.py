
def to_coord(napis):
    if_negative = False
    tupel = napis.split(':')
    degree = float (tupel[0])
    if degree < 0:
        degree = degree *(-1)
        if_negative = True
    segtvtrfvg = (degree + float(tupel[1])/60 + float(tupel[2])/3600)
    if if_negative == True:
        segtvtrfvg = segtvtrfvg * (-1)
    return segtvtrfvg



#-106:21:36.5 -> -106.360388

#print(to_coord("-106:21:36.5"))


#float( int(data[2].split(':')[0] + (int(data[2].split(':')[2] /60) )

        

