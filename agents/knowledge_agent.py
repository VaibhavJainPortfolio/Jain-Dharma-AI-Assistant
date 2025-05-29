# agents/knowledge_agent.py

from openai import OpenAI
import os

def get_prompt(question, language):
    if language == "Hindi":
        return f"""
आप जैन धर्म के एक विद्वान हैं और आपको जिनवाणी, जैन शास्त्र और अन्य धार्मिक पुस्तकों का गहरा ज्ञान है।
आपसे पूछा गया प्रश्न यह है: "{question}"
कृपया इसका उत्तर बहुत ही सरल और स्पष्ट हिन्दी में दें, और जहाँ हो सके, जैन सिद्धांतों का उल्लेख करें।
        """
    else:
        return f"""
You are a Jain Dharma expert with deep knowledge of scriptures like Jinwani and Jain Shastras.
Please answer this question: "{question}"
Keep your answer very simple and clear, and mention Jain principles wherever appropriate.
        """

def get_jain_answer(api_key, question, language):
    try:
        client = OpenAI(api_key=api_key)
        prompt = get_prompt(question, language)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant well-versed in Jain religion."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"