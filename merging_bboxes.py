import sys

import torch
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import combinations


def combineBoundingBox(box1, box2):
    """
    :param box1:
    :param box2:
    :return: max value of first two points and minimum value of the second two points
    """
    x = max(box1[0], box2[0])
    y = max(box1[1], box2[1])
    w = min(box1[2], box2[2])
    h = min(box1[3], box2[3])
    return (x, y, w, h)

def union_xywh(a, b):
    x = min(a[0], b[0])
    y = min(a[1], b[1])
    w = max(a[0] + a[2], b[0] + b[2]) - x
    h = max(a[1] + a[3], b[1] + b[3]) - y
    return (x, y, w, h)


def union_x1y1x2y2(a, b):
    x1 = min(a[0], b[0])
    y1 = min(a[1], b[1])
    x2 = max(a[2], b[2])
    y2 = max(a[3], b[3])
    return (x1, y1, x2, y2)


def xywh2xyxy(x):
    y = x.new(x.shape)
    y[..., 0] = x[..., 0] - x[..., 2] / 2
    y[..., 1] = x[..., 1] - x[..., 3] / 2
    y[..., 2] = x[..., 0] + x[..., 2] / 2
    y[..., 3] = x[..., 1] + x[..., 3] / 2
    return y


def bbox_iou(box1, box2, x1y1x2y2=True):
    # box1, box2 =  np.array(box1), np.array(box2)
    """
    Returns the IoU of two bounding boxes
    """
    if not x1y1x2y2:
        # Transform from center and width to exact coordinates
        b1_x1, b1_x2 = box1[0] - box1[2] / 2, box1[0] + box1[2] / 2
        b1_y1, b1_y2 = box1[1] - box1[3] / 2, box1[1] + box1[3] / 2
        b2_x1, b2_x2 = box2[0] - box2[2] / 2, box2[0] + box2[2] / 2
        b2_y1, b2_y2 = box2[1] - box2[3] / 2, box2[1] + box2[3] / 2
    else:
        # Get the coordinates of bounding boxes
        b1_x1, b1_y1, b1_x2, b1_y2 = box1[0], box1[1], box1[2], box1[3]
        b2_x1, b2_y1, b2_x2, b2_y2 = box2[0], box2[1], box2[2], box2[3]

    # get the corrdinates of the intersection rectangle
    inter_rect_x1 = torch.max(b1_x1, b2_x1)
    inter_rect_y1 = torch.max(b1_y1, b2_y1)
    inter_rect_x2 = torch.min(b1_x2, b2_x2)
    inter_rect_y2 = torch.min(b1_y2, b2_y2)
    # Intersection area
    inter_area = torch.clamp(inter_rect_x2 - inter_rect_x1 + 1, min=0) * torch.clamp(
        inter_rect_y2 - inter_rect_y1 + 1, min=0
    )
    # Union Area
    # inter_area = np.array(inter_area)

    b1_area = (b1_x2 - b1_x1 + 1) * (b1_y2 - b1_y1 + 1)
    b2_area = (b2_x2 - b2_x1 + 1) * (b2_y2 - b2_y1 + 1)

    print(b1_area, b2_area)
    iou = float(np.array(inter_area) / np.array(b1_area + b2_area - inter_area + 1e-16))
    print("###### -->", inter_area, iou, (b1_area + b2_area - inter_area + 1e-16))
    return iou


def non_max_suppression(prediction=None, conf_thres=0.5, nms_thres=0.4):
    prediction = np.array([[200, 200, 100, 100], [150, 250, 100, 100], [400, 300, 250, 150]])
    img = '/Users/ioneliabuzatu/Desktop/happy_email.png'

    img_read = cv2.imread(img)
    # print(img_read)
    # cv2.rectangle(image, start_point, end_point, color, thickness)

    for box in prediction:
        col = random.randint(0, 255)

        cv2.rectangle(img_read, (box[0], box[1]), (box[2], box[3]), color=(col, 255, col), thickness=5)
    # cv2.rectangle(img_read, (150,250), (100,100), color=(0,255,0))

    # From (center x, center y, width, height) to (x1, y1, x2, y2)
    prediction = torch.tensor(prediction)
    # prediction[..., :4] = xywh2xyxy(prediction[..., :4])
    # print("HERE:")
    # print(prediction)
    all_combinations = combinations(prediction, 2)
    # print(all_combinations)

    for i in all_combinations:
        print(i[0], i[1])
        iou = bbox_iou(i[0], i[1], x1y1x2y2=False)
        if iou > 0.1:
            union_overlap = union_x1y1x2y2(i[0], i[1])
            union_overlap_ = union_xywh(i[0], i[1])
            combine_union = combineBoundingBox(i[0],i[1])
            x1, y1, w, h = combine_union
            # w = x2-x1
            # h=y2-y1
            cv2.rectangle(img_read, (x1,y1), (w,h), color=(0,255,0))
            print("iou is greater than 0.1 -->", combine_union)
            print(union_overlap_)
            # append new bbox
        else:
            print("iou is less than 0.1")
            # append or remove current box
        # print(iou)

    plt.imshow(img_read)
    plt.show()

    sys.exit()
    output = [None for _ in range(len(prediction))]
    for image_i, image_pred in enumerate(prediction):
        #     Filter out confidence scores below threshold
        # image_pred = image_pred[image_pred[:, 4] >= conf_thres]
        # If none are remaining => process next image
        # if not image_pred.size(0):
        #     continue
        # Object confidence times class confidence
        # score = image_pred[:, 4] * image_pred[:, 5:].max(1)[0]
        # Sort by it
        # image_pred = image_pred[(-score).argsort()]
        # class_confs, class_preds = image_pred[:, 5:].max(1, keepdim=True)
        # detections = torch.cat((image_pred[:, :5], class_confs.float(), class_preds.float()), 1)
        # Perform non-maximum suppression
        keep_boxes = []
        detections = prediction
        large_overlap = bbox_iou(detections[0, :4].unsqueeze(0), detections[:, :4]) > nms_thres
        print(large_overlap)
        while detections.size(0):
            large_overlap = bbox_iou(detections[0, :4].unsqueeze(0), detections[:, :4]) > nms_thres
            # print("large_overlap", large_overlap)
            #     label_match = detections[0, -1] == detections[:, -1]
            #     Indices of boxes with lower confidence scores, large IOUs and matching labels
            invalid = large_overlap
            # print("invalid ", invalid)
            weights = detections[invalid]
            # print(weights)
            # Merge overlapping bboxes by order of confidence
            detections[0, :4] = (weights * detections[invalid, :4]).sum(0) / weights.sum()
            keep_boxes += [detections[0]]
            detections = detections[~invalid]
        if keep_boxes:
            output[image_i] = torch.stack(keep_boxes)

    # print('output ', output)
    return output


non_max_suppression()
