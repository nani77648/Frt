def prime_palindrome(n):
    for i in range(2,n//2):
        if(n%i==0):
            return False
        else:
            continue
    return str(n)==str(n)[::-1]
n=int(input())
n=n+1
while True:
    if(prime_palindrome(n)):
        print(n)
        break
    else:
        n=n+1
        prime_palindrome(n)
