import os, shutil, logging, hashlib, logging


def pyrobocopy(source, dest):
    for file in os.listdir(source):
        s = os.path.join(source, file)
        d = os.path.join(dest, file)
        
        if os.path.isfile(s):
            if not os.path.exists(d) or os.path.getmtime(s) > os.path.getmtime(d):
                shutil.copy2(s, d)
                log_info(f"Copied file {s} to {d}")
        elif os.path.isdir(s):
            sync_dirs(s, d)

    for file in os.listdir(dest):
        d = os.path.join(dest, file)
        s = os.path.join(source, file)
        
        if not os.path.exists(s):
            if os.path.isfile(d):
                os.remove(d)
                log_info(f"Removed file {d}")
            elif os.path.isdir(d):
                shutil.rmtree(d)
                log_info(f"Removed directory {d}")


def log_info(message):
    logging.info(message)


def logger_func(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a file handler
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def md5(source, dest):
    file1 = "path/to/file1"
    file2 = "path/to/file2"

    if md5(file1) == md5(file2):
        print("The files are identical")
    else:
        print("The files are different")

# Add this below -> 