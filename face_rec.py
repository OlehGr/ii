import shutil

import dlib
from skimage import io
from scipy.spatial import distance
import os
from random import randint
from collections import Counter
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('user_photo') if isfile(join('user_photo', f))]

def len_dir():
    directory = 'frame/'
    files = os.listdir(directory)
    return len(files)


def face_comparison():

    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()

    # 3arpyxaem nepsyw doTorpadnio
    for i in onlyfiles:
        print(i)
        img = io.imread(f"user_photo/{i}")

        # Moka3bisaem doTorpaduio cpeactBamu dlib

        dets = detector(img, 1)

        for k, d in enumerate(dets):
            shape = sp(img, d)

        # Vi3BNeKkKaem AecKpwnTop v3 Anya
        face_descriptor1 = facerec.compute_face_descriptor(img, shape)

        random_number = randint(1, len_dir())
        img = io.imread(f'frame/Frame_{random_number}.jpg')
        dets_webcam = detector(img, 1)

        for k, d in enumerate(dets_webcam):
            shape = sp(img, d)

        face_descriptor2 = facerec.compute_face_descriptor(img, shape)

        a = distance.euclidean(face_descriptor1, face_descriptor2)

        if a < 0.6:
            return [True, i]
            break
        else:
            pass


