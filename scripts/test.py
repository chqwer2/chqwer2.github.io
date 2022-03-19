import os
import numpy as np
from glob import glob, iglob
import regex as re

# md_list = []
path = 'C:\\Users\\calvchen\\PycharmProjects\\chqwer2.github.io\\_posts\\'

md_list = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.lower().endswith('.md') or f.lower().endswith('.markdown')]

print(md_list)