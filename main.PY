import pikepdf

# pip install pikepdf if not installed

def remove_password_from_pdf(filename, password=None):
    pdf = pikepdf.open(filename, password=password)
    pdf.save("no_password.pdf")

if __name__ == "__main__":
    try :
        f = input("Enter the file name that is stored in the current directory in format (example.pdf): ")
        p = input("Enter Password of the locked file : ")
        remove_password_from_pdf(filename=f,password=p)
    except:
        print("Something else went wrong")