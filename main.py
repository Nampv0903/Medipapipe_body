import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageDraw

import math
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

video_dir = 'D:\VS_Code\Medipapipe_body\{}ideo'.format('v')
image_dir = 'D:\VS_Code\Medipapipe_body\{}rameSave'.format('f')
video_saved_dir = 'D:\VS_Code\Medipapipe_body\{}ideoOut'.format('v')



for filename in os.listdir(video_dir):
    if filename.endswith(".mp4"):
        # Đường dẫn đến video
        video_path = os.path.join(video_dir, filename)
        
        # Tạo thư mục tên là tên video để lưu các khung hình
        video_name = os.path.splitext(filename)[0]
        frame_dir = os.path.join(image_dir, video_name)
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)
            print(frame_dir)

    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
        cap = cv2.VideoCapture(video_path)
        count = 1
        total_dis_lwrist = 0
        total_dis_rwrist = 0
        total_dis_lelbow = 0
        total_dis_relbow = 0
        total_dis_lknee = 0
        total_dis_rknee = 0
        total_dis_lankle = 0
        total_dis_rankle = 0
        while True:
            success, image = cap.read()
            if not success:
                break

            image_height, image_width, _ = image.shape

            # Convert BGR image to RGB before processing
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Run pose estimation model
            results = pose.process(image)
            results_next = pose.process(image+1)
            if results.pose_world_landmarks is None:
                continue
            # Draw pose landmarks on the image
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            
            # Plot 3D world landmarks using Matplotlib
            # Plot 3D world landmarks using Matplotlib
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.tick_params(axis='both', which='major', labelsize=7, pad=1)
            for i, connection in enumerate(mp_pose.POSE_CONNECTIONS):
                x1 = results.pose_world_landmarks.landmark[connection[0]].x
                y1 = results.pose_world_landmarks.landmark[connection[0]].y
                z1 = results.pose_world_landmarks.landmark[connection[0]].z
                x2 = results.pose_world_landmarks.landmark[connection[1]].x
                y2 = results.pose_world_landmarks.landmark[connection[1]].y
                z2 = results.pose_world_landmarks.landmark[connection[1]].z

                x_shoulder_mid = (results.pose_world_landmarks.landmark[11].x + results.pose_world_landmarks.landmark[12].x) / 2
                y_shoulder_mid = (-results.pose_world_landmarks.landmark[11].y - results.pose_world_landmarks.landmark[12].y) / 2
                z_shoulder_mid = (-results.pose_world_landmarks.landmark[11].z - results.pose_world_landmarks.landmark[12].z) / 2

                x_neck = results.pose_world_landmarks.landmark[0].x
                y_neck = -results.pose_world_landmarks.landmark[0].y
                z_neck = -results.pose_world_landmarks.landmark[0].z

                ax.plot([x_neck, x_shoulder_mid], [y_neck, y_shoulder_mid], [z_neck, z_shoulder_mid], c='black')

                ax.scatter(x_neck, y_neck, z_neck, c='red', s=10)
                ax.scatter(x_shoulder_mid,y_shoulder_mid,z_shoulder_mid,c='red', s=10)

                ax.plot([x1, x2], [-y1, -y2], [-z1, -z2], c='black')

            for landmark in results.pose_world_landmarks.landmark:
                x = landmark.x
                y = -landmark.y
                z = -landmark.z
                ax.scatter(x, y, z, c='red', s=10)
            
            if results_next.pose_world_landmarks:
                            # Lưu trữ tọa độ trong khung hình hiện tại
                x1_lwrist = results.pose_world_landmarks.landmark[13].x
                y1_lwrist = -results.pose_world_landmarks.landmark[13].y
                z1_lwrist = -results.pose_world_landmarks.landmark[13].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_lwrist = results_next.pose_world_landmarks.landmark[13].x
                y2_lwrist = -results_next.pose_world_landmarks.landmark[13].y
                z2_lwrist = -results_next.pose_world_landmarks.landmark[13].z
                # Tính khoảng cách giữa hai tọa độ
                distance_lw = ((x2_lwrist - x1_lwrist)**2 + (y2_lwrist - y1_lwrist)**2 + (z2_lwrist - z1_lwrist)**2)**0.5
                total_dis_lwrist = total_dis_lwrist + distance_lw
                ax.text(results.pose_world_landmarks.landmark[13].x + 0.02, -results.pose_world_landmarks.landmark[13].y + 0.02, -results.pose_world_landmarks.landmark[13].z, "l wrist: {}".format(round(total_dis_rwrist, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue



            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_rwrist = results.pose_world_landmarks.landmark[14].x
                y1_rwrist = -results.pose_world_landmarks.landmark[14].y
                z1_rwrist = -results.pose_world_landmarks.landmark[14].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_rwrist = results_next.pose_world_landmarks.landmark[14].x
                y2_rwrist = -results_next.pose_world_landmarks.landmark[14].y
                z2_rwrist = -results_next.pose_world_landmarks.landmark[14].z
                # Tính khoảng cách giữa hai tọa độ
                distance_rw = ((x2_rwrist - x1_rwrist)**2 + (y2_rwrist - y1_rwrist)**2 + (z2_rwrist - z1_rwrist)**2)**0.5
                total_dis_rwrist = total_dis_rwrist + distance_rw
                ax.text(results.pose_world_landmarks.landmark[14].x - 0.35, -results.pose_world_landmarks.landmark[14].y + 0.02, -results.pose_world_landmarks.landmark[14].z, "r wrist: {}".format(round(total_dis_rwrist, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue

            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_lelbow = results.pose_world_landmarks.landmark[15].x
                y1_lelbow = -results.pose_world_landmarks.landmark[15].y
                z1_lelbow = -results.pose_world_landmarks.landmark[15].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_lelbow = results_next.pose_world_landmarks.landmark[15].x
                y2_lelbow = -results_next.pose_world_landmarks.landmark[15].y
                z2_lelbow = -results_next.pose_world_landmarks.landmark[15].z
                # Tính khoảng cách giữa hai tọa độ
                distance_le = ((x2_lelbow - x1_lelbow)**2 + (y2_lelbow - y1_lelbow)**2 + (z2_lelbow - z1_lelbow)**2)**0.5
                total_dis_lelbow = total_dis_lelbow + distance_le
                ax.text(results.pose_world_landmarks.landmark[15].x + 0.02, -results.pose_world_landmarks.landmark[15].y + 0.02, -results.pose_world_landmarks.landmark[15].z, "l elbow: {}".format(round(total_dis_lelbow, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_relbow = results.pose_world_landmarks.landmark[16].x
                y1_relbow = -results.pose_world_landmarks.landmark[16].y
                z1_relbow = -results.pose_world_landmarks.landmark[16].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_relbow = results_next.pose_world_landmarks.landmark[16].x
                y2_relbow = -results_next.pose_world_landmarks.landmark[16].y
                z2_relbow = -results_next.pose_world_landmarks.landmark[16].z
                # Tính khoảng cách giữa hai tọa độ
                distance_re = ((x2_relbow - x1_relbow)**2 + (y2_relbow - y1_relbow)**2 + (z2_relbow - z1_relbow)**2)**0.5
                total_dis_relbow = total_dis_relbow + distance_re
                ax.text(results.pose_world_landmarks.landmark[16].x - 0.35, -results.pose_world_landmarks.landmark[16].y + 0.02, -results.pose_world_landmarks.landmark[16].z, "r elbow: {}".format(round(total_dis_relbow, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_lknee = results.pose_world_landmarks.landmark[25].x
                y1_lknee = -results.poseh_world_landmarks.landmark[25].y
                z1_lknee = -results.pose_world_landmarks.landmark[25].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_lknee = results_next.pose_world_landmarks.landmark[25].x
                y2_lknee = -results_next.pose_world_landmarks.landmark[25].y
                z2_lknee = -results_next.pose_world_landmarks.landmark[25].z
                # Tính khoảng cách giữa hai tọa độ
                distance_lk = ((x2_lknee - x1_lknee)**2 + (y2_lknee - y1_lknee)**2 + (z2_lknee - z1_lknee)**2)**0.5
                total_dis_lknee = total_dis_lknee + distance_lk
                ax.text(results.pose_world_landmarks.landmark[25].x + 0.02, -results.pose_world_landmarks.landmark[25].y + 0.02, -results.pose_world_landmarks.landmark[25].z, "l knee: {}".format(round(total_dis_lknee, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_rknee = results.pose_world_landmarks.landmark[26].x
                y1_rknee = -results.pose_world_landmarks.landmark[26].y
                z1_rknee = -results.pose_world_landmarks.landmark[26].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_rknee = results_next.pose_world_landmarks.landmark[26].x
                y2_rknee = -results_next.pose_world_landmarks.landmark[26].y
                z2_rknee = -results_next.pose_world_landmarks.landmark[26].z
                # Tính khoảng cách giữa hai tọa độ
                distance_rk = ((x2_rknee - x1_rknee)**2 + (y2_rknee - y1_rknee)**2 + (z2_rknee - z1_rknee)**2)**0.5
                total_dis_rknee = total_dis_rknee + distance_rk
                ax.text(results.pose_world_landmarks.landmark[26].x - 0.35, -results.pose_world_landmarks.landmark[26].y + 0.02, -results.pose_world_landmarks.landmark[26].z, "r knee: {}".format(round(total_dis_rknee, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_lankle = results.pose_world_landmarks.landmark[27].x
                y1_lankle = -results.pose_world_landmarks.landmark[27].y
                z1_lankle = -results.pose_world_landmarks.landmark[27].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_lankle = results_next.pose_world_landmarks.landmark[27].x
                y2_lankle = -results_next.pose_world_landmarks.landmark[27].y
                z2_lankle = -results_next.pose_world_landmarks.landmark[27].z
                # Tính khoảng cách giữa hai tọa độ
                distance_la = ((x2_lankle - x1_lankle)**2 + (y2_lankle - y1_lankle)**2 + (z2_lankle - z1_lankle)**2)**0.5
                total_dis_lankle = total_dis_lankle + distance_la
                ax.text(results.pose_world_landmarks.landmark[27].x + 0.02, -results.pose_world_landmarks.landmark[27].y + 0.02, -results.pose_world_landmarks.landmark[27].z, "l ankle: {}".format(round(total_dis_lankle, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            if results_next.pose_world_landmarks:
                # Lưu trữ tọa độ trong khung hình hiện tại
                x1_rankle = results.pose_world_landmarks.landmark[28].x
                y1_rankle = -results.pose_world_landmarks.landmark[28].y
                z1_rankle = -results.pose_world_landmarks.landmark[28].z
                # Lưu trữ tọa độ trong khung hình tiếp theo
                x2_rankle = results_next.pose_world_landmarks.landmark[28].x
                y2_rankle = -results_next.pose_world_landmarks.landmark[28].y
                z2_rankle = -results_next.pose_world_landmarks.landmark[28].z
                # Tính khoảng cách giữa hai tọa độ
                distance_ra = ((x2_rankle - x1_rankle)**2 + (y2_rankle - y1_rankle)**2 + (z2_rankle - z1_rankle)**2)**0.5
                total_dis_rankle = total_dis_rankle + distance_ra
                ax.text(results.pose_world_landmarks.landmark[28].x - 0.35, -results.pose_world_landmarks.landmark[28].y + 0.02, -results.pose_world_landmarks.landmark[28].z, "r ankle: {}".format(round(total_dis_rankle, 2)), color='green', fontsize=6, weight='bold', zorder=15)
            else:
                continue
            new_video_name = "_".join(video_name.split("_")[:-1])
            ax.text(results.pose_world_landmarks.landmark[5].x - 0.08, -results.pose_world_landmarks.landmark[5].y + 0.12, -results.pose_world_landmarks.landmark[15].z, "{}".format(new_video_name), fontsize=7, weight='bold', color='black')

            # Set the viewpoint of the 3D plot
            ax.view_init(elev=110., azim=-90.)  # xoay góc nhìn để đặt trục x ở dưới, trục y bên trái
            ax.set_xlim3d([-0.6, 0.6])  # giới hạn trục x
            ax.set_ylim3d([-0.9, 0.8])  # giới hạn trục y
            ax.set_zlim3d([-0.8, 0.8])  # giới hạn trục z và định vị lại vị trí của trục z
   
            
            # Save the plot to an image file
            frame_path = os.path.join(frame_dir, f"{count}.png")
            plt.savefig(frame_path, bbox_inches='tight', pad_inches=0, dpi=200)
            count += 1  # Tăng giá trị biến đếm lên 1
            print(frame_path)
            plt.close()


    cap.release()
    cv2.destroyAllWindows()


