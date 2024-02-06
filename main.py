import openai

openai.api_key= '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'

def generate_voice_assistant_prompt(prompt):
    response = openai.Completion.create(
        engine='davinci',  # Ganti dengan model yang sesuai
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        return_prompt=False,
        echo=False
    )
    return response.choices[0].text.strip()

prompt = "Halo, apa yang bisa saya bantu?"
response = generate_voice_assistant_prompt(prompt)
print(response)

