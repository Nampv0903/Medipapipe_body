import cv2
import os

# Các đường dẫn tới các folder chứa các khung hình
folder1 = "D:\VS_Code\Medipapipe_body\{}nhCuavideo\HipHop_HipHop3".format('a')
folder2 = "D:\VS_Code\Medipapipe_body\{}rameSave\HipHop_HipHop3".format('f')

# Lấy tên của thư mục chứa ảnh trong frame_dirs
output_dir_name = os.path.basename(folder1)

# Tạo đường dẫn tới thư mục chứa ảnh merged
merged_dir = os.path.join('D:\VS_Code\Medipapipe_body\merged_frames', output_dir_name)

# Tạo list chứa tên các ảnh trong từng folder
# Tạo list chứa tên các ảnh trong từng folder
frames1 = sorted(os.listdir(folder1), key=lambda x: int(x.split(".")[0]))
frames2 = sorted(os.listdir(folder2), key=lambda x: int(x.split(".")[0]))



# Lấy kích thước của ảnh đầu tiên trong thư mục đầu tiên để sử dụng cho các ảnh khác
left_frame_path = os.path.join(folder1, frames1[0])
left_frame = cv2.imread(left_frame_path)
height, width, _ = left_frame.shape

# Tạo folder lưu ảnh merged nếu chưa có
if not os.path.exists(merged_dir):
    os.makedirs(merged_dir)

# Sắp xếp các ảnh trong folder1

# Lặp qua các file ảnh trong folder
for i, filename in enumerate(frames1):
    # Đọc ảnh từ folder
    left_frame = cv2.imread(os.path.join(folder1, filename))

    # Đọc ảnh từ folder2 tương ứng
    right_frame = cv2.imread(os.path.join(folder2, frames2[i]))

    # Resize ảnh phải về kích thước giống với ảnh trái
    right_frame = cv2.resize(right_frame, (width, height))

    # Ghép 2 ảnh lại với nhau
    merged_frame = cv2.hconcat([left_frame, right_frame])

    # Tạo path để lưu ảnh merged
    merged_path = os.path.join(merged_dir,"{}.png".format(i+1))

    # Lưu ảnh merged
    cv2.imwrite(merged_path, merged_frame)

    # In ra đường dẫn của ảnh vừa lưu
    print(merged_path)

# Giải phóng bộ nhớ và đóng các file đã mở
cv2.destroyAllWindows()
