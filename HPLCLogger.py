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
    # open serial port, send "psi" command every second, and read response to CSV file. Include timestamp with each response.
    with serial.Serial(args.device, 9600, timeout=1) as ser:
        while True:
            ser.write(b"psi\r")
            response = ser.readline()
            with open("HPLCLog.csv", "a") as f:
                f.write(str(time.time()) + "," + response.decode("utf-8"))
            time.sleep(args.interval)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Optional argument which requires a parameter
    parser.add_argument("-d", "--device", action="store", dest="device", default="/dev/ttyUSB0", help="Set device to log from")
    parser.add_argument("-i", "--interval", action="store", dest="interval", type=int, default="1", help="Set interval to log data in seconds")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
