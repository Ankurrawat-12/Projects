from twilio.rest import Client

TWILIO_SID = "ACcfc788399b0fccd4ba87beb4b3f36b1e"
TWILIO_AUTH_TOKEN = "d212959a4d9f3273e3830a5592f4a02c"
TWILIO_VIRTUAL_NUMBER = "+16468330538"
TWILIO_VERIFIED_NUMBER = "+918287413412"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
