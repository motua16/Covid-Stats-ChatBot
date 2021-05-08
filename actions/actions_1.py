# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloLoc(Action):

    def name(self) -> Text:
        return "action_get_loc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_name = tracker.get_slot("state")
        slot_name = tracker.get_slot("pincode")

        print("slotname", slot_name)

        dispatcher.utter_message(
            text="So You Live In " + slot_name.title() + " , Here Are Your Location's Corona Stats: \n")

        return []

class Actioncoronastats(Action):

    def name(self) -> Text:
        # print('hi')
        return "actions_corona_state_stat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('hi')
        entities = tracker.latest_message['entities']
        if entities[0]["entity"] == "state":
            responses = requests.get("https://api.covid19india.org/data.json").json()
            message = "Please Enter Correct State Name !"
            state = entities[0]["value"]
            if state == "india":
                state = "Total"
            # print('responses')
            # for data in responses["statewise"]:
            for data in responses["statewise"]:
                if data["state"] == state.title():
                
                    message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Since last 24 hours****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]

            print(message)
            
        else:
            responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()

            entities = tracker.latest_message['entities']
            print("Now Showing Data For:", entities)
            pincode = None

            for i in entities:
                if i["entity"] == "pincode":
                    pincode = i["value"]

            message = "Please Enter Correct PinCode !"

            if pincode == "":
                pincode = "Total"
        
            temp_district = responses[0]['PostOffice'][0]['District']
            temp_district = str(temp_district)

            temp_state = responses[0]['PostOffice'][0]['State']
            responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
            info = responses[temp_state.title()]['districtData'][temp_district.title()]
            
            # if data["state"] == state.title():
            # print(data)
            message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Since last 24 hours****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

        dispatcher.utter_message(message)

        return []

# class Actioncoronastats(Action):

#     def name(self) -> Text:
#         return "actions_corona_pincode_stat"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()

#         entities = tracker.latest_message['entities']
#         print("Now Showing Data For:", entities)
#         pincode = None

#         for i in entities:
#             if i["entity"] == "pincode":
#                 pincode = i["value"]

#         message = "Please Enter Correct PinCode !"

#         if pincode == "":
#             pincode = "Total"
    
#         temp_district = responses[0]['PostOffice'][0]['District']
#         temp_district = str(temp_district)

#         temp_state = responses[0]['PostOffice'][0]['State']
#         responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
#         info = responses[temp_state.title()]['districtData'][temp_district.title()]
        
#         # if data["state"] == state.title():
#         # print(data)
#         message = "Now Showing Cases For --> " + temp_district + " Since Last 24 : "+ "\n" + "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])



        
#         dispatcher.utter_message(message)

#         return []


#     def func():
#         entities = tracker.latest_message['entities']
#         if entities[0]["entity"] == "state":
#             responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()
#             message = "Please Enter Correct State Name !"

#             if state == "india":
#                 state = "Total"
#             for data in responses["statewise"]:
#                 if data["state"] == state.title():
#                     print(data)
#                     message = "Now Showing Cases For --> " + state.title() + " Since Last 24 Hours : "+ "\n" + "Active: " + data[
#                         "active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data[
#                                     "recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n" + "As Per Data On: " + data[
#                                     "lastupdatedtime"]

#             print(message)
            
#         else:
#             responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()

#             entities = tracker.latest_message['entities']
#             print("Now Showing Data For:", entities)
#             pincode = None

#             for i in entities:
#                 if i["entity"] == "pincode":
#                     pincode = i["value"]

#             message = "Please Enter Correct PinCode !"

#             if pincode == "":
#                 pincode = "Total"
        
#             temp_district = responses[0]['PostOffice'][0]['District']
#             temp_district = str(temp_district)

#             temp_state = responses[0]['PostOffice'][0]['State']
#             responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
#             info = responses[temp_state.title()]['districtData'][temp_district.title()]
            
#             # if data["state"] == state.title():
#             # print(data)
#             message = "Now Showing Cases For --> " + temp_district + " Since Last 24 : "+ "\n" + "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])

#         dispatcher.utter_message(message)

#         return []



