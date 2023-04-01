from terma.config import PROMPT_STYLE, USER_INPUT_PROMPT
from terma.completer import ActionsCompleter
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.validation import Validator


class PromptInterface:
    """
    Interface used to interact with the user
    via the CLI. The object will be responsible for
    getting inputs from the user and displaying all outputs. 
    """
    def __init__(self, session):
        """
        Sets the session, also intialises the
        completer used to present the set of choices to the
        user. 

        Parameters
        ----------
        session: The prompt_toolkit session.
        """
        self.session = session
        self.completer = ActionsCompleter()
        self.choiceValidator = Validator.from_callable(
            self._choice_validator,
            error_message='Invalid Followup action',
            move_cursor_to_end=True)
        self.defaultValidator = Validator.from_callable(
            self._non_empty_string_validator,
            error_message='Non empty string not proper input',
            move_cursor_to_end=True)

    def _choice_validator(self, text):
        """
        Function to validate the choice
        for followup action selected/written
        by the user. 
        """
        choices = ['Execute', 'Copy', 'Continue']
        return text in choices

    def _non_empty_string_validator(self, text):
        """
        The default validator to be used.
        It should only alert when input is empty
        """
        if not bool(text):
            return False
        else:
            return not text.isspace()
    
    def get_query_from_user(self):
        """
        Get the initial query from the user.

        Returns
        -------
        A plain text string denoting what the user wants
        """
        text = self.session.prompt(USER_INPUT_PROMPT, style=PROMPT_STYLE, validator=self.defaultValidator)
        return text

    def print_to_prompt(self, text: str):
        """
        Print a given response to the terminal. 
        """
        response_text = FormattedText([('class:response', text),])
        print_formatted_text(response_text, style=PROMPT_STYLE)
    
    def get_user_choice(self, text: str):
        """
        Enable completion to True
        Generates an automatic dropdown list of suggestions
        Enable completion to False

        Parameters
        ----------
        text: The text to be displayed before showing the dropdown

        Returns
        -------
        choice (str): follow up action choice
        """
        response_text = FormattedText([('class:response', f'{text} '),])
        self.session.complete_while_typing=True
        selected_option = self.session.prompt(response_text, completer=self.completer,
                                              pre_run=self.session.default_buffer.start_completion,
                                              validator=self.choiceValidator)
        self.session.complete_while_typing=False
        return selected_option
    