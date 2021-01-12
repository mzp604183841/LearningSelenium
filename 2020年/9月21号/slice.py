array = list(range(1, 101))

'''前十个'''
print(array[0:10])
'''后十个'''
print(array[-10:])
'''从5开始，每隔5个'''
print(array[4::5])
'''倒序，并且步进'''
print(array[::-2])
'''正序，取前99个'''
print(array[:-1])


def trim(ttstr):
    if ttstr == '':
        return ttstr
    elif ttstr[0] == ' ':
        return trim(ttstr[1:])
    elif ttstr[-1] == ' ':
        return trim(ttstr[:-1])
    else:
        return ttstr


def findMinAndMax(L):
    l_min = None
    l_max = None
    if len(L) == 0:
        return l_min, l_max
    elif len(L) == 1:
        l_min = L[0]
        l_max = L[0]
        return l_min, l_max
    elif len(L) >= 2:
        l_min = sorted(L)[0]
        l_max = sorted(L)[len(L) - 1]
        return l_min, l_max


mvpList = [x * x for x in list(range(1, 11))]
print(mvpList)
mlist = [x * x for x in list(range(1, 11)) if x % 2 == 0]
print(mlist)

print([m + n for m in 'abc' for n in '123'])
