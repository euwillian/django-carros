import google.generativeai as genai

# Essa configuração é para utilizar o Gemini da Google para gerar a bio dos veículos automaticamente.
# link: https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br&amp%3Bauthuser=3&amp%3Blang=python&lang=python

def get_car_ai_bio(model_vehicle, brand, year):
    genai.configure(api_key="AIzaSyAdi2JhwsA_OOL4ahq7y2VUJExA5Csf2hE")
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = (
        f"Crie uma descrição de venda para o veículo {model_vehicle} {brand} {year}."
        f"Limite a descrição a 300 caracteres, mesmo que fictício."
    )
    
    response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=1000
        )
    )
    
    return response.text
