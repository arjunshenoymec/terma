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
        if "|" in command:
            output, error = _piped_execution(command)
        else:
            output, error = _individual_execution(command)
        if(output):
            print(output.decode('utf-8'))
        if(error):
            print(error.decode('utf-8'))

class EmptyResponseException(Exception):
    """
    """
    pass

class UnknownActionException(Exception):
    """
    """
    pass

def _individual_execution(command):
    """
    Function to trigger an exceution of an indvidual
    command. 
    eg: "ls", "python -i", "ps -ef"
    """
    process = subprocess.Popen(command.split(' '))
    process.wait()
    return process.communicate()

def _piped_execution(command):
    """
    Function to trigger an execution of a command
    which has multiple subcommands grouped together
    via pipes

    eg: "ls -l | grep abc", "cat abc.txt | awk -4" 
    """
    sub_commands = [x.strip() for x in command.split('|')]
    current_input = None
    current_process = None
    for x in sub_commands:
        current_process = subprocess.Popen(x.split(' '),
                                           stdin=current_input,
                                           stdout=subprocess.PIPE)
        current_process.wait()
        current_input = current_process.stdout
    return current_process.communicate()
