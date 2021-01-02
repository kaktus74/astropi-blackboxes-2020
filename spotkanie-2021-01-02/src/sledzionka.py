import reverse_geocoder as rev
from os.path import dirname
from ephem import readtle, degree
from datetime import datetime, timezone

def safe_get(dic, key, default='-'):
    return dic[key] if key in dic and len(dic[key]) > 0 else default
        

def szukaj ():
    with open(dirname(__file__) + '/../stations.txt') as st:
        dic = {}
        lines = st.readlines()
        i = 0
        while i < len(lines)/3:
            dic[lines[i].rstrip()] = (lines[i+1].rstrip(), lines[i+2].rstrip())
            i+=3
    for kot in dic.keys():
        print(kot)
    name = input()
    iss = readtle(name, dic[name][0], dic[name][1])
    now_utc = datetime.now(timezone.utc)
    iss.compute(now_utc)
    were_at = rev.search ((iss.sublat / degree, iss.sublong / degree), mode=1)

    
    name = safe_get(were_at[0], 'name','Miejsce bez nazwy')
    admin1 = safe_get(were_at[0], 'admin1','Nie znam prowincji')
    admin2 = safe_get(were_at[0], 'admin2', 'Nie znam powiatu')
    cc = safe_get(were_at[0],'cc','Bezpaństwowiec')
    print ('{0}\n{1}\n{2}\n{3}'.format(name, admin1, admin2, cc))

if __name__ == "__main__":
    szukaj()
