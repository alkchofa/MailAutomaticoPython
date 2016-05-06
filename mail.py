import smtplib 
 
fromaddr = 'Montoto@hotmail.com'
toaddrs  = 'destino@gmail.com'
msg = """ Este seria todo el cuerpo del mensaje"""
Subject = 'Asunto '
 

message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromaddr, toaddrs, Subject, msg)
 
# Datos
username = 'destinatario@hotmail.com'
password = 'contraseña'
 
# Enviando el correo
server = smtplib.SMTP('smtp.live.com:587') //este es para hotmail
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, message)
server.quit()
