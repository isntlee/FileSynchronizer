from functions import pyrobocopy, logger_func
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', choices=['pyrobocopy', 'md5'], default='pyrobocopy')
    parser.add_argument('source_dir')
    parser.add_argument('dest_dir')
    parser.add_argument('log_file')
    parser.add_argument('period', type=int)
    args = parser.parse_args()
    logger_func(args.log_file)

    while True:
        pyrobocopy(args.source_dir, args.dest_dir)
        time.sleep(args.period)

if __name__ == "__main__":
    main()