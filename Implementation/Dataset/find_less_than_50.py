import os
import shutil

DATA_PATH = '/Users/yuandali/Programs/daily-utils/Implementation/data'

def get_dir_list(path):
    items = os.listdir(path)
    return [item for item in items if os.path.isdir(os.path.join(path, item)) == True]


def is_less_than_fifty(directory):
    path = os.path.join(DATA_PATH, directory)
    file_list = os.listdir(path)
    return len(file_list) < 50

def copy_images(directory):
    path = os.path.join(DATA_PATH, directory)
    file_list = os.listdir(path)
    ori_count = len(file_list)
    count = ori_count
    cur = 0
    while (count < 50):
        count += 1
        shutil.copyfile(os.path.join(path, file_list[cur]), os.path.join(path, ('%04d.jpg' % count)))
        cur = (cur + 1) % ori_count

if __name__ == "__main__":
    dir_list = get_dir_list(DATA_PATH)
    res = []
    for directory in dir_list:
        if is_less_than_fifty(directory) == True:
            res.append(directory)
            copy_images(directory)

    print len(res)
    with open('less_than_50.txt', 'w') as fout:
        for item in res:
            fout.write(item)
            fout.write('\n')
