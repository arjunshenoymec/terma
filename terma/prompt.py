from terma.config import PROMPT_STYLE, USER_INPUT_PROMPT
from terma.completer import ActionsCompleter
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text


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
    
    def get_query_from_user(self):
        """
        Get the initial query from the user.

        Returns
        -------
        A plain text string denoting what the user wants
        """
        text = self.session.prompt(USER_INPUT_PROMPT, style=PROMPT_STYLE, validator=None)
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
                                              pre_run=self.session.default_buffer.start_completion)
        self.session.complete_while_typing=False
        return selected_option
    