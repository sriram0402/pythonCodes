import smtplib

eServer='smtp-mail.outlook.com'
port=587
messagqe=(f'Subject: Hi Testing SMTP'
         f'\n\n'
         f'This is adv python class'
         f'Upload the work'
         '\nThank you')
message=(f'\n\n'
         'This is sriram test mail')
with smtplib.SMTP(eServer, port) as smtpObj:
    smtpObj.starttls()

    smtpObj.login('advpython@outlook.com','sriram123')
    smtpObj.sendmail('advpython@outlook.com','garmillas@mail.sacredheart.edu',message)
    
    
    
