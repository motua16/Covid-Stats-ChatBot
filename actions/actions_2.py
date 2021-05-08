import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

class ActionEntity(Action):

    def name(self) -> Text:
        return "action_get_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_name = tracker.get_slot("name")

        print("slotname", slot_name)
        if slot_name is None:
            dispatcher.utter_message(
            text="hi what is your name?")

        
        else:
            dispatcher.utter_message(
            text="hi what can I do for you " + slot_name+"?")

        return []