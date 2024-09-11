import os
import zipfile

def unzip_files_in_folder(base_folder):
    # 遍历 base_folder 下的所有文件夹
    for foldername, subfolders, filenames in os.walk(base_folder):
        # 遍历每一个 zip 文件
        for filename in filenames:
            if filename.endswith('.zip'):
                zip_path = os.path.join(foldername, filename)
                
                # 解压文件
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(foldername)
                
                # 删除 zip 文件
                os.remove(zip_path)
                
                print(f'解压 {zip_path} 到 {foldername} 并删除了 zip 文件')

if __name__ == "__main__":
    base_folder = r'E:\Desktop\DEFECT_YOLO\DEFECT-DET-Dataset\images'
    unzip_files_in_folder(base_folder)