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
