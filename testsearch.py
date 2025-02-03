# from googlesearch import search

# def google_search(question):
#     results = search(question, num_results = 10)

#     for i, result in enumerate(results, start = 1):
#         print(f'Result {i}: {result}')

# question = input("what u wanna kno")

# google_search(question)

#############################

# from openai import OpenAI

# client = OpenAI(api_key = "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")

# prompt = input("what u wanna kno: ")

# chat_completion = client.chat.completions.create(messages=[{"role":"user", "content":prompt}], model = "gpt-4o-mini")

# print(chat_completion.choices[0])

#############Q####################

import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")

GOOGlE_API_KEY = "AIzaSyDEcsH1rPwbhXxyhrzAiD_Ji2jl29HHzkY"

genai.configure(api_key=GOOGlE_API_KEY)

def prompt():
    prompt = input("wut u wnana know: ")
    response = model.generate_content(prompt)
    print(response.text)
    return response

prompt()