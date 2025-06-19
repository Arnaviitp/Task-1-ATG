from model_loader import load_model
from chat_memory import ChatMemory

def main():
    chat_pipeline = load_model()
    memory = ChatMemory(max_turns=3)

    print("Welcome to Local CLI Chatbot! Type /exit to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        context = memory.get_context() + f"User: {user_input}\nBot:"
        prompt = f"{context} {user_input}"
        response = chat_pipeline(prompt, max_new_tokens=100)[0]["generated_text"]
        print(f"Bot: {response.strip()}")
        memory.add_exchange(user_input, response.strip())

if __name__ == "__main__":
    main()
