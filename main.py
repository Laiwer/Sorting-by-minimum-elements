def sort_by_the_minimum_element(arr: list) -> list:
    a = []
    for _ in range(len(arr)):
        a.append(min(arr))
        arr.remove(min(arr))
    return a


if __name__ == "__main__":
    arr = sort_by_the_minimum_element([3, 1, 5, 2, 4])
    print(arr)