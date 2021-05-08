"""

example capture the console logger without passing log_stream to the hanlder
then assert if certain content is in the output
"""

import logging
import logging.handlers
import sys
from io import StringIO


def main():
    """
    main()
    :return:
    """
    # these two lines must be before calling the setup_logger()
    log_stream = StringIO()
    sys.stderr = log_stream

    setup_logger()
    log = logging.getLogger()
    log.info("test logger INFO")
    log.debug("test logger DEBUG")
    content = log_stream.getvalue()
    print(f"length of console log output: {len(content)}")
    print("=== contents ===")
    print(content, end='')
    print("================")

    # restore sys.stderr back to original stream
    sys.stderr = sys.__stderr__
    assert ('XYZZY' in content) is False, "we don't expect XYZZY in the logging output"
    assert 'DEBUG' in content, "we expect DEBUG in the logging output"

    # end of main()


def setup_logger():
    """
        set up a console logger
    """
    log = logging.getLogger()
    level = logging.DEBUG
    log.setLevel(level)

    root_logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s %(module)s %(filename)s:%(lineno)s %(funcName)20s() - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)


if __name__ == '__main__':
    main()
