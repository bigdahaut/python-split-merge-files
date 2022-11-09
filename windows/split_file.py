import os
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

KILOBYTES = 1024
MEGABYTES = KILOBYTES * 1024
fileNumber = 1

def split(inputFile, chunkedFilePrefix, chunkSize):
    try:
        file_size = os.stat(inputFile).st_size
        file_size_in_megabytes = file_size / MEGABYTES
        if (file_size_in_megabytes / chunkSize) > 2:
            print(Fore.WHITE + 'Spliting file...')
            with open(inputFile, 'rb') as f:
                chunkSize = int(chunkSize * MEGABYTES)
                chunk = f.read(chunkSize)
                global fileNumber
                while chunk:
                    with open(f'{chunkedFilePrefix} {fileNumber}', 'wb') as chunk_file:
                        chunk_file.write(chunk)
                    fileNumber += 1
                    chunk = f.read(chunkSize)
            print(Fore.GREEN + 'File split with success.')
        else:
            print(Fore.RED + f'File is too small to split in several {chunkSize} Mo.')
    except Exception as e:
        print(Fore.RED + str(e))

try:
    if len(sys.argv) == 2 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
        print(Fore.GREEN + 'Use:split_file.exe file-to-split target_dir chunksize')
        print(Fore.GREEN + f'Ex:split_file.exe path{os.sep}to{os.sep}myapp.1.0.0.apk path{os.sep}to{os.sep}split_files 20')
    elif len(sys.argv) == 4:
        input_file = sys.argv[1]
        output_folder = sys.argv[2]
        chunk_size_in_megaoctet = int(sys.argv[3])
        isFileExists = os.path.isfile(input_file)
        #baseName = os.path.basename(output_files_with_prefix)
        #output_folder = output_files_with_prefix[0:-(len(baseName) + 1)]
        isPathExists = os.path.exists(output_folder)
        if not isFileExists:
            print(Fore.RED + f'{input_file} does not exist.')
            sys.exit(0)
        if not isPathExists:
            print(Fore.RED + f'{output_folder} does not exist.')
            # print(Fore.YELLOW + "output_files_with_prefix:", output_files_with_prefix)
            # print(Fore.YELLOW + "baseName:", baseName)
            print(Fore.YELLOW + "output_folder:", output_folder)
            sys.exit(0)
        root_ext = os.path.splitext(input_file) # root + extension for file full path
        output_files_with_prefix = output_folder + os.sep + os.path.basename(root_ext[0]) + "_"
        # print("output_files_with_prefix", output_files_with_prefix)
        # print("root_ext[0]:",root_ext[0])
        split(input_file, output_files_with_prefix, chunk_size_in_megaoctet)
    elif len(sys.argv) < 2 or len(sys.argv) > 4:
        print(Fore.RED + 'Incorrect arguments.')
        print(Fore.RED + 'Use:split_file.exe file-to-split target_dir chunksize')
        print(Fore.RED + 'Ex:split_file.exe path{os.sep}to{os.sep}myapp.1.0.0.apk path{os.sep}to{os.sep}split_files 20')
except Exception as e:
    print(Fore.RED + str(e))

input("Press enter to exit the program.")
