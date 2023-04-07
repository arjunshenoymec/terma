# Terma 
Short for Terminal Asistant, Terma is An NLP based CLI application that takes in input from the user in plain language, converts that into an appropriate bash command and finally displays this generated command along with follow up actions that the user can take. 

Inspired from the `Translate to bash` functionality in [fig.io](https://fig.io/).

# Setup

## Pre-requisite
In this primitive version of terma, the queries typed out are sent directly to an [OpenAI](https://openai.com/) model. In order to use the openaI models you would have to [Sign up](https://platform.openai.com/signup) and get a token. 

Once you have obtained a token, you can either set it as an environment variable before you start as shown below. 
```
export OPENAI_TOKEN=<your_token_here>
```
The other option you have is to create a `.terma` file in your home directory and then just add the token there. This approach has the added advantage that you don't have to remember to set the environment variable every time you want to use terma. 

## Instalation
Terma is a python based application and is available in [PyPI](https://pypi.org/project/terma/1.0.1/). This can be installed in any python virtual environment.
```
pip install terma==1.0.1
```

# Usage 
After installing terma it can be used just by specifying the command `terma` in the envrionment in which the package was installed. This starts an interactive CLI session. In the session you can type in the query you have in plain english and the application would generate a CLI query based on that.

![terma example](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzhiNDYxODRkMDAzNTFiNjFjZWUxMGNiM2UxNDc0NzlkODMwNjNmMCZjdD1n/fLIHvZfthjK3GYSxJx/giphy.gif)

As seen in the above image, along with the generated comand terma also gives you choices on what to do with it. You can execute it in the session directly, copy it to the clipboard (for running in another terminal tab or sharing somewhere else) or you can just choose to continue with the conversation. 

To exit press `ctrl-D` or just type `exit()` or `quit()`. 

# Features planned

I have a couple of ideas to improve the user experience around the application:

**Output validation**: In some cases, the openAI model being used generates invalid commands based on the query inputed by the user. One approach that can be used to deal with it is to pass the output from model into another one that performs this sort of validation and ensures that the generated text is a valid os command. 

**Error Explanation** : In case of errors, it would be handy to get an explanation for the errors along
with possible actions to resolve them. 

More suggestions and contributions welcome :) 