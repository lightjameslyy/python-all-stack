import os
import multiprocessing


def copy_file(q, file_name, src_dierctory, dest_directory):
    """copy file"""
    # print("from %s to %s, file: %s" % (src_dierctory, dest_directory, file_name))
    src_f = open(src_dierctory + "/" + file_name, "rb")
    content = src_f.read()
    src_f.close()

    dest_f = open(dest_directory + "/" + file_name, "wb")
    dest_f.write(content)
    dest_f.close()

    # notify to queue
    q.put(file_name)


def main():
    # 1. get src directory to copy
    src_directory = input("source directory: ")

    # 2. create dest directory
    dest_directory = src_directory + "_cpy"
    try:
        os.mkdir(dest_directory)
    except:
        pass

    # 3. get file name list to copy
    file_names = os.listdir(src_directory)
    # print(file_names)

    # 4. create process pool
    pool = multiprocessing.Pool(2)

    # 5. create queue
    q = multiprocessing.Manager().Queue()

    # 6. add copy tasks to pool
    for file_name in file_names:
        pool.apply_async(copy_file, args=(q, file_name, src_directory, dest_directory))

    pool.close()
    # pool.join()

    file_num = len(file_names)
    copied_num = 0
    while True:
        file_name = q.get()
        # print("%s copied" % file_name)
        copied_num += 1
        print("\rprogress: %.2f%%" % (copied_num/file_num*100), end="")
        if copied_num >= file_num:
            break

    print()


if __name__ == '__main__':
    main()
