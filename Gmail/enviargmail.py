import smtplib
import email.message


def enviar_email():
    faturamento =  20000
    meta = 50000
    
    body = f""" 
    Bom dia Prezados(as), este é código do Python. <br><br>
    
    O faturamento mensal da Loja foi de R$ {faturamento:,.2f}, <br>
    Vendemos abaixo da meta, não foi suficiente para atingir acima de R${meta:,.2f}. <br>
    
    <br> Atenciosamente,
    <br> Python.
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Assunto importante"  # Assunto
    msg['From'] = "seuemail@email.com"  # Rementente
    msg['To'] = "enviar para quem@email.com"  # Destinatário
    password = "mqojjsimfeplcgmu"  # senha gerada pelo gmail.
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(body)
    
    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    
    # Login credencials for sending the email
    
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8")) 
    
enviar_email()   
print(enviar_email)    
    
    