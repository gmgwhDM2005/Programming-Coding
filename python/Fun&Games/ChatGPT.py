import openai

openai.api_key="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"
while True:
    user_input=input('What would you like to ask?\n>: ')
    output=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content":user_input}]
    )
    new_response = [i.replace('\n', '') for i in output.choices[0].message.content.strip()]
    print(f"\nBot: {''.join(new_response)}\n")
