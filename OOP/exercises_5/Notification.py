from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def preview(self):
        print(f"[To: {self.recipient}]: {self.message}")
    
class EmailNotification(Notification):
    def __init__(self, recipient, message, subject):
        super().__init__(recipient, message)
        self.subject = subject

    def send(self):
        print(f"Sending email to {self.recipient} with subject {self.subject}: {self.message}")

class SmsNotification(Notification):
    def send(self):
        if len(self.message) <= 160:
            print(f"Sending SMS to {self.recipient}: {self.message}")
        else:
            print("Message too long for SMS")

class PushNotification(Notification):
    def __init__(self, recipient, message,device_id):
        super().__init__(recipient, message)
        self.device_id = device_id

    def send(self):
        print(f"Push to device {self.device_id}: {self.message}")
    
##TEST
notifications = [
    EmailNotification("jan@nowak.pl", "Cześć Jan, co tam?", "Witamy!"),
    SmsNotification("+48123456789", "Krótka wiadomość tekstowa."),
    SmsNotification("+48987654321", "To jest bardzo długa wiadomość, która ma na celu przetestowanie naszego limitu stu sześćdziesięciu znaków w klasie SmsNotification. Jeśli wszystko działa poprawnie, ten tekst nie powinien zostać wysłany."),
    PushNotification("User_123", "Twoje zamówienie zostało wysłane", "dev_999abc")]

for notification in notifications:
    notification.send()

    