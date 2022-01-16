# -*- coding: utf-8 -*-
"""
Created on Sat 12 18 21:29:16 2021

@author: MDM
"""
# Ref: https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/

# import the necessary packages
import time
import cv2
import pathlib as pl


def dhash(image, hashSize=8):
    # resize the input image, adding a single column (width), compute the 
    # horizontal gradient
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    
    # print('resized[:,:]', *resized, sep='\n')
    # print('resized[:, 1:]', *resized[:, 1:], sep='\n')
    # print('resized[:, :-1]', *resized[:, :-1], sep='\n')
    # compute the (relative) horizontal gradient between adjacent column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # print(f'>> diff: {type(diff)}', *diff, sep='\n')
    
    # convert the difference image to a hash
    # return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    
    diff_hash = 0
    arr = diff.flatten()
    for i, val in enumerate(arr):
        if val != 0:
            diff_hash += 2**i
    print('diff_hash:', diff_hash )
    return diff_hash


# grab the paths to the haystack images
cwd = pl.Path(input("Enter/Paste location of collection: "))
imageTest = pl.Path(input("Enter/Paste searching images location: "))

haystackPaths = [p for p in cwd.rglob("*")]
print(*haystackPaths, sep="\n")


print('----------')
# grab the paths to the needle images
needlePaths = list(imageTest.iterdir())

print('>>> Paths of input images (needles):')
print(*needlePaths, sep='\n')
print('----------')

print(">>> Searching for input images. Please wait a moment .....")

# grab the base subdirectories for the needle paths, initialize the
# dictionary that will map the image hash to corresponding image,
# hashes, then start the timer

# BASE_PATHS = set([pl.PurePosixPath(p).parts[-2] for p in needlePaths])
haystack = {}
start = time.time()

# iterate haystack paths
for p in haystackPaths:
    # load the image from disk
    image = cv2.imread(str(p))
    # if the image is None then we could not load it from disk (so skip it)
    if image is None: continue
    # The image is blurred to reduce the influence of the difference between 
    # neighboring pixels.
    image = cv2.medianBlur(image, 9)
    # convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the hash of image
    imageHash = dhash(image)
    # update the haystack dictionary
    l = haystack.get(imageHash, [])  # return empty list [] if the key 'imageHash' is missing
    l.append(str(p))
    haystack[imageHash] = l


# show timing for hashing haystack images, then start computing the
# hashes for needle images
print(">>> Search the Database with {} images in {:.2f} seconds."
              .format(len(haystack), time.time() - start))


match_pairs = []

# loop over the needle paths
for p in needlePaths:
    # load the image from disk
    image = cv2.imread(str(p))
    # if the image is None then we could not load it from disk (so skip it)
    if image is None: continue
    
    # The image is blurred to reduce the influence of the difference between 
    # neighboring pixels.
    image = cv2.medianBlur(image, 9)
    
    # convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the hash of image
    imageHash = dhash(image)
    # grab all image paths that match the hash
    matchedPaths = haystack.get(imageHash, [])
    
    # loop over all matched paths
    for matchedPath in matchedPaths:
        # match_pairs.append((p, matchedPath))
        match_pairs.append((str(pl.PurePath(p)), matchedPath))


if (match_pairs):
    print(f'>>> Detect {len(match_pairs)} similar image(s):')
    for p in match_pairs:
        print('{0:<15}'.format(' - Input image:\n\t'), p[0])
        print('{0:<15}'.format(' - Image in Collection:\n\t'), p[1])
        print('-----')
else:
    print('>>> All is OK!')
