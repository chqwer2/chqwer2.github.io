

import regex as re
f = open('C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\_posts\\Math\\Statistics'+'.md','r', encoding='utf8')
data = f.read()
# origin_fold = r'C:\\Users\\calvchen\\AppData\\Roaming\\Typora\\typora-user-images'
origin_fold = r'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\img\\Typora\\'
target_fold = r'https://chqwer2.github.io/img/Typora/'

# for i in data:
#     re.findall()

# print(origin_fold)
# print(target_fold)
# print(re.escape(target_fold))
# print( r'![image-20220205172337486](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220205172337486.png)')

print(re.sub(origin_fold, target_fold, data))

from datasets import load_dataset, DatasetDict, Dataset
