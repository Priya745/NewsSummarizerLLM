from langchain.chat_models import init_chat_model

GOOGLE_API_KEY = "AIzaSyAyCaaYlr9QNMLWY9DpLBdX37Q6u7Gyclw"

model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GOOGLE_API_KEY
)

response = model.invoke("how are you?")
response_str = response.content
print(response_str)