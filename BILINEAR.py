import numpy as np
import cv2

class Bilinear:
    def __init__(self, pic_des, scale=2):
        self.pic = cv2.imread(pic_des)

        self.pic_width = self.pic.shape[0]
        self.pic_height = self.pic.shape[1]

        self.resize_pic_width = self.pic_width * scale
        self.resize_pic_height = self.pic_height * scale

        self.scale = scale

    def bilinear(self):



        pic_rgb = []

        rgb = "bgr"

        m = np.array([[0, 1], [1, 1]])
        m_inv = np.linalg.inv(m)

        for x in range(3):

            pic_channel = self.pic[:, :, x]

            pic_channel_output = np.zeros((self.resize_pic_width, self.resize_pic_height), dtype=np.uint8)

            bottom_row = pic_channel[-1, :]
            pic_row_padding = np.vstack((pic_channel, bottom_row))

            rightmost_column = pic_row_padding[:, -1]
            image_padding = np.c_[pic_row_padding, rightmost_column]

            F = np.zeros((self.pic_width, self.pic_height, 2, 2))

            for i in range(self.pic_width):
                for j in range(self.pic_height):
                    f = np.array([[image_padding[i][j], image_padding[i][j + 1]],
                                  [image_padding[i + 1][j], image_padding[i + 1][j + 1]]])
                    F[i][j] = f


            for i in range(self.resize_pic_width):

                i_ori = (i / self.resize_pic_width) * self.pic_width

                i_interp = i_ori - np.floor(i_ori)

                i_int = int(np.floor(i_ori))

                for j in range(self.resize_pic_height):

                    j_ori = (j / self.resize_pic_height) * self.pic_height

                    j_interp = j_ori - np.floor(j_ori)

                    j_int = int(np.floor(j_ori))

                    if i_interp == 0.0 and j_interp == 0.0:

                        pic_channel_output[i][j] = pic_channel[int(i_ori)][int(j_ori)]
                    else:
                        I = np.expand_dims(np.array([i_interp ** 1, i_interp ** 0]), axis=0)
                        J = np.expand_dims(np.array([j_interp ** 1, j_interp ** 0]), axis=1)
                        F_interp = F[i_int][j_int]

                        interpolated_value = I.dot(m_inv).dot(F_interp).dot(m_inv).dot(J)

                        if interpolated_value < 0:
                            interpolated_value = 0
                        elif interpolated_value > 255:
                            interpolated_value = 255

                        pic_channel_output[i][j] = interpolated_value

            pic_rgb.append(pic_channel_output)

        image_rgb_output = cv2.merge((pic_rgb[0], pic_rgb[1], pic_rgb[2]))

        print("Your Implementation has been completed for Bilinear.")


        return image_rgb_output