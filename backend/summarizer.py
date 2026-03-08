from transformers import pipeline

# lightweight fast model
summarizer = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def summarize_text(text):
    prompt = f"Summarize the following lecture in clear bullet points:\n{text}"

    result = summarizer(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )

    return result[0]["generated_text"]