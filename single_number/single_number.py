'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # make sure our array is sorted
    arr.sort()

    # set the min count bigger than array to start
    min_count = len(arr) + 1

    # init least frequent
    least_frequent = -1

    # establish counter
    curr_count = 1

    # loop over starting on the second index since we compare backwards
    for i in range(1, len(arr)):

        # if there are two in consecutive order ( we sorted remember? )
        # increase the count of the current item
        if (arr[i] == arr[i - 1]):
            curr_count += 1

        # else we assume they don't match
        else:
            # if our current count is less than the previous min
            # we are going to whittle that down and set our least frequent
            if (curr_count < min_count):
                min_count = curr_count
                least_frequent = arr[i - 1]

            curr_count = 1

    # If last element is least frequent
    if (curr_count < min_count):
        min_count = curr_count
        least_frequent = arr[len(arr) - 1]

    return least_frequent


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
