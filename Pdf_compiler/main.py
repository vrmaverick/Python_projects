import PyPDF2
import os
def pdf_combine(pdf_list):
    merge = PyPDF2.PdfFileMerger(strict=False)
    for pdf in pdf_list:
        print(pdf)
        merge.append(pdf)
    file_name = input("Enter file name for combined pdf : ")
    merge.write(f'{file_name}.pdf')
while True:
    try:
        number = int(input("Enter number of pdf to merge : "))
        break
    except:
        print('please enter a valid number : ')      
li = []
for i in range(number):
    name = input("enter the path of pdf file ")
    file_path = os.path.abspath(name)  # Get the absolute path of the file
    check = os.path.exists(file_path)
    if check:
        li.append(name)
    else:
        print("file not found error")
        exit()
pdf_combine(li)
