pos=-1
def search(list,num):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==num:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<num:
                l = mid - 1
            else:
                u = mid + 1
    return False

list=[1,2,3,4,5,6,7,8,9,10,34,67,88,99,100]
n=15
if search(list,n):
    print('found at ', pos+1)
else:
    print('not found')

