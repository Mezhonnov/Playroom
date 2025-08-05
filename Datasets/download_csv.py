import kagglehub
import os
import shutil

# 1. Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

# 2. Define target folder
target_path = "C:/Users/imezh/PycharmProjects/Playroom/Datasets"

# 3. Copy all CSV files from the downloaded dataset to the target folder
copied_files = []
for file in os.listdir(path):
    if file.endswith(".csv"):
        src = os.path.join(path, file)
        dst = os.path.join(target_path, file)
        shutil.copy(src, dst)
        copied_files.append(dst)
