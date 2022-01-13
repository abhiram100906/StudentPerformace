from twilio.rest import Client


def sendSms():
    account_sid = "ACb72b923e307484c707975e065c368949"
    auth_token = "af61c72336690df9a0f26354a5dcf2cc"
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
                        to="+91-9902584278",
                        from_="+12014256022",  
                        body="Please check your wards performance report sent to your email.")
