from prompt_toolkit import print_formatted_text, PromptSession
from terma.utils import TermaUtil
from terma.utils import EmptyResponseException, UnknownActionException
from terma.prompt import PromptInterface
from terma.config import PROMPT_STYLE, MOTD


def coordinate(terma_util, action, command):
    if action == 'Continue':
        return True
    elif action == 'Copy':
        terma_util.copy(command)
    elif action == 'Execute':
        terma_util.execute(command)
    else:
        raise UnknownActionException()

def interact_with_user(prompt_interface, terma_util):
    """
    """
    user_query = prompt_interface.get_query_from_user()
    if not user_query:
        return True
    if user_query == 'quit()' or user_query == 'exit()':
        raise EOFError
    response = terma_util.translate_query(user_query)
    if not response:
        raise EmptyResponseException()
    # prompt_interface.print_to_prompt(response)
    choice = prompt_interface.get_user_choice(response)
    try:
        coordinate(terma_util, choice, response)
    except UnknownActionException:
        print('Unknown follow up action asked of me, so doing nothing instead')


def main():
    """
    """
    print(MOTD)
    session = PromptSession(style=PROMPT_STYLE)
    prompt_interface = PromptInterface(session)
    terma_util = TermaUtil()
    while True:
        try:
            interact_with_user(prompt_interface, terma_util)
        except KeyboardInterrupt:
            print_formatted_text('\n KeyboardInterrupt')
        except EOFError:
            print_formatted_text('\n Exiting...')
            break
        except EmptyResponseException:
            print_formatted_text('\n Unable to translate query please rephrase what you want to do')
            continue


if __name__ == "__main__":
    main()