import glob
python_files = glob.glob('D:\\python程式設計範例\\ch10\*.py')
for file_name in python_files:
    print('檔案為' + file_name)
    with open(file_name, encoding = 'utf8') as f:
        for line in f:
            print(line.rstrip())
    print()
