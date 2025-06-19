from collections import deque

class ChatMemory:
    def __init__(self, max_turns=3):
        self.memory = deque(maxlen=max_turns)

    def add_exchange(self, user_input, bot_response):
        self.memory.append((user_input, bot_response))

    def get_context(self):
        context = ""
        for user, bot in self.memory:
            context += f"User: {user}\nBot: {bot}\n"
        return context
