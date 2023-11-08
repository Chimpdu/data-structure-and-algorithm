def subsets(n: int) -> list:
    choice = [0] * n
    result = []
    subsets_help(n, result, choice)
    # list in python is call by reference
    return result


def subsets_help(k: int, result: list, choice: list):
    if k-1 < 0:
        temporary = []
        all_empty = True
        for i in range(len(choice)):
            if choice[i] == 1:
                all_empty = False
                temporary.append(i+1)
        if not all_empty:
            result.append(temporary)

    else:
        for i in (0, 1):
            choice[k-1] = i
            subsets_help(k-1, result, choice)


if __name__ == "__main__":

    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
    # [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
    # [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]
