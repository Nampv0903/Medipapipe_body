import cv2
import os

# Thư mục chứa hình ảnh đầu vào
input_dir = 'D:\VS_Code\Medipapipe_body\merged_frames'

# Thư mục để lưu video
output_dir = 'D:\VS_Code\Medipapipe_body\{}ideoOut'.format('v')

# Duyệt qua các thư mục con của input_dir
for root, dirs, files in os.walk(input_dir):
    # Sắp xếp danh sách các file theo thứ tự số trong tên file
    files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))
    for file in files:
        # Kiểm tra đuôi của file có phải là .jpg hoặc .png hay không
        if file.endswith('.jpg') or file.endswith('.png'):
            # Lấy tên thư mục chứa file
            dir_name = os.path.basename(root)
            # Tạo tên file video
            video_name = os.path.join(output_dir, dir_name + '.mp4')
            # Kiểm tra nếu file video chưa tồn tại thì tạo mới
            if not os.path.exists(video_name):
                frame = cv2.imread(os.path.join(root, file))
                height, width, _ = frame.shape
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(video_name, fourcc, 30.0, (width, height))
            # Đọc file hình ảnh
            frame = cv2.imread(os.path.join(root, file))
            # Ghi hình ảnh vào file video
            out.write(frame)

# Giải phóng bộ nhớ và đóng file video
out.release()
cv2.destroyAllWindows()
