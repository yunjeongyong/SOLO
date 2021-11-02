import os
import glob
import numpy as np

import cv2
import json
from PIL import Image


class PlenopticDataLoader:
    def __init__(self, root, img2d_ref, focal_range=None):
        self.root = root
        self.img2d_ref = img2d_ref
        self.focal_range = focal_range

    def dataLoader_focal(self):
        self.img2d_files = []
        self.focal_files = []
        frames = os.listdir(self.root)
        for frame in frames:
            img2d_file = os.path.join(os.path.join(
                self.root, frame), self.img2d_ref)
            focal_path = os.path.join(os.path.join(self.root, frame), 'focal')
            focal_planes = glob.glob(glob.escape(focal_path) + "/*")
            if self.focal_range is None:
                pass
            else:
                focal_planes = focal_planes[self.focal_range[0]
                    :self.focal_range[1] + 1]
            self.img2d_files.append(img2d_file)
            self.focal_files.append(focal_planes)
        return self.img2d_files, self.focal_files

    def dataLoader_2d(self):
        self.img2d_files = []
        frames = os.listdir(self.root)
        for frame in frames:
            img2d_file = os.path.join(os.path.join(
                self.root, frame), self.img2d_ref)
            self.img2d_files.append(img2d_file)
        return self.img2d_files


def get_frames():
    video_name = 'C:\\Users\\hansung\\Desktop\\intern_code\\PlenOpticVot_SiamRPN++\\save_else\\captured\\Set3.mp4'
    start_num, last_num = 20, 50
    dataLoader_focal = PlenopticDataLoader(
        root=video_name, img2d_ref='images/005.png', focal_range=(start_num, last_num))
    img2d_files = dataLoader_focal.dataLoader_2d()
    # for i in range(len(img2d_files)):
    # for img2d_file in img2d_files:
    #     frame_bgr = cv2.imread(img2d_file)
    #     frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    #     yield frame_bgr, frame_rgb
    for i in range(0, len(img2d_files), 5):
        frame_bgr = cv2.imread(img2d_files[i])
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        yield frame_bgr, frame_rgb

