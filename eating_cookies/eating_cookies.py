'''
Input: an integer
Returns: an integer
'''

# added a cache for recursiveness
def eating_cookies(n, cache={}):
    print(n, cache)
    # check cache for key of n
    if n in cache:
        return cache[n]
    
    # handle 0 and 1 being passed
    elif n < 0:
        cache[n] = 0
        return cache[n]
    elif n == 0:
        cache[n] = 1
        return cache[n]
    
    # else, set the key to the recursive result of the func
    else:
        cache[n] = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
