# Write a resurise function to calculate the sum of first n natural numbers

# n!=(n-1)!*n
#sum(n)=sum(n-1)+n


def sum(n):
    if n==1 or n==0:
        return 1
    return n + sum(n-1)

# f=factorial_iter(5)
f= sum(5)
print(f)