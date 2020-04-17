import os
import json
import string

folders = ["Applications", "Documents", "Torrents", "Compressed Folders", "Images", "Videos", "Audio Files",
           "Other Files", "Installers"]
execFileExtensions = json.loads(open('executableFileExtensions.json').read())
videoFileExtensions = json.loads(open('videoFileExtensions.json').read())
audioFileExtensions = json.loads(open('audioFileExtensions.json').read())
compressedFileExtensions = json.loads(open('compressedFileExtensions.json').read())
imageFileExtensions = json.loads(open('imageFileExtensions.json').read())
documentFileExtensions = json.loads(open('documentFileExtensions.json').read())

bool1 = True
bool2 = True
i = 0

while bool1:
    while bool2:
        downloadDirectoryInput = input('Paste the path of the folder that you want to arrange: ')
        list(downloadDirectoryInput)
        downloadDirectoryInput = downloadDirectoryInput.replace("\\", "/")
        print("\nYour file path: " + downloadDirectoryInput+"\n")

        DOWNLOAD_DIRECTORY = downloadDirectoryInput + "/"
        try:
            os.chdir(DOWNLOAD_DIRECTORY)
            bool2 = False
        except Exception:
            print('Please enter a valid file path \n---------------------------------------------------')
            continue
    names = os.listdir()
    paths = []
    for name in names:
        path = DOWNLOAD_DIRECTORY + name
        paths.append(path)
    file_extensions = []
    for p in paths:
        filename, file_ext = os.path.splitext(p)
        file_extensions.append(file_ext)
    # make folders based on extensions
    ord_ext = list(dict.fromkeys(file_extensions))
    ord_ext_splitted = [x.strip('.') for x in ord_ext]
    for f in folders:
        if os.path.exists(DOWNLOAD_DIRECTORY + f):
            continue
        else:
            os.mkdir(f)
    for p in paths:
        try:
            i = i + 1
            filename, file_extension = os.path.splitext(p)
            file_extension_splitted = file_extension.strip('.')
            if any(p == DOWNLOAD_DIRECTORY + a for a in folders):
                continue
            if any(file_extension.upper() == b for b in execFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Applications/" + os.path.basename(p))
            elif any(file_extension.upper() == c for c in documentFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Documents/" + os.path.basename(p))
            elif file_extension.upper() == ".TORRENT":
                os.rename(p, DOWNLOAD_DIRECTORY + "Torrents/" + os.path.basename(p))
            elif any(file_extension.upper() == d for d in compressedFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Compressed Folders/" + os.path.basename(p))
            elif any(file_extension.upper() == e for e in imageFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Images/" + os.path.basename(p))
            elif file_extension.upper() == ".MSI":
                os.rename(p, DOWNLOAD_DIRECTORY + "Installers/" + os.path.basename(p))
            elif any(file_extension.upper() == f for f in videoFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Videos/" + os.path.basename(p))
            elif any(file_extension.upper() == g for g in audioFileExtensions):
                os.rename(p, DOWNLOAD_DIRECTORY + "Audio Files/" + os.path.basename(p))
            else:
                os.rename(p, DOWNLOAD_DIRECTORY + "Other Files/" + os.path.basename(p))
        except Exception:
            print("Error")
            break

    print("Done!", i, "files have been moved!")

    for f in folders:
        print(str(f), os.stat(f).st_size)

    for f in folders:
        if os.stat(f).st_size == 0:
            os.rmdir(f)

    bool1 = False
