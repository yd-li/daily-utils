import os

import scipy.io as sio
from PIL import Image

def gif21d(gif_file):
	img = Image.open(gif_file)
	# img.putpalette(img.getpalette())
	new_img = Image.new("RGB", img.size)
	new_img.paste(img)
	new_img = new_img.resize((100, 100), Image.ANTIALIAS)
	img_3d = list(new_img.getdata())
	img_1d = []
	for j in range(0, len(img_3d)):
		img_1d.append((0.2126 * img_3d[j][0] + 0.7152 * img_3d[j][1] + 0.0722 * img_3d[j][2]) / 255.0)
	return img_1d

def gifs2mat(data_dir, out_file, mat_file_name, dataset_dir):
	mat_ori = loadMat(mat_file_name)
	class_index = getClassIndex(dataset_dir)

	class_index_new = getClassIndex(data_dir)

	mat = {'datax': [], 'datay': [], 'data_imid': []}
	i_mid = 1
	for i in range(0, len(class_index)):
		print 'index of class\t', i+1
		print os.path.join(data_dir, class_index[i])
		if os.path.isdir(os.path.join(data_dir, class_index[i])) == True:
			for dirpath, subdirs, files in os.walk(os.path.join(data_dir, class_index[i])):
				for file in files:
					file_path = os.path.join(dirpath, file)
					mat['datax'].append(gif21d(file_path))
					mat['datay'].append([i+1])
		else:
			continue	# if only want to generate those images included in data_dir withough any sketch
			for j in range(i * 50, (i + 1) * 50):
				mat['datax'].append(mat_ori['datax'][j])
				mat['datay'].append(mat_ori['datay'][j])

	sio.savemat(out_file, {'datax': mat['datax'], 'datay': mat['datay'], 'data_imid': mat['data_imid']})
	print 'Save %s' % out_file

def getClassIndex(dataset_dir):
    items = os.listdir(dataset_dir)
    return [item for item in items if os.path.isdir(os.path.join(dataset_dir, item)) == True]

def loadMat(mat_file_name):
	return sio.loadmat(mat_file_name)

if __name__ == '__main__':
	"""
	Convert data -- images of different classes to mat

	Parameters:
		@data dir, e.g. './data'
								--airplane
								--bed
								--...
		@name of out file, e.g. 'out_mat.mat'
		@original mat file, e.g. 'sketch_train_ori.mat'
		@train dataset dir
	"""
	gifs2mat('./test', 'sketch_test.mat', 'sketch_train_ori.mat', '../sbsr-cvpr15_datasets/SHREC13_SBR_TRAINING_SKETCHES/SHREC13_SBR_TRAINING_SKETCHES')
