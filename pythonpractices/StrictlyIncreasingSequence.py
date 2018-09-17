import numpy as np

def almostIncreasingSequence(sequence):
    list1 = sequence
    lon = len(list1)
    if lon == 2:
        return True
    if lon > 2 and lon <= 100000:
        for i in list1:
            if i >= -100000 and i <= 100000:
                continue
            else:
                print("the element of sequence should between -100000 and 100000")
        list2 = sorted(list1)
        for i in list1:
            b = list1.count(i)
            if b > 2:
                return False
            if b == 2:
                a = []
                for j in range(0,lon):
                    if list1[j]==i:
                        a.append(j)
                    a = sorted(a)
                if i < list1[a[1]-1]:
                    del list1[a[1]]
                else:
                    del list1[a[0]]
                list2 = sorted(list1)
                for j in list2:
                    if list2.count(j)>=2:
                        return False
                if list1 == list2:
                    return True
                else:
                    return False
        if list1 == list2:
            return True
        else:
            a = np.max(list1)
            if a != list1[lon-1]:
                list1.remove(a)
                list2=sorted(list1)
                if list1 == list2:
                    return True
                else:
                    return False
            else:
                list1.remove(a)
                b = np.min(list1)
                print(b)
                list1.remove(b)
                list2 = sorted(list1)
                if list2 == list1:
                    return True
                else:
                    return False
    else:
         print("the length of sequence should between 2 and 100000")


