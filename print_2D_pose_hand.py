import os
import pandas as pd
import pprint
import numpy as np

FJoin = os.path.join 
def GetFiles(path):
	file_list, dir_list = [], []
	for dir, subdirs, files in os.walk(path):
		file_list.extend([FJoin(dir, f) for f in files])
		dir_list.extend([FJoin(dir, d) for d in subdirs])
	file_list = filter(lambda x: not os.path.islink(x), file_list)
	dir_list = filter(lambda x: not os.path.islink(x), dir_list)
	return file_list, dir_list
files, dirs = GetFiles(os.path.expanduser("handpose"))
for file in files:
	if file.endswith(".pickle"):
		chiso=file.rfind('/')
		link = file[0:chiso]
		namefile= file[chiso+1:len(file)]
		Files = pd.read_pickle(file, compression='infer')
		value = Files['kps2D']
		#print('==============================================')
		#print(value)
		#print('==============================================')
		#exit()

		filename_new = namefile.replace("pickle", "txt")
		
		linktxt=link+ '/'+ filename_new
		print(linktxt)
		np.savetxt(linktxt, value)

		#with open(linktxt, "a") as f:
		#	f.truncate(0)
		#	f.write('{} {} {} {}'.format(minx, miny, maxx - minx, maxy - miny))
		#	f.close()
		#except:
		#	print("error", file )
		#	with open("handpose/error.txt", "a") as f:
		#		pprint.pprint(file, stream=f)
		#		f.close()