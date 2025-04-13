def find_max_recursive(nums):
    if not nums:
        raise ValueError("List is empty")

    if len(nums) == 1:
        return nums[0]

    max_rest = find_max_recursive(nums[1:])
    return nums[0] if nums[0] > max_rest else max_rest

def main():
    test_cases = [
        [3, 5, 2, 9, 1],
        [-7, -3, -22, -1],
        [42],
        [0, 0, 0, 0],
        []
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {case}")
        try:
            result = find_max_recursive(case)
            print(f"Max value: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
