n = int(input())
def prob(n):
    if (n % 2 == 0):
        return n / 2
    else:
        a = (n - 2) / 2
        return a - n
if __name__ == "__main__":
    
    print (prob(n))        

