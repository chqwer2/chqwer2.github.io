import matplotlib.pyplot as plt
from glob import glob, iglob
import regex as re
import os
import numpy as np

path = 'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\_posts\\'

md_list = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.lower().endswith('.md') or f.lower().endswith('.markdown')]


origin_fold = r'C:\\Users\\calvchen\\AppData\\Roaming\\Typora\\typora-user-images\\'
origin_fold1 = r'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\img\\Typora\\'  # https://chqwer2.github.io/img/Typora/
target_fold = r'https://chqwer2.github.io/img/Typora/'


img_list = []

for md in md_list:
    if os.path.isdir(md):
        continue
    if not (md.endswith('md') or md.endswith('markdown')):
        continue

    print(md)
    md = md.rstrip('markdown').rstrip('.')
    try:
        f = open(md+'.md','r', encoding='utf8')

    except:
        f = open(md + '.markdown', 'r', encoding='utf8')

    data = f.read()
    new_data = re.sub(origin_fold, target_fold, data)
    new_data = re.sub(origin_fold1, target_fold, new_data)

    print("handling:", md)
    f.close()

    f1 = open(md + '.md', 'w', encoding='utf8')
    f1.write(new_data)

    group = re.findall(r"C:(.*)", data)
    for i, j in enumerate(group):
        img_list.append(group[i].split('\\')[-1].rstrip(')'))

    f1.close()

print("successful write MD files...")

# trans images


origin_fold = r'C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images'
target_fold = r'C:\Users\calvchen\PycharmProjects\chqwer2.github.io\img\Typora'

def trans(origin_loc, target_loc):
    try:
        img = plt.imread(origin_loc)
        plt.imsave(target_loc, img)
        print("succeed save:", target_loc)
    except:
        # print("defeat: ", origin_loc)
        pass
for img in img_list:
    trans(origin_fold  + '/' + img, target_fold  + '/' + img)



