import openai

commandToClose = "close application"
def Response(messageForGPT):
    openai.api_key = ""

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": "user", "content": messageForGPT
        }])

    print(completion.choices[0].message.content)
    return messageForGPT

def Voice():
    print("Activate Voice")



def VTT():
    print("Voice To Text")
    message = input("Ask your question: ")
    return message

#Code lifecycle
while(Response(VTT()) != commandToClose):
    Voice()

