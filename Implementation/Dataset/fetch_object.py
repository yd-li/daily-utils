import os
import shutil
import requests
import re

base_url = 'http://groups.csail.mit.edu/vision/SUN/objects/pages/'
saved_image_base_path = './data'

def fetch_all_categories(categories):
    for category in categories:
        get_category(category)

def get_html(category):
    url = base_url + category
    return requests.get(url)

def get_category(category):
    image_list = []
    try:
        html = get_html(category)
        content = html.text
        image_list = re.findall('target="_blank"> <img src="(.*?gif)"></a>', content, re.S)
    except:
        print 'Error when parsing ' + category + ' category'

    number = 1
    for file_name in image_list:
        save_image(category, file_name, number)
        number += 1
        if number > 50:
            break
    if number < 50:
        print '[Warning] %s only has %d pictures' % (category, number)
        with open('log.txt', 'w+') as flog:
            flog.write('%s only has %d pictures' % (category, number))

def save_image(category, file_name, number):
    url = base_url + category + '/' + file_name
    if not os.path.exists(os.path.join('data', category)):
        os.makedirs(os.path.join('data', category))
    saved_file_name = ('%04d' % number) + '.gif'
    path = os.path.join('data', os.path.join(category, saved_file_name))

    try:
        response = requests.get(url, stream=True)
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print '[' + category + '] ' + file_name + ' saved as ' + saved_file_name
    except:
        print 'An error occurs when parsing ' + file_name + ' in ' + category

def get_object_list():
    with open('common_categories.txt', 'r') as fin:
        object_list = fin.readlines()
    return [obj.split('\n')[0] for obj in object_list]

def clear_log():
    with open('log.txt', 'w') as flog:
        flog.write('')

if __name__ == "__main__":
    clear_log
    object_list = get_object_list()
    fetch_all_categories(object_list)
