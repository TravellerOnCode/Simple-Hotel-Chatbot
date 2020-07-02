# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta

from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted, AllSlotsReset



"""
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         
         dispatcher.utter_message(text='Hello World !')

         return []
"""

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_send_clean_service"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         times = tracker.latest_message['entities']
         print(times)
         h = m = 0
         if times[0]['value'] == 'now':
             
             print('I am here !')
             response_text = "Sure, I am sending someone right now."
         else:
             #s = (times[0]['value']).split(" ")     
             t = int(times[0]['value'])
             tt = (times[1]['value'])
             if tt[0] == 'h' or tt[0] == 'H' :
                 h = t
             else:
                 m = t
             #Adding and adjusting to Indian Timezone
             h = h
             m = m
             print(datetime.now())
             d = (datetime.now() + timedelta(hours=h,minutes=m)).strftime('%H:%M')
                 
             response_text = "Sure, scheduling a cleaning service at " + d
                 
         
         #response_text = 'Hello from Action !'
         dispatcher.utter_message(text=response_text)

         return []
     
           

class ActionRoomBookingForm(FormAction):
    
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "roombooking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["roomcount", "roomtype"]
    
    
    """
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        
        
        return {"roomcount": [self.from_entity(entity="roomcount"),
                         self.from_text()],
            "roomtype": [self.from_entity(entity="roomtype"),
                         self.from_text()]
            }
    """



    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        
        
    
        dispatcher.utter_message(template='utter_submit')
    
        return [AllSlotsReset()]
    
    
class ActionApologize(Action):

    def name(self):
        return "action_apologize"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_apologize", tracker)
        return [UserUtteranceReverted()]
    
    
      

