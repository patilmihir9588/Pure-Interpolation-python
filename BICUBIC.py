import numpy as np
import cv2

class Bicubic:
    def __init__(self, pic_des, scale=2):
        self.pic = cv2.imread(pic_des)

        self.pic_width = self.pic.shape[0]
        self.pic_height = self.pic.shape[1]

        self.resized_pic_width = self.pic_width * scale
        self.resized_pic_height = self.pic_height * scale

        self.scale = scale

    def bicubic(self):

        pic_rgb = []
        m = np.array([[-1, 1, -1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [8, 4, 2, 1]])
        m_inv = np.linalg.inv(m)
        m_inv_T = m_inv.T

        rgb = "bgr"
        for x in range(3):

            pic_channel = self.pic[:, :, x]

            pic_channel_output = np.zeros((self.resized_pic_width, self.resized_pic_height), dtype=np.uint8)

            top_row = pic_channel[0, :]
            bottom_row = pic_channel[-1, :]
            pic_row_padding = np.vstack((top_row, pic_channel))
            pic_row_padding = np.vstack((pic_row_padding, bottom_row))
            pic_row_padding = np.vstack((pic_row_padding, bottom_row))

            leftmost_column = pic_row_padding[:, 0]
            rightmost_column = pic_row_padding[:, -1]
            pic_padding = np.c_[leftmost_column, pic_row_padding, rightmost_column, rightmost_column]

            F = np.zeros((self.pic_width, self.pic_height, 4, 4))

            for i in range(self.pic_width):
                i_padding = i + 1
                for j in range(self.pic_height):
                    j_padding = j + 1

                    f = np.array([[pic_padding[i_padding - 1][j_padding - 1], pic_padding[i_padding - 1][j_padding],
                                   pic_padding[i_padding - 1][j_padding + 1],
                                   pic_padding[i_padding - 1][j_padding + 2]],
                                  [pic_padding[i_padding][j_padding - 1], pic_padding[i_padding][j_padding],
                                   pic_padding[i_padding][j_padding + 1], pic_padding[i_padding][j_padding + 2]],
                                  [pic_padding[i_padding + 1][j_padding - 1], pic_padding[i_padding + 1][j_padding],
                                   pic_padding[i_padding + 1][j_padding + 1],
                                   pic_padding[i_padding + 1][j_padding + 2]],
                                  [pic_padding[i_padding + 2][j_padding - 1], pic_padding[i_padding + 2][j_padding],
                                   pic_padding[i_padding + 2][j_padding + 1],
                                   pic_padding[i_padding + 2][j_padding + 2]]])

                    F[i][j] = f

            for i in range(self.resized_pic_width):

                i_ori = (i / self.resized_pic_width) * self.pic_width

                i_interp = i_ori - np.floor(i_ori)

                i_int = int(np.floor(i_ori))

                for j in range(self.resized_pic_height):

                    j_ori = (j / self.resized_pic_height) * self.pic_height


                    j_interp = j_ori - np.floor(j_ori)

                    j_int = int(np.floor(j_ori))

                    if j_interp == 0.0 and j_interp == 0.0:

                        pic_channel_output[i][j] = pic_channel[int(i_ori)][int(j_ori)]
                    else:
                        I = np.expand_dims(np.array([i_interp ** 3, i_interp ** 2, i_interp ** 1, i_interp ** 0]), axis=0)

                        J = np.expand_dims(np.array([j_interp ** 3, j_interp ** 2, j_interp ** 1, j_interp ** 0]), axis=1)

                        F_interp = F[i_int][j_int]

                        interpolated_value = I.dot(m_inv).dot(F_interp).dot(m_inv_T).dot(J)
                        if interpolated_value < 0:
                            interpolated_value = 0
                        elif interpolated_value > 255:
                            interpolated_value = 255

                        pic_channel_output[i][j] = interpolated_value

            pic_rgb.append(pic_channel_output)

        pic_rgb_output = cv2.merge((pic_rgb[0], pic_rgb[1], pic_rgb[2]))
        print("Your Implementation has been completed for Bicubic.")

        return pic_rgb_output