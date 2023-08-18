import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    #Buy the Api  from open ai API KEY website and  Keep in the above code API KEY

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens=100,
            temperature = 0.5
        ).choices[0].text
        return response

if __name__ =="__main__":
    chatbot =Chatbot()
    response = chatbot.get_response("Write a joke about birds.")

