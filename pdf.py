from pypdf import *

def ensure_pdf_extension(file_name):
    if not file_name.lower().endswith('.pdf'):
        file_name += '.pdf'
    return file_name

def Manage(lor):
    split = PdfReader(f"./imp/{lor}")
    for i, page in enumerate(split.pages):
        writer = PdfWriter()
        writer.add_page(page)
        pdf_path = f"LOR_{i + 1}.pdf"
        with open(pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"Page {i + 1} saved as {pdf_path}")
    print("LOR-(n) files")

def ManageMarksheets(marksheets, transcripts):
    writer = PdfWriter() 

    files_to_merge = [f"./imp/{marksheets}", f"./imp/{transcripts}"]

    for file in files_to_merge:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    merged_pdf_path = "merged_output.pdf"
    with open(merged_pdf_path, "wb") as output_file:
        writer.write(output_file)
    
    print("Merged PDF saved as merged_output.pdf")
# print("All The Best")

if __name__ == "__main__":
    n = int(input("For LOR splitting press 1 \n For Marksheet and Transcript Merging press 2 \n For both press 3\n :> "))
    if (n!=0) and (n < 4) :
        if n == 1:
            lor = input("Enter PDF name in imp file of combine lor's : ")
            lor = ensure_pdf_extension(lor)
            Manage(lor)
        if n == 2:
            marksheets = input("Enter PDF name in imp file of marksheets : ")
            transcripts = input("Enter PDF name in imp file of transcripts : ")
            marksheets = ensure_pdf_extension(marksheets)
            transcripts = ensure_pdf_extension(transcripts)
            ManageMarksheets(marksheets,transcripts)
        if n == 3:
            lor =input("Enter PDF name in imp file of combine lor's : ")
            marksheets =input( "Enter PDF name in imp file of marksheets : ")
            transcripts =input( "Enter PDF name in imp file of transcripts : ")
            lor = ensure_pdf_extension(lor)
            marksheets = ensure_pdf_extension(marksheets)
            transcripts = ensure_pdf_extension(transcripts)
            Manage(lor)
            ManageMarksheets(marksheets,transcripts)
    else:
        print("Invalid Input")