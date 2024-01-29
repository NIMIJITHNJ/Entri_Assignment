def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)


x = int(input('Enter a number:'))
result=sum(x)
print('Sum of integers from 1 to',x,'=', result)