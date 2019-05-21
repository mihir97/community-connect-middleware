# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import ibm_watson


assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='xxxx',
    url='https://gateway.watsonplatform.net/assistant/api'
)


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    assistant.set_default_headers({'x-watson-metadata': "12345"})
    message = request.values.get('Body', None)
    from_no = request.values.get('From', None)
    print(message, from_no)
    response = assistant.message(
    workspace_id='xxxx',
        input={
            'text': message
        }
    ).get_result()
    #res = json.dumps(response)
    reply = response["output"]["text"][0]
    print(reply)
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
