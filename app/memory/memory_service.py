from app.memory.chat_history import ChatHistory


class MemoryService:

    def __init__(self):
        self.history = ChatHistory()

    def load_memory(self, session_id):

        return self.history.load(session_id)

    def save_memory(
        self,
        session_id,
        question,
        answer,
    ):

        history = self.history.load(session_id)

        history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        self.history.save(
            session_id,
            history[-20:],
        )