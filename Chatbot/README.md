# Original README by Microsoft Corporation

# With modifications by James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447

A bot that returns an appropriate response back to a user's query.

This bot has been created using [Bot Framework](https://dev.botframework.com), using the echo bot example as a framework.

## Prerequisites

This sample **requires** prerequisites in order to run.

### Install Python 3.6

## Running the sample
To install all dependencies:
- Run `pip install -r requirements.txt` 
- Run `python -m spacy download en_core_web_sm`
Then run `python app.py`


## How to define topics
Each topic is defined with 5 arguments:
- ID: String
- List of patterns: List of lists
- Parents, and their parent-to-child patterns: List of Strings, lists
- Response: String
- Provides a solution: Boolean

- ID
    Define the ID as one unique word

- Patterns
    Use spaCy's pattern definition. This is done with:
    'Linguistic Feature': 'Value'
    A pattern is a list of sets. One word is defined within one set, e.g.
    [{'LEMMA': 'hello'}, {'LEMMA': 'world'}]
    You can give each topic multiple patterns by using a list of lists.
    For more information, see https://spacy.io/usage/linguistic-features 

- Parents, and their parent-to-child patterns
    Define a parent topic by using its ID
    Then, place the relevant patterns in a list, e.g.
    'PARENT_ID', [ [{'LEMMA': 'hello'}, {'LEMMA': 'world'}] ]
    You can also use the pattern of another topic by using its ID, e.g.
    'PARENT_ID', ['HELLO_WORLD']
    You can also use multiple patterns, e.g.
    'PARENT_ID', ['HELLO_WORLD', 'HI_EARTH']
    If the current topic is 'PARENT_ID', then if the user's message contains 'hello world', the topic will change to the child topic
    Make sure to define all parents when relevant! e.g.  
    'PARENT_ID', ['HELLO_WORLD']
    'HELLO_WORLD', ['PARENT_ID']

- Response
    Define the response as a string. The chatbot will message the user with this response when it reaches this topic.

- Provides a solution
    True or False. Define whether the response above is intended to solve the user's query.


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`


## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)