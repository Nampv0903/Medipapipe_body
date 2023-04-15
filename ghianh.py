import cv2
import os
import mediapipe as mp

# Khởi tạo đối tượng mediapipe Pose
mp_pose = mp.solutions.pose.Pose()

# Đường dẫn đến thư mục chứa các video
video_dir = "D:\VS_Code\Medipapipe_body\{}ideo".format('v')

# Đường dẫn đến thư mục để lưu các ảnh
img_dir = "D:\VS_Code\Medipapipe_body\{}nhCuavideo".format('a')

# Lặp qua từng tệp video trong thư mục
for video_file in os.listdir(video_dir):
    # Kiểm tra xem tệp có phải là tệp video không
    if video_file.endswith(".mp4") or video_file.endswith(".avi") or video_file.endswith(".mov"):
        # Tạo một thư mục mới để lưu các ảnh từ video này
        video_name = os.path.splitext(video_file)[0]
        img_folder = os.path.join(img_dir, video_name)
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)
        
        # Tạo đối tượng VideoCapture để đọc video
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)

        # Khởi tạo biến đếm để đánh số ảnh
        count = 1

        # Lặp lại cho đến khi hết video
        while cap.isOpened():
            # Đọc một khung hình
            ret, frame = cap.read()
            if ret:
                # Phát hiện body trong ảnh bằng mediapipe pose
                results = mp_pose.process(frame)
                if results.pose_landmarks is not None:
                    # Lưu ảnh với tên tương ứng vào thư mục
                    img_path = os.path.join(img_folder, "{:d}.jpg".format(count))
                    cv2.imwrite(img_path, frame)
                    print(img_path)
                    count += 1
            else:
                break

        # Giải phóng bộ nhớ và đóng tệp video
        cap.release()
        cv2.destroyAllWindows()
