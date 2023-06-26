
# e-posta gönderme programı --   hatalı çalışıyor..


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QTextCursor
from email.message import EmailMessage
import smtplib

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class EmailSender(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("E-posta Gönderme")
        self.setGeometry(100, 100, 400, 300)

        self.label_to = QLabel("Kime:", self)
        self.label_to.move(50, 30)
        self.to_lineedit = QLineEdit(self)
        self.to_lineedit.move(120, 30)

        self.label_subject = QLabel("Konu:", self)
        self.label_subject.move(50, 70)
        self.subject_lineedit = QLineEdit(self)
        self.subject_lineedit.move(120, 70)

        self.label_body = QLabel("İçerik:", self)
        self.label_body.move(50, 110)
        self.body_textedit = QTextEdit(self)
        self.body_textedit.setGeometry(120, 110, 200, 100)

        self.send_button = QPushButton("Gönder", self)
        self.send_button.setGeometry(150, 230, 100, 30)
        self.send_button.clicked.connect(self.send_email)

    def send_email(self):
        sender_email = "your_email@gmail.com"
        client_id = "your_client_id"
        client_secret = "your_client_secret"
        access_token = "your_access_token"
        refresh_token = "your_refresh_token"

        receiver_email = self.to_lineedit.text()
        subject = self.subject_lineedit.text()
        body = self.body_textedit.toPlainText()

        message = EmailMessage()
        message.set_content(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = receiver_email

        try:
            oauth2_client = BackendApplicationClient(client_id=client_id)
            oauth2_session = OAuth2Session(client=oauth2_client)
            oauth2_session.token = {'access_token': access_token,
                                    'refresh_token': refresh_token,
                                    'token_type': 'Bearer'}

            auth_string = oauth2_session.get_auth_header()
            smtp_url = 'smtp.gmail.com'
            smtp_port = 587

            with smtplib.SMTP(smtp_url, smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(sender_email, None, initial_response_ok=False, auth_string=auth_string)
                server.send_message(message)
                print("E-posta gönderildi!")
        except Exception as e:
            print("E-posta gönderme hatası:", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    sys.exit(app.exec_())
