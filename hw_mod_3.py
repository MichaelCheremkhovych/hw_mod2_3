import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def copy_file(source_path, target_dir):
    file_name = os.path.basename(source_path)
    _, extension = os.path.splitext(file_name)
    extension = extension.lower()

    if not os.path.exists(os.path.join(target_dir, extension)):
        os.makedirs(os.path.join(target_dir, extension))

    target_path = os.path.join(target_dir, extension, file_name)
    shutil.copyfile(source_path, target_path)

def process_directory(source_dir, target_dir):
    with ThreadPoolExecutor(max_workers=5) as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                executor.submit(copy_file, source_path, target_dir)

def main():
    parser = argparse.ArgumentParser(description='Process directory "Хлам"')
    parser.add_argument('source_dir', type=str, help='Path to source directory')
    parser.add_argument('target_dir', type=str, nargs='?', default='dist', help='Path to target directory')
    args = parser.parse_args()

    source_dir = args.source_dir
    target_dir = args.target_dir

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    process_directory(source_dir, target_dir)

if __name__ == "__main__":
    main()
