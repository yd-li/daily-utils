"""
	Decrease/increase font-size in web page for better print layout

	@old_file_name
	@new_file_name
	@percentage

"""

old_file_name = 'main.css'
new_file_name = 'main_new.css'
percentage = 0.7

with open(old_file_name, 'r') as oldfile:
	newfile = open(new_file_name,'w')
	for line in oldfile:
		if 'font-size' in line and 'px' in line:
			index1 = line.index('font-size')
			index2 = line.index('px')
			new_line = line[:index1+11] + str(int(line[index1+11:index2]) * percentage) + line[index2:] + '\n'
			# print line
			# print new_line
			newfile.write(new_line)
		else:
			newfile.write(line)
	newfile.close()
    