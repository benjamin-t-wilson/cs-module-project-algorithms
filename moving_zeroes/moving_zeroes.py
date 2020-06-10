'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # count total number of 0s and set a pointer
    zero_count = arr.count(0)
    curr_count = 0

    # provided our current count is less than the total number
    # we will not hit the index not found error
    while curr_count < zero_count:
        # remove the 0 and place at the end
        arr.pop(arr.index(0))
        arr.append(0)
        # progress counter
        curr_count += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
