import os
import shutil
import requests
import re

base_url = 'http://groups.csail.mit.edu/vision/SUN/objects/pages/'

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

def save_image(category, file_name, number):
    url = base_url + category + '/' + file_name
    if not os.path.exists(category):
        os.makedirs(category)
    saved_file_name = ('%06d' % number) + '.gif'
    path = category + '/' + saved_file_name

    try:
        response = requests.get(url, stream=True)
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print '[' + category + '] ' + file_name + ' saved as ' + saved_file_name
    except:
        print 'An error occurs when parsing ' + file_name + ' in ' + category

if __name__ == "__main__":
    categories = ['chair', 'airplane']
    fetch_all_categories(categories)
