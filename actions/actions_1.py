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

import re

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

        if tracker.latest_message['intent'].get('name')=='deny':
            responses = requests.get("https://api.covid19india.org/data.json").json()
            state = "Total"
                
            for data in responses["statewise"]:
                if data["state"] == state.title():
                
                    message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Today's Reported Cases****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]
            dispatcher.utter_message(message)
            return []




        elif ((slot_state is not None or slot_pincode is not None) and tracker.latest_message['intent'].get('name')=='affirm') :
            
            
            entities = tracker.latest_message['entities']
            
            if slot_state:
                responses = requests.get("https://api.covid19india.org/data.json").json()
                message = "Please Enter Correct State Name !"
                state = slot_state

                if state.title() == "India":
                    state = "Total"
            
                for data in responses["statewise"]:
                    print(data["state"].title())
                    print('state is ', state.title())

                    if data["state"].title() == state.title()  :                    
                        message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Today's Reported Cases****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]
                
                if message!="Please Enter Correct State Name !":
                    dispatcher.utter_message(message)
                    return []

                # print('get slot result ',tracker.get_slot('state'))
                else:
                    responses = requests.get(f"https://api.postalpincode.in/postoffice/{tracker.get_slot('state')}").json()

                    entities = tracker.latest_message['entities']
                    print("Now Showing Data For:", entities)
                    state = None

                    for i in entities:
                        if i["entity"] == "state":
                            state = i["value"]
                    # print('state is ', state )

                    
                    try:
                        for i in responses[0]['PostOffice']: 

                            if i['District'] == 'Rewa'  :
                                print(i)
                            
                            if str(i['Name']) == state.title() or str(i['District']) == state.title() :     
                                
                                temp_district = i['District']
                                temp_state = i['State']
                                break
                        
                        temp_district =  re.sub("\(.*?\)","",temp_district).replace('&', 'and')

                        print(temp_district)
                        temp_state = re.sub("\(.*?\)","",temp_state).replace('&', 'and')
                        print('district is',temp_district)
                        print(temp_state)

                        

                        temp_district = str(temp_district)
                        if temp_district=='Bangalore':
                            temp_district='Bengaluru Urban'
                        if temp_state=='Chattisgarh':
                            temp_state='Chhattisgarh'

                        
                        responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
                        
                        try:
                            info = responses[(temp_state.title())]['districtData'][temp_district.title()]
                        except:
                            
                            info = responses[(temp_state.title()).replace('And', 'and')]['districtData'][temp_district.title().replace('And', 'and')]

                        print('info is ',info)
                    
                        message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Today's Reported Cases****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

                        dispatcher.utter_message(message)

                        return []
                    except:
                        dispatcher.utter_message('Please Enter valid city/state name !')
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
                    print('hi')
                    dispatcher.utter_message('Please Enter valid PinCode !')
                    return []

        else:
            
            try:
                entities = tracker.latest_message['entities']
                print('entities ',entities)
                if entities[0]["entity"] == "state":
                    responses = requests.get("https://api.covid19india.org/data.json").json()
                    message = "Please Enter Correct State Name !"
                    
                    state = entities[0]["value"]
                    if slot_state.title() == "India":
                        state = "Total"
                
                    for data in responses["statewise"]:
                        if data["state"].title() == state.title():
                        
                            message = "Now Showing Cases For --> " + state.title()+"\n" + "****Overall****"+ "\n"+"\n" + "Active: " + data["active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data["recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n"+"\n"+"\n" + "****Today's Reported Cases****"+ "\n"+ "\n" + "Confirmed Today: " + data["deltaconfirmed"] + " \n"  + "Recovered Today: " + data["deltarecovered"] + " \n" + "Deaths Today: " + data["deltadeaths"]
                    if message!="Please Enter Correct State Name !":
                        dispatcher.utter_message(message)
                        return []

                    else:

                        # print('get slot result ',tracker.get_slot('state'))
                        responses = requests.get(f"https://api.postalpincode.in/postoffice/{tracker.get_slot('state')}").json()

                        entities = tracker.latest_message['entities']
                        print("Now Showing Data For:", entities)
                        state = None

                        for i in entities:
                            if i["entity"] == "state":
                                state = i["value"]
                        # print('state is ', state )

                        
                        try:
                            for i in responses[0]['PostOffice']: 

                                if str(i['Name']) == state.title() or str(i['District']) == state.title() :     
                                    
                                    temp_district = i['District']
                                    temp_state = i['State']
                                    break
                            
                            temp_district =  re.sub("\(.*?\)","",temp_district).replace('&', 'and')

                            print(temp_district)
                            temp_state = re.sub("\(.*?\)","",temp_state).replace('&', 'and')
                            print('district is',temp_district)
                            print(temp_state)

                            

                            temp_district = str(temp_district)
                            if temp_district=='Bangalore':
                                temp_district='Bengaluru Urban'
                            if temp_state=='Chattisgarh':
                                temp_state='Chhattisgarh'

                            
                            responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
                            
                            try:
                                info = responses[(temp_state.title())]['districtData'][temp_district.title()]
                            except:
                                
                                info = responses[(temp_state.title()).replace('And', 'and')]['districtData'][temp_district.title().replace('And', 'and')]

                            print('info is ',info)
                        
                            message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Today's Reported Cases****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

                            dispatcher.utter_message(message)

                            return []
                        except:
                            dispatcher.utter_message('Please Enter valid city/state name !')
                            return []
            except:
                dispatcher.utter_message('Please valid city/state name!')
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
                    print(temp_state)
                    if temp_district=='Bangalore':
                        temp_district='Bengaluru Urban'

                    
                    responses = requests.get("https://api.covid19india.org/state_district_wise.json").json()
                    info = responses[temp_state.title()]['districtData'][temp_district.title()]
                    
                    # if data["state"] == state.title():
                    # print(data)
                    message = "Now Showing Cases For --> " + temp_district +"\n"+ "****Overall****"+ "\n"+  "\n" +  "\n"+ "Active: " + str(info["active"]) + " \n" + "Confirmed: " + str(info["confirmed"]) + " \n" + "Recovered: " + str(info["recovered"]) + " \n" + "Deaths: " + str(info["deceased"])+" \n"+ "\n" + "\n"+ "****Today's Reported Cases****"+ "\n" +  " \n" + "Confirmed Today: " + str(info["delta"]["confirmed"]) + " \n" + "Recovered Today: " + str(info["delta"]["recovered"]) + " \n" + "Deaths Today: " + str(info["delta"]["deceased"])

                    dispatcher.utter_message(message)

                    return []
                except:
                    print('hellooo')
                    dispatcher.utter_message('Please Enter valid PinCode !')

            

