import os

SUN_DATABASE_PATH = '/Users/yuandali/Programs/NYU_MMVC'
SKETCH_DATABASE_PATH = '/Users/yuandali/Downloads/sbsr-cvpr15_datasets/SHREC13_SBR_TRAINING_SKETCHES/SHREC13_SBR_TRAINING_SKETCHES'

def get_sketch_categories():
    return get_dir_list(SKETCH_DATABASE_PATH)

def get_sun_categories():
    with open('SUN_category_list.txt', 'r') as fin:
        content = fin.readlines()
    return [item.split('/')[0] for item in content]

def get_dir_list(path):
    items = os.listdir(path)
    return [item for item in items if os.path.isdir(os.path.join(path, item)) == True]

def get_common_categories():
    sketch_category = get_sketch_categories()
    print '%d categories for sketch' % len(sketch_category)

    sun_categories = get_sun_categories()
    print '%d categories for SUN database' % len(sun_categories)

    intersection = set(sketch_category).intersection(sun_categories)
    print '%d common categories in both datasets' % len(intersection)
    return sorted(intersection)

if __name__ == "__main__":
    common_categories = get_common_categories()
    with open('common_categories.txt', 'w') as fout:
        for category in common_categories:
            fout.write(category)
            fout.write('\n')
    print 'File saves as common_categories.txt'
