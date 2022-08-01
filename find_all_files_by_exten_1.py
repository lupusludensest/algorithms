import os
for root, dirs, files in os.walk("E:\Gurov_SSD_256\IT\Testing"):
    for file in files:
        if file.endswith(".pdf"):
             print(os.path.join(root, file))