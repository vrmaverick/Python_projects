import requests
import hashlib
import PyPDF2

def request_api(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)

    if res.status_code != 200:
        print(f"Request failed with status code: {res.status_code}")
        raise RuntimeError('Please check with API')
    
    return res.text  # Return the response content as text

def count(response, to_check):
    response_lines = (line.split(':') for line in response.splitlines())

    for h, count in response_lines:
        if h == to_check:
            return int(count)
        
    return 0

def convert_sa1(Raw_Password):
    hash_prefix = hashlib.sha1(Raw_Password.encode('utf-8')).hexdigest().upper()
    head, tail = hash_prefix[:5], hash_prefix[5:]
    response = request_api(head)  # Will return all the hash that matches first 5 chars of the 
    
    return count(response, tail)  # Check the remaining and return count
def printing(password):
    breach_count = convert_sa1(password)

    if breach_count != 0:
        print(f"The password '{password}' has been found  {breach_count} time please change it ASAP!!")

    else:
        print(f"The password '{password}'has not been found Please carry on ")

def main():

    while True:

        try:
            select = int(input("Do you want to enter in Terminal or read from a text file?\n Enter 1 for terminal\n Enter 2 for text file:\n Enter 3 to Exit : "))

            if select == 1:
                password = input("Enter the password you wish to check for: ")
                printing(password)

            elif select == 2:
                path = input("Enter full path of the file: ")

                with open(path, "r") as filee:
                    password = filee.read().strip()

                printing(password)

            elif select == 3:
                exit()
                
            else:
                print("Enter a valid option (1 or 2)")

        except ValueError:
            print("Enter a valid numeric option")

if __name__ == '__main__':
    main()

