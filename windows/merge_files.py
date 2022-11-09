import os
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

readSize = 1024

def join(fromDir, toFile):
    try:
        with open(toFile, 'wb'):
            output = open(toFile, 'wb')
            parts  = os.listdir(fromDir)
            parts.sort()
            print(Fore.WHITE + 'Merging files...')
            for fileName in parts:
                filePath = os.path.join(fromDir, fileName)
                with open(filePath, 'rb') as f:
                    while 1:
                        fileBytes = f.read(readSize)
                        if not fileBytes: break
                        output.write(fileBytes)
        print(Fore.GREEN + 'Files merged with success.')
    except Exception as e:
        print(Fore.RED + str(e))

try:
    if len(sys.argv) == 2 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
        print(Fore.GREEN + 'Use:merge_files.exe split-files-dir result-file')
        print(Fore.GREEN + 'Ex:merge_files.exe split_files fast-scalable-secure-hosting.pdf')
    elif len(sys.argv) == 3:
        split_files_dir = sys.argv[1]
        result_file = sys.argv[2]
        isPathExists = os.path.exists(split_files_dir)
        if not isPathExists:
            print(Fore.RED + f'{split_files_dir} does not exist.')
            sys.exit(0)
        join(split_files_dir, result_file)
    elif len(sys.argv) < 2 or len(sys.argv) > 3:
        print(Fore.RED + 'Incorrect arguments.')
        print(Fore.RED + 'Use:merge_files.exe split-files-dir result-file')
        print(Fore.RED + 'Ex:merge_files.exe split_files fast-scalable-secure-hosting.pdf')
except Exception as e:
    print(Fore.RED + str(e))

input("Press enter to exit the program.")
