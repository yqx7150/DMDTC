
import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.io as sio

images = []
masks = []

for i in range(0,20):
    img_path = rf"\DMDTC\Code\Time_domain_compression\fft\magnitudes_{i}.png"
    mask_path = rf"\DMDTC\Code\Time_domain_compression\mask\mask_{i}.bmp"

    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)  # Load image
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)  # Load mask

    images.append(img)
    masks.append(mask)


images = np.array(images, dtype=np.float32)
masks = np.array(masks, dtype=np.float32)


images = images/255
masks = masks/255

# under-sampling
compressed_image = np.sum(images * masks, axis=0)


# compressed_image *= 255
compressed_image = compressed_image.astype(np.float64)

# save the compressed image
cv2.imwrite(r"\DMDTC\Code\Time_domain_compression\compressed_image.jpg", compressed_image)
plt.imshow(compressed_image, cmap='gray')
plt.show()
meas = np.stack((compressed_image, compressed_image), axis=2)
data = {'meas': meas}


# save as .mat file
output_path = r'\DMDTC\Code\Time_domain_compression\meas.mat'
sio.savemat(output_path, data)
