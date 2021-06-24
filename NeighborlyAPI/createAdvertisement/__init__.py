import azure.functions as func
import pymongo
import logging
import json
def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    request = req.get_json()
    value = "Sending message from my Azure Functions HTTP Trigger"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "batur.usta93@gmail.com"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    if request:
        try:
            url = "mongodb://project2cosmosdb:oIEHxvzEXWWZIugAqL74I0qJIgrc01qSmydEfw8T5hYvVRLjJ2cemDhpnd0RXYjapnLYb7iK5LWf4nsvxWx92w==@project2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmosdb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['project2_database']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )