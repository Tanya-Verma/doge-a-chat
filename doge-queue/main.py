import hashlib
import hmac
import json

from google.cloud import pubsub_v1

publisher_client = pubsub_v1.publisher_client()

project_id="<PROJECT_ID>"
topic_name = "<PUBSUB_TOPIC_NAME>"
topic_path=publisher_client.topic_path(
project_id, topic_name
)

future=dict()

with open("config.json", "r") as f:
    data=f.read()
config = json.loads(data)

#Python 3+ version of https://github.com/slackpi/python-slack-events-api/blob/master/slackeventsapi/server.py

def verify_signature(request)
# Takes a slack request and determines if the request and its credentials are valid

#Args:
    #request (flask.Request): A slack request

timestamp=request.headers.get(
    "X-Slack-Request-Timestamp"," ")
        signature = request.headers.get(
            "X-Slack-Signature"," ")

            req =str.encode("v0:{}:".format(timestamp))+ request.get_data()
            request_digest = hmac.new(
                str.encode(config["SLACK_SECRET"], req, hashlib.sha256
                ).hexdigest()
                request_hash ="v0={}".format(request_digest)
            )

            if not hmac.compare_digest(request_hash,signature):
                raise ValueError("Invalid request/credentials.")


def doge_queue(request):
    #HTTP cloud Function. Takes a slck request and passes it to 
    #a second cloud function for process processing via Pub/
    #Sub.
        #Args:
          # request(flast.Request):A Slack request 
       # Returns:
             # A response to the slack channel

              if request.method !="Post":
                return "Only POST requests are accepted", 405

                verify_signature(request)
                data = json.dump(request.form)

                future.update({dta:None})

                # when you publish a message , the client returns a future.

                future =publisher_client.publish(
                    topic_path, data= data.encode("utf-8")

                    #data must be a byterstring
                )

                """check if future.result() resolved with the ID of the message.
                This indicates the message was successful.
                """

                try:
                    print(future.result())
                except Exception as e:
                    print("Error publishing:" + str(e))

                return "Working on it!"


        )
)

