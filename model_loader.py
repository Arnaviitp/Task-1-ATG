from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_model(model_name="google/flan-t5-small"):
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    chat_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return chat_pipeline
