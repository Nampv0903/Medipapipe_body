import matplotlib.pyplot as plt
import os
import numpy as np
path = 'D:\VS_Code\Medipapipe_body\{}est'.format('t')

def get_files(path):
    """
    Lấy danh sách tất cả các file .txt trong folder và các folder con của folder đầu vào.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))
    return file_list

files = get_files(path)
for file in files:
				coords = np.loadtxt(file)
				# Sắp xếp lại các điểm theo thứ tự tương ứng với các Marker
				markers = ['LFHD', 'RFHD', 'LBHD', 'RBHD', 'C7', 'T10', 'CLAV', 'STRN', 'RBAK', 'LSHO', 
					'LUPA', 'LELB', 'LWRA', 'LWRB', 'LFIN', 'RSHO', 'RUPA', 'RELB', 'RFRM', 'RWRA', 
					'RWRB', 'RFIN', 'LASI', 'RASI', 'LPSI', 'RPSI', 'LTHI', 'LKNE', 'LTIB', 'LANK', 
					'LHEE', 'LTOE', 'RTHI', 'RKNE', 'RTIB', 'RANK', 'RHEE', 'RTOE', 'LFRM']
				coords_dict = {}
				for i, marker in enumerate(markers):
					coords_dict[marker] = coords[i]

				# Vẽ từng điểm và đánh nhãn tương ứng
				fig = plt.figure(figsize=(13, 23))
				ax = fig.add_subplot(111)
				# for i, coord in enumerate(coords):
				# 	x, y, z = coord
				# 	print(x,y,z)
				# 	ax.scatter(x, z, color='black', marker='o')
				# 	ax.annotate(markers[0], xy=(x[0], z[0]), xytext=(-10, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LFHD 
				x, y, z = coords[0]	
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LFHD', (x, z), xytext=(-10, -20), textcoords='offset points', fontsize=20)

				# Vẽ điểm RFHD 
				x, y, z = coords[1]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RFHD', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)

				# Vẽ điểm LBHD 
				x, y, z = coords[2]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LBHD', (x, z), xytext=(-10, 10), textcoords='offset points', fontsize=20)

				# Vẽ điểm RBHD 
				x, y, z = coords[3]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RBHD', (x, z), xytext=(-10, 10), textcoords='offset points', fontsize=20)

				# Vẽ điểm C7 
				x, y, z = coords[4]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('C7', (x, z), xytext=(-10, 12), textcoords='offset points', fontsize=20)

				# Vẽ điểm T10
				x, y, z = coords[5]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('T10', (x, z), xytext=(10, -20), textcoords='offset points', fontsize=20)

				# Vẽ điểm CLAV 
				x, y, z = coords[6]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('CLAV', (x, z), xytext=(15, 10), textcoords='offset points', fontsize=20)

				# Vẽ điểm STRN 
				x, y, z = coords[7]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('STRN', (x, z), xytext=(-10, -20), textcoords='offset points', fontsize=20)

				# Vẽ điểm RBAK 
				x, y, z = coords[8]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RBAK', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)
				# for marker, coord in coords_dict.items():
				#     x, y, z = coord
				#     plt.scatter(x, z, color='black', marker='o')
				#     plt.annotate(marker, (x, z), xytext=(-10, 10), textcoords='offset points', fontsize = 15)
				# Vẽ điểm LSHO
				x, y, z = coords[9]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LSHO', (x, z), xytext=(-30, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LUPA
				x, y, z = coords[10]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LUPA', (x, z), xytext=(-40, -30), textcoords='offset points', fontsize=20)
				# Vẽ điểm LELB
				x, y, z = coords[11]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LELB', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LWRA
				x, y, z = coords[12]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LWRA', (x, z), xytext=(-60, -10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LWRB
				x, y, z = coords[13]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LWRB', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LFIN
				x, y, z = coords[14]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LFIN', (x, z), xytext=(-0, -10), textcoords='offset points', fontsize=20)
				# Vẽ điểm RSHO
				x, y, z = coords[15]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RSHO', (x, z), xytext=(-30, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm RUPA
				x, y, z = coords[16]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RUPA', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RELB
				x, y, z = coords[17]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RELB', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RFRM
				x, y, z = coords[18]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RFRM', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RWRA
				x, y, z = coords[19]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RWRA', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RWRB
				x, y, z = coords[20]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RWRB', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RFIN
				x, y, z = coords[21]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RFIN', (x, z), xytext=(-10, -30), textcoords='offset points', fontsize=20)
				# Vẽ điểm LASI
				x, y, z = coords[22]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LASI', (x, z), xytext=(-50, -20), textcoords='offset points', fontsize=20)
				# Vẽ điểm RASI
				x, y, z = coords[23]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RASI', (x, z), xytext=(-40, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LPSI
				x, y, z = coords[24]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LPSI', (x, z), xytext=(-20, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm RPSI
				x, y, z = coords[25]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RPSI', (x, z), xytext=(-30, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LTHI
				x, y, z = coords[26]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LTHI', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LKNE
				x, y, z = coords[27]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LKNE', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LTIB
				x, y, z = coords[28]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LTIB', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LANK
				x, y, z = coords[29]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LANK', (x, z), xytext=(10, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm LHEE
				x, y, z = coords[30]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LHEE', (x, z), xytext=(-40, 10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LTOE
				x, y, z = coords[31]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LTOE', (x, z), xytext=(-30, -20), textcoords='offset points', fontsize=20)
				# Vẽ điểm RTHI
				x, y, z = coords[32]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RTHI', (x, z), xytext=(-50, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RKNE
				x, y, z = coords[33]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RKNE', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RTIB
				x, y, z = coords[34]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RTIB', (x, z), xytext=(-50, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RANK
				x, y, z = coords[35]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RANK', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)
				# Vẽ điểm RHEE
				x, y, z = coords[36]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RHEE', (x, z), xytext=(10, -10), textcoords='offset points', fontsize=20)
				# Vẽ điểm RTOE
				x, y, z = coords[37]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('RTOE', (x, z), xytext=(-60, -10), textcoords='offset points', fontsize=20)
				# Vẽ điểm LFRM
				x, y, z = coords[38]
				ax.scatter(x, z, color='black', marker='o')
				ax.annotate('LFRM', (x, z), xytext=(-60, 0), textcoords='offset points', fontsize=20)

				# đầu
				plt.plot([coords_dict['LFHD'][0], coords_dict['RFHD'][0]], [coords_dict['LFHD'][2], coords_dict['RFHD'][2]])
				plt.plot([coords_dict['LFHD'][0], coords_dict['LBHD'][0]], [coords_dict['LFHD'][2], coords_dict['LBHD'][2]])
				plt.plot([coords_dict['LBHD'][0], coords_dict['RBHD'][0]], [coords_dict['LBHD'][2], coords_dict['RBHD'][2]])
				plt.plot([coords_dict['RFHD'][0], coords_dict['RBHD'][0]], [coords_dict['RFHD'][2], coords_dict['RBHD'][2]])

				#cổ với ngực
				plt.plot([coords_dict['C7'][0], coords_dict['CLAV'][0]], [coords_dict['C7'][2], coords_dict['CLAV'][2]])
				plt.plot([coords_dict['CLAV'][0], coords_dict['T10'][0]], [coords_dict['CLAV'][2], coords_dict['T10'][2]])
				plt.plot([coords_dict['T10'][0], coords_dict['STRN'][0]], [coords_dict['T10'][2], coords_dict['STRN'][2]])
				plt.plot([coords_dict['STRN'][0], coords_dict['RBAK'][0]], [coords_dict['STRN'][2], coords_dict['RBAK'][2]])
				plt.plot([coords_dict['RBAK'][0], coords_dict['C7'][0]], [coords_dict['RBAK'][2], coords_dict['C7'][2]])

				#tay trai
				plt.plot([coords_dict['CLAV'][0], coords_dict['RSHO'][0]], [coords_dict['CLAV'][2], coords_dict['RSHO'][2]])
				plt.plot([coords_dict['RSHO'][0], coords_dict['RUPA'][0]], [coords_dict['RSHO'][2], coords_dict['RUPA'][2]])
				plt.plot([coords_dict['RUPA'][0], coords_dict['RELB'][0]], [coords_dict['RUPA'][2], coords_dict['RELB'][2]])
				plt.plot([coords_dict['RELB'][0], coords_dict['RFRM'][0]], [coords_dict['RELB'][2], coords_dict['RFRM'][2]])
				plt.plot([coords_dict['RFRM'][0], coords_dict['RWRA'][0]], [coords_dict['RFRM'][2], coords_dict['RWRA'][2]])
				plt.plot([coords_dict['RWRA'][0], coords_dict['RFIN'][0]], [coords_dict['RWRA'][2], coords_dict['RFIN'][2]])
				plt.plot([coords_dict['RWRA'][0], coords_dict['RWRB'][0]], [coords_dict['RWRA'][2], coords_dict['RWRB'][2]])
				plt.plot([coords_dict['RWRB'][0], coords_dict['RFIN'][0]], [coords_dict['RWRB'][2], coords_dict['RFIN'][2]])
				plt.plot([coords_dict['RWRA'][0], coords_dict['RELB'][0]], [coords_dict['RWRA'][2], coords_dict['RELB'][2]])

				# tay trái
				plt.plot([coords_dict['CLAV'][0], coords_dict['LSHO'][0]], [coords_dict['CLAV'][2], coords_dict['LSHO'][2]])
				plt.plot([coords_dict['LSHO'][0], coords_dict['LUPA'][0]], [coords_dict['LSHO'][2], coords_dict['LUPA'][2]])
				plt.plot([coords_dict['LUPA'][0], coords_dict['LELB'][0]], [coords_dict['LUPA'][2], coords_dict['LELB'][2]])
				plt.plot([coords_dict['LELB'][0], coords_dict['LFRM'][0]], [coords_dict['LELB'][2], coords_dict['LFRM'][2]])
				plt.plot([coords_dict['LFRM'][0], coords_dict['LWRA'][0]], [coords_dict['LFRM'][2], coords_dict['LWRA'][2]])
				plt.plot([coords_dict['LWRA'][0], coords_dict['LFIN'][0]], [coords_dict['LWRA'][2], coords_dict['LFIN'][2]])
				plt.plot([coords_dict['LWRA'][0], coords_dict['LWRB'][0]], [coords_dict['LWRA'][2], coords_dict['LWRB'][2]])
				plt.plot([coords_dict['LWRB'][0], coords_dict['LFIN'][0]], [coords_dict['LWRB'][2], coords_dict['LFIN'][2]])
				plt.plot([coords_dict['LWRA'][0], coords_dict['LELB'][0]], [coords_dict['LWRA'][2], coords_dict['LELB'][2]])

				#chan phai
				plt.plot([coords_dict['LPSI'][0], coords_dict['LTHI'][0]], [coords_dict['LPSI'][2], coords_dict['LTHI'][2]])
				plt.plot([coords_dict['LTHI'][0], coords_dict['LKNE'][0]], [coords_dict['LTHI'][2], coords_dict['LKNE'][2]])
				plt.plot([coords_dict['LKNE'][0], coords_dict['LTIB'][0]], [coords_dict['LKNE'][2], coords_dict['LTIB'][2]])
				plt.plot([coords_dict['LTIB'][0], coords_dict['LANK'][0]], [coords_dict['LTIB'][2], coords_dict['LANK'][2]])
				plt.plot([coords_dict['LANK'][0], coords_dict['LTOE'][0]], [coords_dict['LANK'][2], coords_dict['LTOE'][2]])
				plt.plot([coords_dict['LTOE'][0], coords_dict['LHEE'][0]], [coords_dict['LTOE'][2], coords_dict['LHEE'][2]])
				plt.plot([coords_dict['LHEE'][0], coords_dict['LANK'][0]], [coords_dict['LHEE'][2], coords_dict['LANK'][2]])
				plt.plot([coords_dict['LANK'][0], coords_dict['LKNE'][0]], [coords_dict['LANK'][2], coords_dict['LKNE'][2]])
				plt.plot([coords_dict['LKNE'][0], coords_dict['LASI'][0]], [coords_dict['LKNE'][2], coords_dict['LASI'][2]])
				plt.plot([coords_dict['LASI'][0], coords_dict['LPSI'][0]], [coords_dict['LASI'][2], coords_dict['LPSI'][2]])

				#chan TRAI
				plt.plot([coords_dict['RPSI'][0], coords_dict['RTHI'][0]], [coords_dict['RPSI'][2], coords_dict['RTHI'][2]])
				plt.plot([coords_dict['RTHI'][0], coords_dict['RKNE'][0]], [coords_dict['RTHI'][2], coords_dict['RKNE'][2]])
				plt.plot([coords_dict['RKNE'][0], coords_dict['RTIB'][0]], [coords_dict['RKNE'][2], coords_dict['RTIB'][2]])
				plt.plot([coords_dict['RTIB'][0], coords_dict['RANK'][0]], [coords_dict['RTIB'][2], coords_dict['RANK'][2]])
				plt.plot([coords_dict['RANK'][0], coords_dict['RTOE'][0]], [coords_dict['RANK'][2], coords_dict['RTOE'][2]])
				plt.plot([coords_dict['RTOE'][0], coords_dict['RHEE'][0]], [coords_dict['RTOE'][2], coords_dict['RHEE'][2]])
				plt.plot([coords_dict['RHEE'][0], coords_dict['RANK'][0]], [coords_dict['RHEE'][2], coords_dict['RANK'][2]])
				plt.plot([coords_dict['RANK'][0], coords_dict['RKNE'][0]], [coords_dict['RANK'][2], coords_dict['RKNE'][2]])
				plt.plot([coords_dict['RKNE'][0], coords_dict['RASI'][0]], [coords_dict['RKNE'][2], coords_dict['RASI'][2]])
				plt.plot([coords_dict['RASI'][0], coords_dict['RPSI'][0]], [coords_dict['RASI'][2], coords_dict['RPSI'][2]])

				# mong
				plt.plot([coords_dict['RASI'][0], coords_dict['LASI'][0]], [coords_dict['RASI'][2], coords_dict['LASI'][2]])
				plt.plot([coords_dict['RPSI'][0], coords_dict['LPSI'][0]], [coords_dict['RPSI'][2], coords_dict['LPSI'][2]])


				# Thiết lập giới hạn của trục x và y
				plt.xlim(-600, 600)
				plt.ylim(0, 2000)
				print(file)
				# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
				plt.savefig(file.replace('.txt','.jpg'))