import scipy.io as sio
import scipy.misc as misc
import numpy as np

mat = sio.loadmat('shrec-default-epoch20-test.mat')
print mat
# print len(mat['labels'])
# print len(mat['triples'])
print len(mat['dist_mat'])
print len(mat['dist_mat'][0])
# print len(mat['datax'])
# print len(mat['datay'])
# print len(mat['data_valid'])
print len(mat['view_label'])

print '-----------'


ind = mat['view_label']
arr = mat['dist_mat']
# arr.sort()
# maxIdx = 0
count = 0

file = open('dist_mat.txt', 'w')

for i in range(0, len(arr)):
	for j in range(0, len(arr[i])):
		file.write('%s ' % arr[i][j])
	print np.argmin(arr[i]), ind[np.argmin(arr[i])]
	if ind[np.argmin(arr[i])] == 19:
		count += 1
	file.write('\n')
print 'count: %d\n' % count

# file.write(arr)
file.close()
	
