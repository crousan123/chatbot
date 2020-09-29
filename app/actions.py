# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class RecordsForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "records_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["date",]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "date": self.from_entity(entity="date"),
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_date(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        if str(value):
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"date": value}
        else:
            dispatcher.utter_template("utter_wrond_date", tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"date": None}

    

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_to_record", tracker)
        return [] 