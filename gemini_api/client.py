import google.generativeai as genai
import os

# Essa configuração é para utilizar o Gemini da Google para gerar a bio dos veículos automaticamente.
# link: https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br&amp%3Bauthuser=3&amp%3Blang=python&lang=python

def get_car_ai_bio(model_vehicle, brand, year):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # obs: Use uma variável de ambiente para a chave da API
    model = genai.GenerativeModel('gemini-1.5-flash') 
    
    prompt = (
        f"Crie uma descrição de venda para o veículo {model_vehicle} {brand} {year}."
        f"Limite a descrição a 300 caracteres, mesmo que fictício."
    )
    
    response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=300
        )
    )
    
    return response.text
