from argparse import ArgumentParser
import sys
import os
import subprocess


def open_file(file_path, drawio_app_path=None):
    
    print(file_path)
    if file_path.endswith('.png'):
        if file_path.endswith('.drawio.png'):
            if drawio_app_path:
                try:
                    subprocess.Popen([drawio_app_path, file_path])
                    return
                except FileNotFoundError:
                    print(f"file not found: {file_path}")
            else:
                print("未指定 Draw.io 应用程序路径，将使用默认 PNG 应用打开。")
        os.startfile(file_path)
    else:
        print(f'not supported file type: {file_path}')


if __name__ == "__main__":
    # get file path
    parser = ArgumentParser(description='tell .drawio.png from .png file')
    parser.add_argument('file', type=str, help='file to open')
    args = parser.parse_args()
    file_path = args.file
    
    # get drawio path
    txt_path = os.path.join(os.path.dirname(__file__), "drawio_path.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        drawio_app_path = f.read().strip()
    open_file(file_path, drawio_app_path)
    