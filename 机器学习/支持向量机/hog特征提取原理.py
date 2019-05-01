import cv2
import numpy as np

img=cv2.imread('E:/face/person.png',cv2.IMREAD_GRAYSCALE)
img=np.sqrt(img/np.max(img))

#计算梯度
height,width=img.shape
gradient_values_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
gradient_values_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
gradient_magnitude=np.abs(gradient_values_x)+np.abs(gradient_values_y)
gradient_angle=cv2.phase(gradient_values_x,gradient_values_y,angleInDegrees=True)
#plt.hist(grdient_angle.ravel(),256,[0,256])
#plt.show()
# cv2.imshow('image',img)
# cv2.imwrite("Image-test.jpg", img)
# cv2.waitKey(0)

cell_size=8
bin_size=9
angle_unit=180/bin_size
cell_gradient_vector=np.zeros((int(height / cell_size), int(width / cell_size),
                                int(bin_size)))

def cell_gradient(cell_magnitude,cell_angle):
    orientation_centers=np.zeros(bin_size)
    for i in range(cell_magnitude.shape[0]):
        for j in range(cell_magnitude.shape[0]):
            min_angle=int(cell_angle[i][j]/angle_unit)%bin_size
            max_angle=(min_angle+1)%bin_size
            mod=cell_angle[i][j] % angle_unit
            orientation_centers[min_angle]+=cell_magnitude[i][j]*(1-(mod/angle_unit))
            orientation_centers[max_angle]+=cell_magnitude[i][j]*(mod/angle_unit)
    return orientation_centers

for i in range(cell_gradient_vector.shape[0]):
    for j in range(cell_gradient_vector.shape[1]):
        cell_magnitude=gradient_magnitude[i*cell_size:(i+1)*cell_size,
                       j*cell_size:(j+1)*cell_size]
        cell_angle = gradient_angle[i * cell_size:(i + 1) * cell_size,
                     j * cell_size:(j + 1) * cell_size]
        cell_gradient_vector[i][j]=cell_gradient(cell_magnitude,cell_angle)
#print(cell_gradient_vector.shape)

hog_vector=[]
for i in range(cell_gradient_vector.shape[0]-1):
    for j in range(cell_gradient_vector.shape[1] - 1):
        block_vector=[]
        block_vector.extend(cell_gradient_vector[i][j])
        block_vector.extend(cell_gradient_vector[i][j+1])
        block_vector.extend(cell_gradient_vector[i+1][j])
        block_vector.extend(cell_gradient_vector[i+1][j+1])
        mag=lambda vector:np.sqrt(sum(i**2 for i in vector))
        magnitude=mag(block_vector)
        if magnitude != 0:
            normalize=lambda block_vector,magnitude:[element/magnitude for element in block_vector]
            block_vector=normalize(block_vector,magnitude)
        hog_vector.extend(block_vector)
print(np.array(hog_vector))