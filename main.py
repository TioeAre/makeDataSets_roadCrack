import readFile
import saveData

read_dir = "/home/tioeare/project/dataset/crack_segmentation_dataset"
save_dir = "/home/tioeare/project/dataset/yolo_datasets"

train_picture_dir = read_dir + "/images/train/images"
test_picture_dir = read_dir + "/images/test/images"
train_mask_dir = read_dir + "/images/train/masks"
test_mask_dir = read_dir + "/images/test/masks"

train_save_dir = save_dir + "/images/train"
test_save_dir = save_dir + "/images/test"
train_label_dir = save_dir + "/labels/train"
test_label_dir = save_dir + "/labels/test"

if __name__ == '__main__':
    train_dirs = [train_picture_dir, train_mask_dir, train_save_dir, train_label_dir]
    test_dirs = [test_picture_dir, test_mask_dir, test_save_dir, test_label_dir]

    pictures_train = readFile.read_pictures(train_dirs)
    pictures_test = readFile.read_pictures(test_dirs)

    saveData.save_image(pictures_train, train_dirs)
    saveData.save_image(pictures_test, test_dirs)
