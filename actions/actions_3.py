import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

class ActionEntity(Action):

    def name(self) -> Text:
        return "action_know_whether_previous_calculated"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_state = tracker.get_slot("state")
        slot_pincode = tracker.get_slot("pincode")
        print("latest message intent ",tracker.latest_message['intent'].get('name'))
        # print("slotname", slot_name)
        if (slot_state is None and slot_pincode is None) or tracker.latest_message['intent'].get('name')=='deny':
            dispatcher.utter_message(
            text="Tell me the state/pincode you want to know about")

        
        else:
            dispatcher.utter_message(
            text="Do you want previously calculated results?")

        return []