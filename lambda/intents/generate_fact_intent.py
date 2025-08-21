from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
import random


class GenerateFactIntentHandler(AbstractRequestHandler):
    """Handler for Generate Fact Intent."""
    unfun_facts: list[str]
    def __init__(self, unfun_facts: list[str]):
        self.unfun_facts = unfun_facts
        super().__init__()

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("GenerateFactIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        fact = random.choice(self.unfun_facts)
        speak_output = fact

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask("Would you like to hear another unfun fact?")
            .response
        )
