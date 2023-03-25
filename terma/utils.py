from terma.config import OPENAI_PARAM_MAPPING, OPENAI_TOKEN, PROMPT_STYLE, USER_INPUT_PROMPT
from terma.translator import Translator
import pyperclip
import subprocess


class TermaUtil:
    """
    Class to coordinate all the activities inside
    the terma prompt session. 
    """
    def __init__(self):
        self.translator = Translator(OPENAI_TOKEN, OPENAI_PARAM_MAPPING)
    
    def translate_query(self, query: str):
        """
        """
        translation = self.translator.translate(query)
        return translation.strip()

    def copy(self, text: str):
        """
        Function that copies what is passed to it
        to the clipboard. 
        """
        pyperclip.copy(text)
        print("Copied to clipboard")

    def execute(self, command: str):
        """
        Function that uses subprocess to execute what
        is passed to it. 
        """
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output.stdout.decode())
        print(output.stderr.decode())

class EmptyResponseException(Exception):
    """
    """
    pass

class UnknownActionException(Exception):
    """
    """
    pass