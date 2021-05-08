"""
Some examples on use of pathlib.Path


"""
from pathlib import Path
import os.path
import sys

sys.path.append("..")
from utils import normalize_path, get_file_pathlib_contents


def main():
    """
    Main program
    """
    rel_path_file = '../../test_data/relative_path/data.txt'
    rel_path_file_bad = '../../test_data/relative_path/bad/data.txt'
    # abs_path assumes mac OSX
    abs_path = '/tmp'
    abs_path_bad = '/junk'
    # use os version just till we figure out how pathlib works
    assert os.path.exists(rel_path_file), f"file does not exist: {rel_path_file}"
    assert os.path.exists(rel_path_file_bad) is False, f"file does exist: {rel_path_file_bad}"
    # What do we want to know
    # is a path or file relative or absolute
    # does it exist

    # start with relative paths and move to absolute

    p = Path(rel_path_file)
    assert p.exists(), f"file does not exist: {rel_path_file}"
    # because this is a file not a dir
    assert p.is_dir() is False, f"dir does not exist: {rel_path_file}"

    # get absolute path
    p_abs = p.resolve()
    assert p.exists(), f"absolute file does not exist: {rel_path_file}"
    print(f"absolute path for {rel_path_file}: {p_abs}")

    # RELATIVE PATHS
    # what happens with p.resolve() with path that does not exist
    p_bad = Path(rel_path_file_bad)
    # this does notg throw and error
    p_bad_abs = p_bad.resolve()
    print(f"absolute path for {rel_path_file_bad}: {p_bad_abs}")
    assert p_bad_abs.exists() is False, f"{rel_path_file_bad} does exist, it should not"

    # ABSOLUTE PATHS
    print("results of normalize_path() with good absolute path")
    p_exists, p_abs_ = normalize_path(abs_path)
    assert p_exists, f"path {abs_path} should exist"
    print(p_exists, p_abs_)

    print("results of normalize_path() with bad absolute path")
    p_exists, p_abs_ = normalize_path(abs_path_bad)
    assert p_exists is False, f"path {abs_path_bad} should not exist"
    print(p_exists, p_abs_)

    # can we read a file using pathlib.PosixPath as the file str?
    print(f"contents of {rel_path_file}\n {get_file_pathlib_contents(rel_path_file)}")
    assert get_file_pathlib_contents(
        rel_path_file) == '# this is content in a relative path', "contents of file not correct"


if __name__ == "__main__":
    main()

"""
Resources
pathlib docs https://docs.python.org/3/library/pathlib.html



"""
