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

class Actioncoronastats(Action):

    def name(self) -> Text:
    
        return "actions_corona_state_stat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('hi')
        slot_state = tracker.get_slot("state")
        slot_pincode = tracker.get_slot("pincode")
        print(slot_state)
        print(slot_pincode)


        if ((slot_state is not None or slot_pincode is not None) and tracker.latest_message['intent'].get('name')=='affirm') :
            
            try:
                entities = tracker.latest_message['entities']
                
                if slot_state:
                    responses = requests.get("https://api.covid19india.org/data.json").json()
                    message = "Please Enter Correct State Name !"
                    state = slot_state

                    if state.title() == "India":
                        state = "Total"
                
                    for data in responses["statewise"]:
                        if data["state"] == state.title():
                        
                            message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Today's Reported Cases****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]
                    dispatcher.utter_message(message)
                    return []
            except:
                dispatcher.utter_message("Please Enter Correct State Name !")
                return []

                
                 
            else:
                responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()

                entities = tracker.latest_message['entities']
                print("Now Showing Data For:", entities)
                pincode = None

                for i in entities:
                    if i["entity"] == "pincode":
                        pincode = i["value"]

                
                try:
                        temp_district = responses[0]['PostOffice'][0]['District']
                    
                        temp_district = str(temp_district)
                        if temp_district=='Bangalore':
                            temp_district='Bengaluru Urban'

                        temp_state = responses[0]['PostOffice'][0]['State']
                        responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
                        info = responses[temp_state.title()]['districtData'][temp_district.title()]
                      
                        message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Today's Reported Cases****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

                        dispatcher.utter_message(message)

                        return []
                except:
                    dispatcher.utter_message('Please Enter valid PinCode !')
                    return []

        else:
            try:
            
                entities = tracker.latest_message['entities']
                if entities[0]["entity"] == "state":
                    responses = requests.get("https://api.covid19india.org/data.json").json()
                    message = "Please Enter Correct State Name !"
                    
                    state = entities[0]["value"]
                    if slot_state.title() == "India":
                        state = "Total"
                
                    for data in responses["statewise"]:
                        if data["state"] == state.title():
                        
                            message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Today's Reported Cases****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]
                    dispatcher.utter_message(message)
                    return []
            except:
                dispatcher.utter_message("Please Enter Correct State Name !")
                return []


            
            else:
                responses = requests.get(f"https://api.postalpincode.in/pincode/{tracker.get_slot('pincode')}").json()

                entities = tracker.latest_message['entities']
                print("Now Showing Data For:", entities)
                pincode = None

                for i in entities:
                    if i["entity"] == "pincode":
                        pincode = i["value"]

                       
                try:
                        temp_district = responses[0]['PostOffice'][0]['District']
                    
                        temp_district = str(temp_district)
                        if temp_district=='Bangalore':
                            temp_district='Bengaluru Urban'

                        temp_state = responses[0]['PostOffice'][0]['State']
                        responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
                        info = responses[temp_state.title()]['districtData'][temp_district.title()]
                        
                        # if data["state"] == state.title():
                        # print(data)
                        message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Today's Reported Cases****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

                        dispatcher.utter_message(message)

                        return []
                except:
                    dispatcher.utter_message('Please Enter valid PinCode !')

            

