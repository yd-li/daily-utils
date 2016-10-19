import os

SKETCH_DATABASE_PATH = '/Users/yuandali/Downloads/sbsr-cvpr15_datasets/SHREC13_SBR_TRAINING_SKETCHES/SHREC13_SBR_TRAINING_SKETCHES'

def get_dir_list(path):
    items = os.listdir(path)
    return [item for item in items if os.path.isdir(os.path.join(path, item)) == True]

if __name__ == "__main__":
    lst = get_dir_list(SKETCH_DATABASE_PATH)
    all_list = sorted(lst)
    with open('sketch_category_list.txt', 'w') as fout:
        for item in all_list:
            fout.write(item)
            fout.write('\n')
