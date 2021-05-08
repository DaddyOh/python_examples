"""
example for real python user for capturing console output
"""

import logging
import logging.handlers
import sys
from io import StringIO


def main():
    log_stream = StringIO()
    setup_logger(console_log_to=log_stream)
    log = logging.getLogger()
    log.info("test logger INFO")
    log.debug("test logger DEBUG")
    content = log_stream.getvalue()
    print(f"length of console log output: {len(content)}")
    print("=== contents ===")
    print(content, end='')
    print("================")
    assert ('XYZZY' in content) == False
    assert 'DEBUG' in content

    # end of main()


def setup_logger(console_log_to=sys.stderr):
    log = logging.getLogger()
    level = logging.DEBUG
    log.setLevel(level)

    root_logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s %(module)s %(filename)s:%(lineno)s %(funcName)20s() - %(message)s')

    console_handler = logging.StreamHandler(console_log_to)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)


if __name__ == '__main__':
    main()
