import openai
import platform

__all__ = ("Translator")

class Translator(object):
    """
    """
    def __init__(self, token: str, param_mapping: dict):
        openai.api_key = token
        self._params = param_mapping
        self.os_name = platform.system()

    def translate(self, query):
        """
        """
        if not query:
            return None
        prompt = f"Convert this text to a programmatic command in {self.os_name}: {query}"
        self._params['prompt'] = prompt
        response = openai.Completion.create(**self._params)
        if response.choices:
            return response.choices[0].text
        else: 
            return None