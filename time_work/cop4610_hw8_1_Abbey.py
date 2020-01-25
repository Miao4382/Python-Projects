import os


def get_size(start_path='C:\\'):
    total_size = 0
    total_modified_size = 0
    num_files = 0
    num_modified_files = 0

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if os.path.exists(fp):
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
                    num_files += 1
                    if os.path.getctime(fp) != os.path.getmtime(fp):
                        total_modified_size += os.path.getsize(fp)
                        num_modified_files += 1

    print('Total file number: ', num_files)
    print('Modified file number: ', num_modified_files)
    print('Total bytes: ', total_size)
    print('Total bytes of modified file: ', total_modified_size)


get_size()
