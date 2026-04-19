import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailBot:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_mail(self, receiver_email, subject, body):
        try:
            # Create message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))

            # SMTP Server (Gmail)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send email
            server.sendmail(self.sender_email, receiver_email, message.as_string())
            server.quit()

            print("✅ Email sent successfully!")

        except Exception as e:
            print("❌ Error:", str(e))


# ==========================
# 🔹 Run MailBot
# ==========================
if __name__ == "__main__":
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your app password: ")

    bot = MailBot(sender_email, sender_password)

    receiver = input("Receiver Email: ")
    subject = input("Subject: ")
    body = input("Message: ")

    bot.send_mail(receiver, subject, body)