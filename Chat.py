#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openai
openai.api_key = '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'
messages = [ {"role": "system", "content":
            "You are an intelligent gardening assistant."} ]
while True:
    message = input("User : ")
    message = "Only answer questions related to gardening. Do not give suggestions if the question is unrelated to gardening. " + message
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


# In[ ]:




