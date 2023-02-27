import os

def main():
    fileList = []
    pyFileList = []
    for root,directories,files in os.walk("."):
        for _file in files:
            absolute_path = os.path.join(root,_file)
            size = os.path.getsize(absolute_path)/1024
            fileAux = [absolute_path,size]
            if absolute_path[-3:] == '.py': pyFileList.append(fileAux)
            if size >= 1:
                fileList.append(fileAux)
            print(f"File path: {absolute_path} Size: {size}")
    print(fileList)
    print()
    print(pyFileList)


if __name__=='__main__':
    main()