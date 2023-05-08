import smtplib
import os
from datetime import datetime
from email.message import EmailMessage

def send_sudoku(recipient_email="alghaf.ahmd@gmail.com", puzzle_path='puzzles/puzzle0.pdf'):
    # Set up email details
    sender_email = 'sudoku.mailman@gmail.com'
    sender_password = 'nlbeqompyefoyihz'
    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Sudoku PDF'
    message.set_content('Please find attached the Sudoku PDF for today.')
    
    # Attach the PDF file to the email
    with open(puzzle_path, 'rb') as file:
        file_data = file.read()
        message.add_attachment(file_data, maintype='application', subtype='pdf', filename=os.path.basename(puzzle_path))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)
    
    # print(f'Email sent to {recipient_email} at {datetime.now()}')