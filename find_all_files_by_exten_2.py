import os
for root, dirs, files in os.walk("C:/Users/rapid/AppData/Local/Programs/Python/Python310"):
    for file in files:
        res1 = ''
        if file.endswith("._pth"):
             res1 += (os.path.join(root, file))
             print(f'{res1}')



