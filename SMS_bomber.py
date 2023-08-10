#twillio for text voice or audio
from twilio.rest import Client

account_sid = 'VDEGRERGERGERGERG#'#Account id from twilio
auth_token = '@@@@@222@@2'#Api token from twilio
client = Client(account_sid, auth_token)

mssg = input("Enter the message you want to send: ")

while(True):
  
    try:
        bomb = int(input("do you want to bomb messages ?? Enter value "))
      
        if bomb < 10 and bomb != 0 :
          
            for i in range(0,bomb):
                message = client.messages.create(
                from_='+123456789', # twilo number valid
                body= mssg ,
                to='+91################3'#recipiant phone mumber
                )
                print(message.sid)
            break
          
        elif bomb == 0:
            print("Zero is not Valid")
            break
          
        elif bomb < 0:
            raise ValueError('Fatal error')
          
    except :
        print("Please enter valid number !!!!")
