"""
Example of how to use the logger.

"""

from pathlib import Path
import sys

sys.path.append("..")
from utils import normalize_path, setup_logger, remove_folder_files, get_file_pathlib_contents
import logging


def main():
    """

    """
    log_location = './logs'
    log_location_exists, log_location_abs = normalize_path(log_location)
    log_debug = True
    log_console = True
    # TODO create example script without console logging turned on
    app_name = "App logging example 1"
    print(f"abs log location: {log_location_abs}")
    assert log_location_exists, "log location needs to exist"

    if log_location_exists:
        remove_folder_files(log_location_abs)
    else:
        raise FileExistsError(f"folder does not exist: {log_location_abs}")

    print("setup logger")
    setup_logger(log_debug, log_location, log_console)
    print("setup root logger to use")
    log_root = logging.getLogger()
    print("set up app name logger")
    log_app = logging.getLogger(app_name)
    log_root.info("log to root logger")
    log_app.info("log to app name logger")
    some_func()

    # Assert that we are seeing log files in the folder
    log_loc_path = Path(log_location_abs)
    root_file = log_loc_path / "root.log"
    assert root_file.exists(), f"root logging file does not exist: {root_file}"

    # do info messages appear in root
    content_ = get_file_pathlib_contents(root_file)
    assert "INFO" in content_, f"INFO text not found in root log file: {root_file}"

    # do DEBUG messages appear in root - expect not to find then
    log_root.info("We do not expect D E B U G messages in root log file")
    assert ("DEBUG" in content_) is False, f"DEBUG text found in root log file: {root_file}"

    # add DEBUG message to root
    log_root.debug("we expect D E B U G message in root log file")
    content_ = get_file_pathlib_contents(root_file)
    assert "DEBUG" in content_, f"DEBUG text NOT found in root log file: {root_file}"


def some_func():
    """
    Just an function to test logging
    """
    log = logging.getLogger()
    log.info("inside some_func()")


if __name__ == "__main__":
    main()
