import openai
import constants
import sys

prompt = [
            {"role": "system", "content": "You are a test bot to see if you work using the API. There are a few checks you need to fufill"},
            {"role": "system", "content": "You need to complete the following. 1. Remember our chat history, 2. Have voice to text, 3. Have text to voice, 4. Create multiple bots, 5. Make them interact with each other"}
         ]

response = "non"

commandToClose = "x"

def Response(messageForGPT):
    if messageForGPT != commandToClose:
        openai.api_key = constants.api_Key
        
        prompt.append({
            "role": "user", "content": messageForGPT
        })

        print(prompt)

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
        return response
    
    else:
        #close script
        sys.exit()

def Voice():
    print("Activate Voice")



def VTT():
    print("Voice To Text")
    message = input("Ask your question: ")
    return message

#Code lifecycle
while(True):
    Response(VTT())
    Voice()

