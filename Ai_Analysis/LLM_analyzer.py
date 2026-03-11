import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_alerts(alerts):
    if not alerts:
        return "No threats detected. Your system looks safe."

    prompt = "Analyze these security alerts and explain them as a SOC analyst:\n\n"
    for alert in alerts:
        prompt += str(alert) + "\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI analysis failed: {e}"
