from prompt_toolkit.completion import Completer, Completion

class ActionsCompleter(Completer):
    def get_completions(self, document, complete_event):
        yield Completion('Execute', start_position=-1 * len(document.text))
        yield Completion('Copy', start_position=-1 * len(document.text))
        yield Completion('Continue', start_position=-1 * len(document.text))