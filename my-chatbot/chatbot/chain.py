# LangChain chain / LLM setup
import re
import requests
from chatbot.config import SARVAM_API_KEY

API_URL = "https://api.sarvam.ai/v1/chat/completions"

def get_chatbot_response(user_input):

    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sarvam-m",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            # Strip internal reasoning tags from the model output
            content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
            return content
        else:
            return f"API Error {response.status_code}: {response.text}"

    except requests.exceptions.ConnectionError:
        return "❌ Connection error. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "❌ Request timed out. Please try again."
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
