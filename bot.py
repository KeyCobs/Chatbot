import openai
import constants
import TextToVoice
import VoiceToText
import sys
import install as i

i.checkinstall()

prompt = [
            {"role": "system", "content": "You are a test bot to see if you work using the API. There are a few checks you need to fufill"},
            {"role": "system", "content": "You need to complete the following. 1. Remember our chat history, 2. Have voice to text, 3. Have text to voice, 4. Create multiple bots, 5. Make them interact with each other"},
            {"role": "system", "content": "You have successfully completed the first task"},
        ]

response = "non"
commandToClose = "x"

def Response(messageForGPT):
    if messageForGPT != commandToClose:
        openai.api_key = constants.chatGPT_APIKey
        
        prompt.append({
            "role": "user", "content": messageForGPT
        })

        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=prompt
        )
        print(completion.choices[0].message.content)
        response = completion.choices[0].message.content

        prompt.append
        ({
            "role": "system", "content": response
        })

        TextToVoice.TTV(response)
    else:
        #close script
        sys.exit()

def Voice():
    print("Activate Voice")



def VTT():
    print("Voice To Text:\n Press T to start talking")
    message = input()
    if message =='t' or message =='T':
        message = VoiceToText.voice_to_text()
    elif message == 'x' or message == 'X' or message == commandToClose:
        message = commandToClose
    else:
        print('ERROR You pressed' + str(message) + ' instead of t, T, x or X. Text was not send.')
        VTT()
   

    return message

#Code lifecycle
while(True):
    Response(VTT())
    Voice()

