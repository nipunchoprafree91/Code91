########### 0 1 1 2 3 5 8
def recursive_fibonacci(n):
    if  n <= 1 :
        return n
    else:
       return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def main():
    n_terms = 10

    if n_terms < 0:
        print("Its less than 0")
    else:
        print("Fibonacci series is :")
        
        for i in range(n_terms):
            print(recursive_fibonacci(i))
            
if  __name__ == "__main__":
    main()



