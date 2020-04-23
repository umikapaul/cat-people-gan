import os
from tqdm import tqdm
from PIL import Image

for i in range(1,4):
    PIC_DIR = "./Cat-faces-dataset-master/dataset-part"+str(i)+"/"
    for pic_file in tqdm(os.listdir(PIC_DIR)):
        im = Image.open(PIC_DIR + pic_file)
        im_resized = im.resize((128,128))
        im_resized.save("./resized-cats/"+pic_file)