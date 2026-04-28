# Without using the max() function in python, create a function that returns the max value using:
# recursion
# a pivot that splits the list in half

def max_num(A): 
    if len(A) == 1:
        return A[0]

    m = len(A) // 2

    left_max = max_num(A[:m])
    right_max = max_num(A[m:])

    return left_max if left_max > right_max else right_max


def main():
    sanity_check = [
        [3, 1, 4, 1, 5, 9],
        [10],
        [-5, -2, -9, -1],
        [7, 7, 7, 7],
        [100, 50, 200, 150],
    ]

    for a in sanity_check:
        print(f"{a} : {max_num(a)}")

if __name__ == "__main__":
    main()
