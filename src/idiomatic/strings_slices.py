"""
Demonstratee on string work and especially slices

"""


def main():
    """
    main()

    """
    test_str1 = "#12345"

    print(f"test_str1: {test_str1}")
    print(f"first char of {test_str1}: {test_str1[0]}")

    print("===== How do slices work? =====")

    print("obj[start:stop:step]")
    print(f"first char of {test_str1} using slice: {test_str1[0]}")
    print(test_str1[0:1])
    assert test_str1[0:1] == '#', "1st char must be '#'"

    # x[:]
    # empty start means start at the beginning
    # empty stop meaks continue to the end

    print("revese the chars in the string")
    test_str1_reversed = test_str1[::-1]
    print(f'test_str1_reversed: {test_str1_reversed}')
    assert test_str1_reversed == '54321#', "reversed string must be '54321#'"


if __name__ == '__main__':
    main()

"""
references



"""
