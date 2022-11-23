import win32com.client as win32


# Criar a integração com Outlook
outlook = win32.Dispatch('outlook.application')

# Criar o email
email = outlook.CreateItem(0)

faturamento = 20000
metas =  50000

# configurar as informações do seu e-email
email.To = "seuemail@email.com"   # destino
email.Subject = "E-mail automatizado com Python"  # assunto
email.HTMLBody = f""" 
        <p>Bom dia Prezados(as), este é código do Python </p>
        
        <p> O faturamento mensal da Loja foi de R$ {faturamento} </p> 
        <p> Vendemos abaixo da meta, não foi suficiente para atingir a meta de {metas} . </p>
        
        <p> Atenciosamente, </p>
        <p> Python. </p>

"""  # corpo do e-mail


email.Send()
print('E-mail enviado com sucesso.')