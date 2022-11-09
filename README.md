# python-split-merge-files
Split and merge files with python

#  Split file on Windows (windows/split_file.exe)
Use: split_file.exe file-to-split target_dir chunksize
Ex: split_file.exe "C:\Users\IEUser\Downloads\2022\DesktopEditors_x64.exe" "C:\Users\IEUser\Documents\Other\split_files" 50
For help, type: split_file.exe --help
#  Merge file on Windows (windows/merge_files.exe)
Use: merge_files.exe split-files-dir result-file
Ex: merge_files.exe "C:\Users\IEUser\Documents\Other\split_files" "C:\Users\IEUser\Documents\Other\DesktopEditors_x64.exe"
For help, type: merge_files.exe --help

#  Split file on Linux (ubuntu/split_file)
Use: ./split_file file-to-split target_dir chunksize
Ex: ./split_file "/home/xxx/my-movie.webm" "/home/xxx/Documents/split_files" 50
For help, type: split_file --help
#  Merge file on Linux (ubuntu/merge_files)
se:./merge_files split-files-dir result-file
Ex: ./merge_files "/home/xxx/Documents/split_files" "/media/xxx/my-movie.webm"
For help, type: merge_files --help

# Parameters
chunksize parameter is in megaoctet (Mo).
