import os


def read_pictures(read_dir):
    """
    return the file name of each picture and mask
    :param read_dir: the folder of pictures
    :return: filenames
    """
    pictures = os.listdir(read_dir[0])
    return pictures
