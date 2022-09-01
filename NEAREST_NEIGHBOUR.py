import numpy as np
import cv2


class Nearest_Neighbor:
    def __init__(self, pic_des, scale= 2):
        self.pic = cv2.imread(pic_des)

        self.pic_width = self.pic.shape[0]
        self.pic_height = self.pic.shape[1]

        self.resize_pic_width = self.pic_width * scale
        self.resize_pic_height = self.pic_height * scale

        self.scale = scale

    def nn(self):
        pic_rgb = []
        rgb = 'bgr'

        for x in range(3):

            pic_channel = self.pic[:, :, x]
            pic_channel_out = np.zeros((self.resize_pic_width, self.resize_pic_height), dtype=np.uint8)

            for i in range(self.resize_pic_width):
                i_ori = (i / self.resize_pic_width) * self.pic_width
                i_interpolation = i_ori - np.floor(i_ori)

                if i_interpolation < 0.5:
                    i_int = int(np.floor(i_ori))
                else:
                    i_int = int(np.ceil(i_ori))
                    if i_int >= self.pic_width:
                        i_int = int(np.floor(i_ori))
                for j in range(self.resize_pic_height):
                    j_ori = (j / self.resize_pic_height) * self.pic_height
                    j_interpolation = j_ori - np.floor(j_ori)

                    if j_interpolation < 0.5:
                        j_int = int(np.floor(j_ori))
                    else:
                        j_int >= int(np.ceil(j_ori))

                        if j_int >= self.pic_height:
                            j_int = int(np.floor(j_ori))

                    pic_channel_out[i][j] = pic_channel[i_int][j_int]

            pic_rgb.append(pic_channel_out)
        pic_rgb_output = cv2.merge((pic_rgb[0], pic_rgb[1], pic_rgb[2]))
        print("Your Implementation has been completed for Nearest Neighbour.")
        return pic_rgb_output