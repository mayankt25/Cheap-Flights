import smtplib
from data_manager import DataManager
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email = "mayank.test098@gmail.com"
        self.password = os.environ.get("PASS")

    def send_emails(self, message):
        data_manager = DataManager()
        user_data = data_manager.get_user_data()
        for data in user_data:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(from_addr=self.my_email, to_addrs=data["email"], msg=f"Subject: New Low Price Flight!\n\n{message}")
