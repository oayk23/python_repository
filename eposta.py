import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
import sys
mesaj = MIMEMultipart()
mesaj["From"] = "omeraykilic1905@gmail.com"
mesaj["To"] = "coskun.m.murat@gmail.com"
mesaj["Subject"] = "Smtp modülüyle mail gönderme"
yazi = """
**************
smtp ile mail atıyorum. 
ömer aykılıç
dersler güzel
**************
"""
mesaj_govdesi = MIMEText(yazi,"Plain")
mesaj.attach(mesaj_govdesi)
try:
    mail = smtplib.SMTP("smtp.gmail.com",658)
    mail.ehlo()
    mail.starttls()
    mail.login("omeraykilic1905@gmail.com","756530Gs_")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("mail başarıyla gönderildi....")
    mail.close()
except:
    sys.stderr.write("bir sorun oluştu")
    sys.stderr.flush()
