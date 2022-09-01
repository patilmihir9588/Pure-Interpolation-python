from  NEAREST_NEIGHBOUR import Nearest_Neighbor
from BILINEAR import Bilinear
from BICUBIC import Bicubic
import cv2


a = cv2.imread("C:/Users/patil/PycharmProjects/pythonProject/Shelby-GT500CR.jpg")
cv2.imshow("Original", a)



Interpolation = Nearest_Neighbor(pic_des="C:/Users/patil/PycharmProjects/pythonProject/Shelby-GT500CR.jpg")
interpolated_pic_nn = Interpolation.nn()
cv2.imshow("NN Interpolated", interpolated_pic_nn )
img0 = cv2.imwrite("NN.jpg",interpolated_pic_nn )

Interpolation = Bilinear(pic_des="C:/Users/patil/PycharmProjects/pythonProject/Shelby-GT500CR.jpg")
interpolated_pic_bil = Interpolation.bilinear()
cv2.imshow("Bilinear Interpolated", interpolated_pic_bil)
img1 = cv2.imwrite("Bilinear.jpg",interpolated_pic_bil )

Interpolation = Bicubic(pic_des="C:/Users/patil/PycharmProjects/pythonProject/Shelby-GT500CR.jpg")
interpolated_pic_bic = Interpolation.bicubic()
cv2.imshow("Bicubic Interpolated", interpolated_pic_bic)
img2 = cv2.imwrite("Bicubic.jpg",interpolated_pic_bic )

cv2.waitKey(0)
cv2.destroyAllWindows()