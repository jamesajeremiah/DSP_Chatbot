# From https://docs.python.org/3/library/email.examples.html

# Modified by: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Creates an email using the conversation log and sends it to the appropriate inbox
# The inbox will then be read by ITOnline using Chatbot_XSL.xsl


import smtplib, ssl
from email.message import EmailMessage


''' DEFINE CONSTANTS '''

PORT = 465  # For SSL
PASSWORD = "ZoGvz7kWM3Zz3KyW*j$kx9AzoPJ3j7m^UvMr%QV#bvyDESfbLN"

SENDER_EMAIL = "jjchatbotproject@gmail.com"
RECEIVER_EMAIL = "itonline.studentbot@uwe.ac.uk"
#RECEIVER_EMAIL = "jjbotproject@outlook.com"
#RECEIVER_EMAIL = "jjchatbotproject@gmail.com"


''' DEFINE FUNCTIONS '''

def main(conversation):
    """ Creates the email from the conversation's attributes,
    then logs into the email account using SMTP and sends it. """

    user_name = conversation.user_name
    chat_log = conversation.chat_log
    solved_string = conversation.topic.id
    subject_string = conversation.solution

    email_subject = f"{solved_string} - Chatlog: {subject_string}"
    email_body = f"{user_name}\n{chat_log}"
    
    email_msg = EmailMessage()
    email_msg.set_content(email_body)
    email_msg["Subject"] = email_subject
    email_msg["SubjectID"] = user_name
    email_msg["From"] = SENDER_EMAIL
    email_msg["To"] = RECEIVER_EMAIL
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    #login and send email
    s = smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context)
    s.login(SENDER_EMAIL, PASSWORD)
    s.send_message(email_msg)
    s.quit()