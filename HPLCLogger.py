#!/usr/bin/env python3
"""
HPLCLogger.py: A simple python script to log HPLC Pump data to a file.
"""

__author__ = "Ezra Kainz"
__version__ = "0.0.1"

import argparse
import serial
import time

def main(args):
    # open serial port, send "psi" command every second, and read response to CSV. Include timestamp with each response.
    with serial.Serial(args.device, 9600, timeout=1) as ser:
        while True:
            ser.write(b"psi\r")
            time.sleep(1)
            response = ser.readline()
            print("{},{}".format(time.time(), response.decode("utf-8").rstrip()))
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-d", "--device", action="store", dest="device", default="/dev/ttyUSB0", help="Set device to log from")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
