import os
for root, dirs, files in os.walk("E:\Gurov_SSD_256"):
    for file in files:
        res1 = ''
        if file.endswith(".pdf"):
             res1 += (os.path.join(root, file))
             print(f'{res1}')
