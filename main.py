from PIL import Image
import os

path = "C:/Users/sezes/OneDrive/Pictures/IG folder"
new_path = "C:/Users/sezes/OneDrive/Pictures/Resized IG"

IG_size = (1080, 1080)

for images in os.listdir(path):
    im = Image.open(f'{path}/{images}')

    Resized_im=im.resize(IG_size)
    fn=os.path.splitext(images)[0]
    Resized_im.save(f'{new_path}/{fn}_editedIG.jpg')