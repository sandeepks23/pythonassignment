import smtplib

def send_mail():
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("kichusandeep71@gmail.com","9446328350")
    server.sendmail("kichusandeep71@gmail.com","kssandeep230@gmail.com","Hello")
    server.quit()

send_mail()