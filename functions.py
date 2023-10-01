import os, shutil, logging, hashlib, logging


def log_info(message):
    logging.info(message)


def sync_mode(source, dest, mode='pyrobocopy'):
    for file in os.listdir(source):
        s = os.path.join(source, file)
        d = os.path.join(dest, file)
        
        if os.path.isfile(s):
            if not os.path.exists(d):
                shutil.copy2(s, d)
                print(f"Copied file {s} to {d}")
                
            elif mode == 'pyrobocopy':
                if os.path.getmtime(s) > os.path.getmtime(d):
                    shutil.copy2(s, d)
                    print(f"Copied file {s} to {d}")

            elif mode == 'md5':
                if md5_hashing(s) != md5_hashing(d):
                    shutil.copy2(s, d)
                    print(f"Copied file {s} to {d}")
        elif os.path.isdir(s):
            sync_mode(s, d, mode)

    for file in os.listdir(dest):
        d = os.path.join(dest, file)
        s = os.path.join(source, file)
        
        if not os.path.exists(s):
            if os.path.isfile(d):
                os.remove(d)
                print(f"Removed file {d}")
            elif os.path.isdir(d):
                shutil.rmtree(d)
                print(f"Removed directory {d}")


def md5_hashing(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


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


