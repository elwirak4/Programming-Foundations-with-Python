from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0e992cb7b5044e5ce789e0983681f36d"
# Your Auth Token from twilio.com/console
auth_token  = "986bb53081b0e75a8f45455301e94f14"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+48662795227", 
    from_="+48732484187",
    body="Hello from Python! This is the first massage freom twilio to me!!!")

print(message.sid)
