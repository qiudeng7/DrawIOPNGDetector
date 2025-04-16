from argparse import ArgumentParser
import sys
import os
import subprocess


def open_file(file_path, drawio_app_path=None, png_app_path=None):

    print(file_path)
    if file_path.endswith('.png'):
        if file_path.endswith('.drawio.png'):
            if drawio_app_path:
                subprocess.Popen([drawio_app_path, file_path])
                return
        else:
            subprocess.Popen([png_app_path, file_path])
    else:
        print(f'not supported file type: {file_path}')


if __name__ == "__main__":
    # get file path
    parser = ArgumentParser(description='tell .drawio.png from .png file')
    parser.add_argument('file', type=str, help='file to open')
    args = parser.parse_args()
    file_path = args.file

    # get drawio path
    txt_path = os.path.join(os.path.dirname(__file__), "app_path.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        app_path = f.readlines()
        drawio_app_path = app_path[0].strip()
        png_app_path = app_path[1].strip()
    open_file(file_path, drawio_app_path, png_app_path)
