# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from Utils import Twilio_Cred


def call():
    # Your Account Sid and Auth Token from twilio.com/console
    client = Client(Twilio_Cred.ACCOUNT_SID, Twilio_Cred.AUTH_TOKEN)

    obj_call = client.calls.create(
        method='POST',
        twiml='<Response>'
              '<Say voice="alice">Thanks for trying our documentation. Enjoy!</Say>'
              '</Response>',
        to='+524495293218',
        from_='+12058968177',
        machine_detection='DetectMessageEnd'
    )
    return obj_call

# ---------------------------------------------------------------------------


if __name__ == "__main__":
    call()
