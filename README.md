# Terma 
Short for Terminal Asistant, Terma is An NLP based CLI application that takes in input from the user in plain language, converts that into an appropriate bash command and finally displays this generated command along with follow up actions that the user can take. 

# Installation

# Pre-requisite
In this primitive version of terma, the queries typed out are sent directly to an [OpenAI](https://openai.com/) model. In order to use the openaI models you would have to [Sign up](https://platform.openai.com/signup) and get a token. 

Set the token as an environment variable before you start

```
export OPENAI_TOKEN=<your_token_here>
```

# Usage 
After installing terma it can be used just by specifying the command `terma` in the envrionment in which the package was installed. This starts an interactive CLI session. In the session you can type in the query you have in plain english and the application would generate a CLI query based on that.

![terma example](https://giphy.com/gifs/terma-jyKHGxzI9JvcIdkywS)

As seen in the above image, along with the generated comand terma also gives you choices on what to do with it. You can execute it in the session directly, copy it to the clipboard (for running in another terminal tab or sharing somewhere else) or you can just choose to continue with the conversation. 

To exit press `ctrl-D` or just type `exit()` or `quit()`. 
