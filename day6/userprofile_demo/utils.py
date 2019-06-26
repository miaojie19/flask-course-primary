import os,secrets
from flask import current_app
from PIL import Image


def save_user_face_image(image_data):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(image_data.filename)
    new_image_name = random_hex + f_ext
    new_image_path = os.path.join(current_app.root_path, "static/profile", new_image_name)
    output_size = (125,125)
    i = Image.open(image_data)
    i.thumbnail(output_size)
    i.save(new_image_path)
    return new_image_name


