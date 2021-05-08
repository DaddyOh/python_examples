"""

Some list comprehensions

"""
import sys

sys.path.append("..")
from utils import normalize_path


def main():
    """
    Demonstrate the usage of the list comprehension to clean up a commented file
    The cleanup:
        removes blank lines
        removes empty lines after strip()
        removed commented lines with specified comment delimiter
        returns all remaining lines strip()

    :return: N/A
    """
    # remove comments and strip what space from lines in file

    commented_file = '../../test_data/commented_data.txt'
    commented_file_semicolon = '../../test_data/commented_data_different_comment.txt'
    file_exists, commented_file_abs = normalize_path(commented_file)
    assert file_exists, f"commented file {commented_file_abs} does not exist"
    file_exists, commented_file_semicolon_abs = normalize_path(commented_file_semicolon)
    assert file_exists, f"commented file {commented_file_semicolon_abs} does not exist"
    # get file contents

    with open(commented_file_abs, 'r') as f:
        lines = f.readlines()

    with open(commented_file_semicolon_abs, 'r') as f:
        lines_semicolon = f.readlines()

    assert len(lines) > 0, "fi;e contents does not exist"

    print("original lines from file\n=====================")
    for line in lines:
        print(line, end='')

    print("list comprehensions")

    # new_lines = [line.strip() for line in lines if len(line.strip())>0 if not line.strip()[0] == '#']
    new_lines = clean_commented_lines(lines)
    print("process content to remove all unwanted lines with #\n=====================")

    for line in new_lines:
        print(line)
    print("=====================")

    print("===== test with ; comment delimiter =====")

    new_lines = clean_commented_lines(lines_semicolon, comment_delimiter=';')
    print("process content to remove all unwanted lines with ;\n=====================")

    for line in new_lines:
        print(line)
    print("=====================")


# TODO move to utils.py file
def clean_commented_lines(lines: list, comment_delimiter='#'):
    """
    See below

    :param lines: a list of lines, typically from a file
    :param comment_delimiter: 1 character length only
    :return: the new list witrh lines stripped , blank lines removed and commented lines remove
    """

    return [line.strip() for line in lines if len(line.strip()) > 0 if
            not line.strip()[0] == comment_delimiter]


if __name__ == "__main__":
    main()

"""
Resources

https://docs.python.org/3.6/tutorial/datastructures.html see section on list comprehensions

"""
