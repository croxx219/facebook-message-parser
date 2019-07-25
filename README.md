# Facebook Messages Parser
This is a utility that parses Facebook messages after they have been downloaded in json format.

## Assumptions:
1. The messages have been downloaded as outlined [here](https://www.zapptales.com/en/download-facebook-messenger-chat-history-how-to/)
2. A file named `message.json` has been moved to the same level as `parse.py`. Note that the download includes many
 files, make sure to select the conversation history (contact) you care about.
3. Run `parse.py` as python2. 

**NOTE:** Some libraries might be missing so make sure to run a virtualenv and install
 them.
 
 
 At the end you will get an HTML file with a curated output of the json conversation.
 
 **IMPORTANT:** Anything that is not a message (image, gif, sticker...) will NOT be parsed and written to the HTML.