# import smtplib

# smtpObj = smtplib.SMTP(host,port,local_hostname)


# import smtplib
# sender_mail = 'sender@fromdomain.com'
# receivers_mail = ['reciever@todomain.com']
# message = '''From:From Person %s
# To:To Person %s
# Subject: Sending SMTP e-mail
# This is a test e-mail message.
# '''%(sender_mail,receivers_mail)
# try:
#     smtpobj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender_mail,receivers_mail,message)
#     print("Successfully sent email")
# except Exception:
#     print("Error : unable to send email")


# smtpObj = smtplib.SMTP("gmail.com", 587)     



# import smtplib    
# sender_mail = 'sender@gmail.com'    
# receivers_mail = ['reciever@gmail.com']    
# message = """From: From Person %s  
# To: To Person %s  
# Subject: Sending SMTP e-mail   
# This is a test e-mail message.  
# """%(sender_mail,receivers_mail)    
# try:    
#    password = input('Enter the password');    
#    smtpObj = smtplib.SMTP('gmail.com',587)    
#    smtpobj.login(sender_mail,password)    
#    smtpObj.sendmail(sender_mail, receivers_mail, message)    
#    print("Successfully sent email")    
# except Exception:    
#    print("Error: unable to send email")    



#!/usr/bin/python3    
# import smtplib    
# sender_mail = 'sender@fromdomain.com'    
# receivers_mail = ['reciever@todomain.com']    
# message = """From: From Person %s  
# To: To Person %s  
  
# MIME-Version:1.0  
# Content-type:text/html  
  
  
# Subject: Sending SMTP e-mail   
  
# <h3>Python SMTP</h3>  
# <strong>This is a test e-mail message.</strong>  
# """%(sender_mail,receivers_mail)    
# try:    
#    smtpObj = smtplib.SMTP('localhost')    
#    smtpObj.sendmail(sender_mail, receivers_mail, message)    
#    print("Successfully sent email")    
# except Exception:    
#    print("Error: unable to send email")    
