import os, patoolib
import glob # this is for pathname pattern

# patoolib can extract .zip, .gz, .tar, .rar, etc..

# patoolib.extract_archive('<zip_filename>', outdir='<path>', program='<zip_program>')
# if no outdir, file will be extracted to current dir
# patoolib.extract_archive('testing.rar')

def extractFiles(fromDir,toDir):
    os.chdir(fromDir)
    filesList = [f for f_ in [glob.glob(e) for e in ['*.rar', '*.zip']] for f in f_]
    # print (filesList)

    if not os.path.exists(toDir):
        os.makedirs(toDir)

    tempFile = os.listdir("Extracted")
    extractedFile = []
    for ef in tempFile  :
        extractedFile.append(os.path.splitext(ef)[0])
        # print (extractedFile)

    for f in filesList:
        # convert from list to string
        filename = f.split('.')[0]
        # print (filename)
        # print (extractedFile)

        if filename not in extractedFile:
            # print(f)
            patoolib.extract_archive(f, outdir=toDir)
        else:
            print(filename + " already exist!")
            # print(filename)
        

print('Start')

fromDir = 'C:\\Users\\User\\Desktop\\Python Tutorial\\02_Extracting data'
toDir = 'C:\\Users\\User\\Desktop\\Python Tutorial\\02_Extracting data\\Extracted'
extractFiles(fromDir,toDir)

print('Finish')