import openai

# Set up OpenAI API credentials
openai.api_key = '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'


def generate_response(message):
    try:
        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )

        response = completion.choices[0].message["content"]

        if response:
            return response
        else:
            return 'Failed to generate response!'

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = generate_response(user_input)
        print(f"AI:{response}")