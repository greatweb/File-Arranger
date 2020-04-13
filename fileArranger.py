import os


folders = ["Applications", "Documents", "Torrents", "Zip Folders", "Images", "Videos", "Audio Files", "Other Files"]
fileTypes = ["exe", "pdf", "txt", "torrent", "rar", "jpg", "png", "jpeg", "mov", "mp4", "mp3"]

bool1 = True
bool2 = True
i = 0


while bool1 == True:
    while bool2 == True:
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
            if any(file_extension_splitted.lower() == a for a in ["exe", "msi"]):
                os.rename(p, DOWNLOAD_DIRECTORY + "Applications/" + os.path.basename(p))
            elif any(file_extension_splitted.lower() == a for a in ["pdf", "txt", "docx", "pptx"]):
                os.rename(p, DOWNLOAD_DIRECTORY + "Documents/" + os.path.basename(p))
            elif file_extension_splitted.lower() == "torrent":
                os.rename(p, DOWNLOAD_DIRECTORY + "Torrents/" + os.path.basename(p))
            elif any(file_extension_splitted.lower() == a for a in ["rar", "zip", "7z"]):
                os.rename(p, DOWNLOAD_DIRECTORY + "Zip Folders/" + os.path.basename(p))
            elif any(file_extension_splitted.lower() == a for a in ["jpg", "jpeg", "png", "psd"]):
                os.rename(p, DOWNLOAD_DIRECTORY + "Images/" + os.path.basename(p))
            elif any(file_extension_splitted.lower() == a for a in ["mov", "mp4"]):
                os.rename(p, DOWNLOAD_DIRECTORY + "Videos/" + os.path.basename(p))
            elif file_extension_splitted.lower() == "mp3":
                os.rename(p, DOWNLOAD_DIRECTORY + "Audio Files/" + os.path.basename(p))
            else:
                os.rename(p, DOWNLOAD_DIRECTORY + "Other Files/" + os.path.basename(p))
        except Exception:
            print("Error")
            break

    print("Done!", i, "files have been moved!")

    for f in folders:
        if os.stat(f).st_size == 0:
            os.rmdir(DOWNLOAD_DIRECTORY + f)
    bool1 = False
