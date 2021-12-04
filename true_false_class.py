import json
import os, shutil, pathlib

with open('Photo_1.json', 'r', encoding='utf-8') as f: #открыли файл с данными
    text = json.load(f) #загнали все, что получилось в переменную

    
new_base_dir = pathlib.Path("Photos")    
dir_1 = new_base_dir / "true"
dir_2 = new_base_dir / "false"

for i in range(len(text['images'])):
    if text['images'][i]['max_detection_conf'] > 0.9:
        for j in range(len(text['images'][i]['detections'])):
            if (text['images'][i]['detections'][j]["category"] == '1'):
                if (text['images'][i]['detections'][j]["conf"] > 0.9):
                    new_name = f"{i}.jpeg"
                    shutil.copyfile(src= text['images'][i]['file'], dst=dir_1 / new_name)
    else:
        new_name = f"{i}.jpeg"
        shutil.copyfile(src= text['images'][i]['file'], dst=dir_2 / new_name)
