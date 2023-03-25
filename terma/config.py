import os
from prompt_toolkit.styles import Style

# Open ai token to access the openai endpoints
OPENAI_TOKEN = os.environ["OPENAI_TOKEN"]

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