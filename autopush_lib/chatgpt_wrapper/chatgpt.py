import openai

RESPONSE_ERR_MSG = "I don't have answer for this"


class ChatGPT:
    def __init__(self, model_engine, openai_api_key):
        openai.api_key = openai_api_key
        self.model_engine = model_engine
        self.open_api_key = openai_api_key
        self.response_on_error = RESPONSE_ERR_MSG

    def ask(self, question):
        ai_response = openai.Completion.create(
            engine=self.model_engine,
            prompt=question,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return ai_response.choices[0].text or self.response_on_error
