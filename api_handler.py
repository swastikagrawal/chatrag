from groq import Groq
from config import GROQ_API_KEY, SYSTEM_PROMPT


client = Groq(api_key=GROQ_API_KEY)


def get_answer(question, chunks, model):
    context = ""
    for chunk in chunks:
        context += chunk["chunk"] + "\n\n"

    user_message = "Context:\n" + context + "\nQuestion:\n" + question

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content

    except Exception as e:
        error = str(e).lower()
        if "rate limit" in error:
            return "RATE_LIMIT"
        if "model" in error:
            return "MODEL_UNAVAILABLE"
        return "ERROR"