def sample(n,k):
    return [i for i in range(n) if i % k == 0]  

# Example usage:
if __name__ == "__main__":  
    n = 20
    k = 3
    result = sample(n, k)
    print(f"Numbers from 0 to {n-1} that are divisible by {k}: {result}")