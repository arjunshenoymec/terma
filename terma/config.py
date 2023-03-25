import os
from prompt_toolkit.styles import Style

def _get_token():
    '''
    Function to retrieve the OpenAI
    token from either the .terma file
    or from the envrionment as a env variable.
    '''
    home_dir = os.path.expanduser("~")
    terma_config_file = '.terma'
    config_file_path = os.path.join(home_dir, terma_config_file)
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            token = f.readline()
    else:
        token = os.environ["OPENAI_TOKEN"]
    return token.strip() if token else None

# Open ai token to access the openai endpoints
OPENAI_TOKEN = _get_token()

# OpenAI model parameters that will be used while
# querying the openai endpoint
OPENAI_PARAM_MAPPING = {
    "model": "text-davinci-003",
    "prompt": "",
    "temperature": 0.7,
    "max_tokens": 100,
    "top_p": 1,
    "frequency_penalty": 0.2,
    "presence_penalty": 0
}


PROMPT_STYLE = Style.from_dict({
    # User input (default text).
    '':          '#00ff88',
    # Prompt.
    'username': '#884444',
    'pound':    '#00aa11 bold',
    'response': '#ff0066 bold',
    'terma': '#33FFB2',
    'action_choice': 'hidden'
})

USER_INPUT_PROMPT = [
    ('class:username', os.getlogin()),
    ('class:pound',    ' \u276F\u276F '),
]

MOTD = "Starting terma session \npress Ctrl+D or type \"quit()\" to exit"