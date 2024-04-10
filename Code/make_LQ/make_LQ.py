
import os
import cv2

def process_images(input_folder, mask_folder, output_folder):
    # get picture list
    image_files = os.listdir(input_folder)
    # get mask list
    mask_files = os.listdir(mask_folder)

    # number of the images
    num_images = len(image_files)

    for i in range(num_images):
        # if gray image
        image_file = image_files[i]
        # if not image_file.endswith('.png'):
        #     continue


        mask_file = mask_files[i % len(mask_files)]
        mask_path = os.path.join(mask_folder, mask_file)


        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # CS process
        processed_image = cv2.bitwise_and(image, mask)

        # transform to uint8
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, processed_image.astype('uint8'))


# 定义文件夹路径
input_folder = r'\DMDTC\Code\Time_domain_unfolding\recon'
mask_folder = r'\DMDTC\Code\make_LQ\mask'
output_folder = r'\DMDTC\Code\make_LQ\TEST-LQ'

# 调用函数进行处理
process_images(input_folder, mask_folder, output_folder)