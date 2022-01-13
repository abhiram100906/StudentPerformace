from twilio.rest import Client


def sendSms():
    account_sid = "twillio_account_Sid"
    auth_token = "twillio_auth_token"
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
                        to="+91-9902584278",
                        from_="+12014256022",  
                        body="Please check your wards performance report sent to your email.")
