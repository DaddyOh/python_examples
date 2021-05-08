"""

capture the console logger stream and test it for certain content

"""

import os.path
import sys
from io import StringIO
import logging

# necessary to import modules above this file
sys.path.append("..")
# noinspection PyPep8
from utils import normalize_path, setup_logger


def main():
    """

    Test console logging by capturing the console log and looking for conternt in that stream

    """
    log_location = './logs'
    print(__file__)
    # pycharm is stuck and thinks I'm in a different folder
    file_parts = __file__.split('/')
    # remove script name
    del file_parts[-1]
    new_cwd = "/".join(file_parts)
    print(new_cwd)
    os.chdir(new_cwd)

    # pycharm thinks this file in in the ./logs folder
    # this is necessary to make it work wiht pycharm
    log_location_exists, log_location_abs = normalize_path(log_location)
    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    print(log_location)
    print(log_location_abs)
    log_debug = True
    log_console = True
    cwd = os.getcwd()
    print(cwd)

    assert log_location_exists, f"log location needs to exist: {log_location_abs}"

    print("setup logger")

    log_stream = StringIO()
    setup_logger(log_debug, log_location, log_console, console_log_to=log_stream)
    print("setup root logger to use")
    log_root = logging.getLogger()

    log_root.info("log to root logger")
    log_root.info("XYZZY should be in stderr because we are logging to the console")

    content_ = log_stream.getvalue()
    print(f"len of log content: {len(content_)}")
    print("\nlog_stream contents before assertions below\n=================")
    sys.stdout.write(content_)
    print("end of content\n=================")

    assert "INFO" in content_, f"INFO text not found in console logging output"

    # do DEBUG messages appear in root - expect not to find then
    log_root.info("We do not expect D E B U G messages in root log file")
    content_ = log_stream.getvalue()
    assert ("DEBUG" in content_) is False, f"DEBUG text found in  console logging output"

    # add DEBUG message to root
    log_root.debug("we expect D E B U G message in root log file")
    content_ = log_stream.getvalue()
    assert "DEBUG" in content_, f"DEBUG text NOT found in root  console logging output"


if __name__ == "__main__":
    main()
