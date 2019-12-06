import socket, smtplib, time
flag = 0
IpAddr = 0
time.sleep(20)
while flag < 5:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IpAddr = s.getsockname()[0]
    if IpAddr != 0:
        flag = False
        sm = smtplib.SMTP('smtp.gmail.com',587)
        sm.starttls()
        sm.login("senders_email_address","sendes_email_password")
        sm.sendmail("senders_email_address","recivers_email_address",str(IpAddr))
        sm.quit()
        s.close()
        break
    else:
        flag += 1
        
    s.close()
    
    
print("Done", flag, IpAddr)




