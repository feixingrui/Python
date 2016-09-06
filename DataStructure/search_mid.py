#寻找中位数，两个列表等长且升序
#从头开始分别比较两个列表，用k来计数，当k=n/2时即为中位数
#两数若相等k增2，若其中一个大于另外一个，则把令中位数等于小的，同时k增1

s1 = [1,2,3,4,5]
s2 = [1,1,1,1,11]

def search_mid():
    i = j = k = 0
    while(k<5):
        if(s1[i] == s2[j]):
            i += 1
            j += 1
            k += 1
            mid = s1[i]
        elif(s1[i] > s2[j]):
            mid = s2[j]
            j += 1
        else:
            mid = s1[i]
            i += 1
        k += 1
    return mid

print('%s' %search_mid())
