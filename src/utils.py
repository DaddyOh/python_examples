"""
Various functions that will be used across examp,e files

"""
from pathlib import Path
import logging
import logging.handlers
import glob
import os
import sys


def remove_folder_files(folder_path: str):
    """
    Warning this delete files - make sure you operate on the right folder

    this only operates on the first level files

    :param folder_path:
    :return:
    """

    path_exists, abs_path = normalize_path(folder_path)
    if not path_exists:
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    cwd = os.getcwdb()
    os.chdir(folder_path)

    files = glob.glob('*')
    for filename in files:
        # TODO what to do where
        # print(filename)
        os.unlink(filename)
    os.chdir(cwd)


def normalize_path(path_or_file: str):
    """
    Useful function to get status of path_or_file.exists() and get its absolute path version
    :param path_or_file: relative or absolute file path (with file or just path)
    :return: boolean, absolute_path as pathlib.PosixPath
    """

    p = Path(path_or_file)
    p_abs = p.resolve()
    print(type(p_abs))
    return p_abs.exists(), p_abs


def setup_logger(debug, log_folder, console_log=True, console_log_to=sys.stderr):
    """
    sets up root, error and warning loggers
    optionally sets up console logger
    :param console_log_to:
    :param debug: boolean turns on debug for logging
    :param log_folder: relative or absolute path (must exist)
    :param console_log: boolean turns on console logging in addition to file loggint
    :return: NO RETURN VALUE
    """

    """
    
    :param debug: boolean turns on debug for logging
    :param log_folder: 
    :return: 
    
    Note that the console_log_to allows us to capture the contsole log and grep it
    
    Probably only use that feature when testing
    
    see 
    """
    log_folder_path = Path(log_folder)
    log = logging.getLogger()
    level = logging.INFO
    if debug:
        level = logging.DEBUG
    log.setLevel(level)

    # rootLogger appears good
    # %(filename)s:%(lineno)s - %(funcName)20s()

    root_logger = logging.getLogger()
    fh = logging.handlers.RotatingFileHandler(log_folder_path / 'root.log', "a", 50000, 2)
    # formatter = logging.Formatter('%(levelname)s: %(asctime)s %(module)s %(funcName)s - %(message)s')
    formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s %(module)s %(filename)s:%(lineno)s %(funcName)20s() - %(message)s')
    fh.setFormatter(formatter)

    if console_log:
        console_handler = logging.StreamHandler(console_log_to)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    root_logger.addHandler(fh)

    fh2 = logging.handlers.RotatingFileHandler(log_folder_path / 'error.log', "a", 20000, 2)
    fh2.setLevel(logging.ERROR)
    fh2.setFormatter(formatter)
    root_logger.addHandler(fh2)

    fh3 = logging.handlers.RotatingFileHandler(log_folder_path / 'warning.log', "a", 30000, 2)
    fh3.setLevel(logging.WARNING)
    fh3.setFormatter(formatter)
    root_logger.addHandler(fh3)


def get_file_pathlib_contents(file_path: str):
    """
    We can read a file that is a pathlib.PosixPath object

    :param file_path: pathlib.PosixPath
    :return contents: str
    """
    fp = open(file_path, 'r')
    return fp.read()


if __name__ == "__main__":
    # for testing only
    path_bad = '../bad_path'
    path_good = './logging/logs'
    remove_folder_files(path_good)

"""
https://docs.python.org/3.6/library/exceptions.html
https://docs.python.org/3.6/library/exceptions.html#exception-hierarchy

"""
