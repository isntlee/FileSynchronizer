from functions import sync_mode, logger_func
import argparse, time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['pyrobocopy', 'md5'])
    parser.add_argument('source_dir')
    parser.add_argument('dest_dir')
    parser.add_argument('log_file')
    parser.add_argument('period', type=int)
    args = parser.parse_args()
    logger_func(args.log_file)

    while True:
        sync_mode(args.source_dir, args.dest_dir)
        time.sleep(args.period)


if __name__ == "__main__":
    main()