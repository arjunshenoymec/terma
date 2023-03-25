# Terma 
Short for Terminal Asistant, Terma is An NLP based CLI application that takes in input from the user in plain language, converts that into an appropriate bash command and finally displays this generated command along with follow up actions that the user can take. 

# Setup
## Pre-requisite
In this primitive version of terma, the queries typed out are sent directly to an [OpenAI](https://openai.com/) model. In order to use the openaI models you would have to [Sign up](https://platform.openai.com/signup) and get a token. 

Once you have obtained a token, you can either set it as an environment variable before you start as shown below. 
```
export OPENAI_TOKEN=<your_token_here>
```
The other option you have is to create a `.terma` file in your home directory and then just add the token there. This approach has the added advantage that you don't have to remember to set the environment variable every time you want to use terma. 

# Usage 
After installing terma it can be used just by specifying the command `terma` in the envrionment in which the package was installed. This starts an interactive CLI session. In the session you can type in the query you have in plain english and the application would generate a CLI query based on that.

![terma example](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzhiNDYxODRkMDAzNTFiNjFjZWUxMGNiM2UxNDc0NzlkODMwNjNmMCZjdD1n/fLIHvZfthjK3GYSxJx/giphy.gif)

As seen in the above image, along with the generated comand terma also gives you choices on what to do with it. You can execute it in the session directly, copy it to the clipboard (for running in another terminal tab or sharing somewhere else) or you can just choose to continue with the conversation. 

To exit press `ctrl-D` or just type `exit()` or `quit()`. 
