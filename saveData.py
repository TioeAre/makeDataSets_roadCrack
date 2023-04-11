import os
import cv2

height = 640
width = 640


def save_image(pictures, dirs):
    for i in range(len(pictures)):
        print("processing " + str(i + 1) + " :" + pictures[i] + " \t--- " + str(i + 1) + "/" + str(len(pictures)) + "\n")
        picture = dirs[0] + "/" + pictures[i]
        mask = dirs[1] + "/" + pictures[i]
        if os.path.isfile(picture) and os.path.isfile(mask):
            id = classify(pictures[i])  # crack Classes in crack.yaml
            if id == 0:
                continue
            road_crack_mat = cv2.imread(picture, cv2.IMREAD_COLOR)
            mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)
            road_crack_mat = cv2.resize(road_crack_mat, (width, height))
            mask = cv2.resize(mask, (width, height))

            new_name = "%05d" % (i + 1)  # rename the picture by numbers
            cv2.imwrite(dirs[2] + "/" + new_name + ".jpg", road_crack_mat)

            contours, if_empty = find_contours(mask)
            if if_empty:
                continue
            write_labels(contours, dirs[3], new_name, id)
        i = i+1


def classify(filename):
    filename_split = filename.split("_", 1)
    if filename_split[0] == "noncrack":
        return 0
    elif filename_split[0] == "CRACK500":
        return 1
    elif filename_split[0] == "cracktree200":
        return 2
    elif filename_split[0] == "DeepCrack":
        return 3
    elif filename_split[0] == "Eugen":
        return 4
    elif filename_split[0] == "forest":
        return 5
    elif filename_split[0] == "GAPS384":
        return 6
    elif filename_split[0] == "CFD":
        return 7
    elif filename_split[0] == "Rissbilder":
        return 8
    elif filename_split[0] == "Sylvie":
        return 9
    elif filename_split[0] == "Volker":
        return 10


def find_contours(mask):
    """
    return contours
    :param mask: mask mat
    :return: contours of crack, does the mat have crack
    """
    ret, thresh = cv2.threshold(mask, 1, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cracks = [[]]
    crack = []
    if_empty = True
    if hierarchy is None:
        return cracks, if_empty
    for i in range(len(hierarchy[0])):
        if hierarchy[0][i][3] == -1:    # 没有父轮廓
            crack = cv2.approxPolyDP(contours[i], 10, True)
            cracks.append(crack)
    if len(cracks) != 0:
        if_empty = False
    return cracks, if_empty


def write_labels(contours, dir, filename, id):
    with open(dir + "/" + filename + ".txt", "w") as f:
        for contour in contours:
            if len(contour) < 5:
                continue
            f.write(str(id))
            for position in contour:
                f.write(" " + str(position[0][0] / width) + " " + str(position[0][1] / height))
            f.write("\n")