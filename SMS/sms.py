#  Você precisará de uma conta Sinch para obter a chave e o segredo do aplicativo. 
#  Visite www.sinch.com para começar.


import time
from sinchsms import SinchSMS

def SendSMS():
    phone = '+' 
    app_key = ''
    app_secret = ''
    
    message = 'Hello World'
    client = SinchSMS(app_key, app_secret)
    print(f'Enviado {message} para {phone}.')
    
    response = client.send_message(phone, message)
    message_id = response["messageId"]
    response = client.check_status(message_id)
    
    while response['status'] != "sucesso":
        print(response['status'])
        time.sleep(1)
        response = client.send_message(message_id)
        
    print(response["status"])
    
    
    
if __name__=="__main__":
    SendSMS()