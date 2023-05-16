import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
from Subscriber import Subject

class EmailSender(Subject):
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def send_sudoku(self, recipient_email: str):
        # Generate Sudoku puzzle
        puzzle = generate_sudoku()

        # Send email with puzzle to recipient
        try:
            # Set up email content
            msg = MIMEMultipart()
            msg['From'] = 'sender_email@gmail.com' # Replace with your own email address
            msg['To'] = recipient_email
            msg['Subject'] = 'Here is your Sudoku puzzle!'

            # Add HTML content to email
            html = f"""\
            <html>
              <body>
                <p>Hi,<br>
                   Here is your Sudoku puzzle for today:</p>
                <p>{puzzle}</p>
              </body>
            </html>
            """
            msg.attach(MIMEText(html, 'html'))

            # Send email using SMTP server
            smtp_server = 'smtp.gmail.com'
            port = 587
            sender_email = 'sender_email@gmail.com' # Replace with your own email address
            sender_password = 'sender_password' # Replace with your own password
            smtp = smtplib.SMTP(smtp_server, port)
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, msg.as_string())
            smtp.quit()

            # Notify observers that the email has been sent
            self.notify_observers(f"Email sent to {recipient_email} successfully")

        except Exception as e:
            # Notify observers that the email failed to send
            self.notify_observers(f"Email failed to send to {recipient_email}. Error: {str(e)}")