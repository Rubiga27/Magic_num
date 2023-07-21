def is_magic(A):
    sum=0
    for i in A:
        sum+=int(i)
    if sum>=10:
        return is_magic(str(sum))
    if sum <=10:
        if sum==1:
            return 1
        else:
            return 0

    
A=input()
print(is_magic(A))

