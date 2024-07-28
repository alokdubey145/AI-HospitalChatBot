pip install python-aiml

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("/content/hospitalChatbot.xml")
kernel.respond("Hospital ChatBot")

while True:
    input_text= input(">You: ")
    response =kernel.respond(input_text)
    print(">System: "+response)
