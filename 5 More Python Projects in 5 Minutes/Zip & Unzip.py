import patoolib

def Zip():
    patoolib.create_archive("file.zip",("path_to_file_1","path_to_file_2"))

def Unzip():
    patoolib.extract_archive("path_to_file_to_be_extracted",outdir="extract")

if __name__ == '__main__':
    choice=(int(input(Enter 1 for Zip & 2 for Unzip)))
    if choice==1:
        Zip()
    else:
        Unzip()
