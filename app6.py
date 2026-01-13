import google.generativeai as genai
genai.configure(api_key="gen-lang-client-03517629686")
for model in genai.list_models():
    print(model.name)