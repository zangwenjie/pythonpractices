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
        for i in list1:
            if list1.count(i) > 2:
                return False
            if list1.count(i) == 2:
                a = []
                for j in range(0, lon):
                    if list1[j] == i:
                        a.append(j)
                    a = sorted(a)
                if i < list1[a[1] - 1]:
                    del list1[a[1]]
                else:
                    del list1[a[0]]
                list2 = sorted(list1)
                for j in list2:
                    if list2.count(j) >= 2:
                        return False
                if list1 == list2:
                    return True
                else:
                    return False
                    # for i in range(1,lon):   #如果有一对相同的元素
        #     for j in range(0,i):
        #         if list1[j]==list1[i]:
        #             if list1[i-1] > list1[i]: #如果相同的元素中，后边的那个比它的前一项小，则删除该元素
        #                 del list1[i]
        #             else:
        #                 del list1[j]   #如果相同元素中，后边的一项比它的前一项大，则删除前面的相同元素
        #             for m in range(1,lon-1):#如果剩余列表中，仍有相同元素，则返回false，否则排序对比
        #                 for n in range(0,m):
        #                     if list1[m]==list1[n]:
        #                         return False
        #             list2 = sorted(list1)
        #             if list1 == list2:
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             continue
        print("bugs")
        if list1 == list2:
            return True
        else:
            print("bugubug")
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


