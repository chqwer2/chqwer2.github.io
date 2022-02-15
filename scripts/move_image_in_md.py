import matplotlib.pyplot as plt
from glob import glob
import regex as re

md_list = [r'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\_posts\\Math\\Statistics']
origin_fold = r'C:\\Users\\calvchen\\AppData\\Roaming\\Typora\\typora-user-images'
target_fold = r'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\img\\Typora'  # https://chqwer2.github.io/img/Typora/
print(origin_fold, target_fold)

img_list = []

for md in md_list:
    f = open(md+'.md','r', encoding='utf8')
    f1 = open(md+'1.md', 'w', encoding='utf8')
    data = f.read()
    new_data = re.sub(origin_fold, target_fold, data)
    f1.write(new_data)

    group = re.findall(r"C:(.*)", data)
    for i, j in enumerate(group):
        img_list.append(group[i].split('\\')[-1].rstrip(')'))

    f.close()
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
        print("defeat: ", origin_loc)

for img in img_list:
    trans(origin_fold  + '/' + img, target_fold  + '/' + img)



