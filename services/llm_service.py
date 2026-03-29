from tavily import TavilyClient
from openai import OpenAI
from config.settings import OPENAI_API_KEY, TAVILY_API_KEY, MODEL


tavily = TavilyClient(api_key=TAVILY_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

def search_diabetes_knowledge(query: str):

    response = tavily.search(
        query=query + " diabetes medical guidance",
        search_depth="advanced",
        max_results=5
    )

    results = []

    for r in response["results"]:
        results.append({
            "title": r["title"],
            "content": r["content"],
            "url": r["url"]
        })

    return results

def build_prompt(question: str, context: str):

    prompt = f"""
You are a medical AI assistant specialized in diabetes care.

Your job is to help diabetes patients understand their condition and guide them
on safe actions they can take.

Use the medical information provided in the context below.

If the question involves emergencies (severe hypoglycemia, diabetic ketoacidosis,
loss of consciousness), advise the patient to seek immediate medical care.

Always explain:

1. What is happening medically
2. Why it happens in diabetes
3. What the patient should do
4. When they must contact a doctor

Context:
{context}

Patient Question:
{question}

Provide a clear structured answer.
"""

    return prompt

def ask_model(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert diabetes clinical assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def diabetes_rag(question: str):

    context_docs = search_diabetes_knowledge(question)

    context = ""

    for doc in context_docs:
        context += f"""
Title: {doc['title']}
Content: {doc['content']}
Source: {doc['url']}

"""

    prompt = build_prompt(question, context)

    answer = ask_model(prompt)

    return {
        "answer": answer,
        "sources": context_docs
    }

