# This approch has nlogn time complexity, so instead of this we can use Hashing Method to get O(n) complexity.


def ArithmaticProgression(arr):
    n = len(arr)
    if (n == 1) : return True

    arr.sort()

    d = arr[1] - arr[0]
    for i in range(2,n):
        if (arr[i] - arr[i-1] != d):
            return False
        
    return True


if __name__ == '__main__':
    arr = [ 20, 15, 5, 0, 10 ]
    print(ArithmaticProgression(arr))