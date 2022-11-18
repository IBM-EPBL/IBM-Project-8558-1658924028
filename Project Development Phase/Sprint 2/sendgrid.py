import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# from_address we pass to our Mail object, edit with your name
FROM_EMAIL = ‘Your_Name@SendGridTest.com’ Def
SendEmail (to_email):
 “”” Send an email to the provided email addresses
: param to_email = email to be sent to
 : returns API response code
 : raises Exception e: raises an exception “””
 Message = Mail (
 From_email=FROM_EMAIL,
 To_emails=to_email,
 Subject=’A Test from SendGrid!’,
 Html_content=’hello there from SendGrid your URL is: ‘+
‘<a href=https://github.com/cyberjive> right here! </a></strong>’)
 Try:
 Sg = SendGridAPIClient (os.environ.get (‘SENDGRID_API_KEY’))
 Response = sg.send (message)
 Code, body, headers = response.status_code, response.body, response.headers
 Print (f”Response Code: {code} “)
 Print (f”Response Body: {body} “)
 Print (f”Response Headers: {headers} “)
 Print (“Message Sent!”)
Except Exception as e:
 Print(“Error: {0}”.format€)
Return str (response.status_code)
If __name__ == “__main__”:
Send Email (to_email=input (“Email address to send to? “))