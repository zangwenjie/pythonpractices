import numpy as np


def almostIncreasingSequence(sequence):
    list1 = sequence
    lon = len(list1)
    if lon == 2:
        return True
    if lon > 2 and lon <= 100000:
        for i in range(0, lon):
            if list1[i] >= -100000 and list1[i] <= 100000:
                continue
            else:
                print("the element of sequence should between -100000 and 100000")
        list2 = sorted(list1)
        for i in range(1, lon):
            for j in range(0, i):
                if list1[j] == list1[i]:
                    if list1[i - 1] > list1[i]:
                        del list1[i]
                    else:
                        del list1[j]
                    for m in range(1, lon - 1):
                        for n in range(0, m):
                            if list1[m] == list1[n]:
                                return False
                    list2 = sorted(list1)
                    print(list1)
                    print(list2)
                    if list1 == list2:
                        return True
                    else:
                        return False
        if list1 == list2:
            return True
        else:
            a = np.max(list1)
            if a != list1[lon - 1]:
                list1.remove(a)
                list2 = sorted(list1)
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


print(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]))




