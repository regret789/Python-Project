import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('kushwahashambhu999@gmail.com',"Maurya@#$123")
subject="application for leave"
body="i want leave for 5 days"
message='subject:{}\n\n{}'.format(subject,body)
listadd=['kushwahashambhu888@gmail.com','kushwahashambhu777@gmail.com','kushwahashambhu666@gmail.com']
ob.sendmail('kushwahashambhu999@gmail.com',listadd,message)
print("sent mail")
ob.quit()