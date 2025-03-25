import pytest
import logging as log
import os
import sys
import subprocess
import argparse

LOGS_DIR = "logs"
DEBUG_LOG=f"{LOGS_DIR}{os.sep}{LOGS_DIR}"
XML_DIR=f"{LOGS_DIR}{os.sep}xmlreports"

def run_tests(directory="tests/",  args=None):
    """
    Tests to check specific classes
    """

    if directory is None:
        directory = "tests/"

    test_type = "all"

    run_command = [f"{sys.executable}", "-m", "pytest", "-v"]

    test_out = subprocess.run(run_command,
                              capture_output=True,
                              text=True,
                              check=False)
    log.info(f"Test completed with status: {test_out.returncode}")

def main():
    """
    Main loop
    """
    argparser = argparse.ArgumentParser(description="Run tests")
    argparser.add_argument("-d", "--directory", help="Test directory")
    args = argparser.parse_args()


    log.basicConfig(filename=DEBUG_LOG, level=log.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    tests_failed=False
    if args.direcrotory:
        for directory in args.directory:
            ret_code = run_tests(directory, args=args)
            if ret_code != 0:
                test_failed = ret_code
    else:
        ret_code = run_tests(args=args)
        if ret_code != 0:
            test_failed = ret_code

    if tests_failed:
        sys.exit(tests_failed)

if __name__ == "__main__":
    main()



