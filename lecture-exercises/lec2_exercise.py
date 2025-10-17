# An inversion in an array, a, is a pair (i,j) such that i<j and a[i]>a[j]
# Suggest a simple algo to count the no. inversions in an array of size n complexity? O(n^2)

# Example: a=[1,3,2,4], (1,3), 1<3, a[1]=3, a[3]=2, a[1]>a[3]
test1 = [1,3,2,4]
test2 = [1,5,2,8,3,9,10]

def inversion_counter(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):  # always i<j
            if arr[i] > arr[j]:
                print(f'Inversion at:')
                print(f'idx={i}; idx={j}')
                print(f'a[i]={arr[i]}; arr[j]={arr[j]}\n')
                count += 1
    return f'Total inversions: {count}'

if __name__ == '__main__':
    print(inversion_counter(test1))
    print(inversion_counter(test2))