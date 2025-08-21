from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
import random

from unfun_facts.unfun_facts import unfun_facts

class GenerateFactIntentHandler(AbstractRequestHandler):
    """Handler for Generate Fact Intent."""
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("GenerateFactIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        fact = random.choice(unfun_facts)
        speak_output = fact

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Would you like to hear another unfun fact?")
                .response
        )