from openai import OpenAI
from database import chat_history

client = OpenAI(api_key="PUT_OPENAI_KEY")

SYSTEM_PROMPT = """
أنت مساعد معلومات أدوية فقط.
اشرح الاستخدامات والأعراض والتحذيرات.
لا تعطي وصفات علاج.
"""

def ask_ai(user_id, message):
    chat_history[user_id].append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *chat_history[user_id][-5:]
            ]
        )

        answer = response.choices[0].message.content
        chat_history[user_id].append({"role": "assistant", "content": answer})
        return answer

    except Exception as e:
        return "⚠️ خطأ مؤقت"
