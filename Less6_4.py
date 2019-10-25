import smtplib
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login('igortest3667@gmail.com', '3667test')
smtp_obj.sendmail('igortest3667@gmail.com', 'notifications@github.com', 'I did it!')
