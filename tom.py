import openai

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

def chat_with_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",  # You can choose other engines as well
            prompt=prompt,
            max_tokens=50,  # Adjust this value based on your desired response length
            stop=None,  # You can specify stop words to end the response
            temperature=0.7,  # Adjust temperature for creativity (0.2 for focused, 1.0 for random)
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print("Welcome to the OpenAI Chatbot!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        response = chat_with_openai(user_input)
        print("Chatbot:", response)
