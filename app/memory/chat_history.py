import json

from app.memory.redis_client import get_redis


class ChatHistory:

    def __init__(self):
        self.redis = get_redis()

    def load(self, session_id: str):

        history = self.redis.get(session_id)

        if history:
            return json.loads(history)

        return []

    def save(
        self,
        session_id: str,
        history: list,
    ):

        self.redis.set(
            session_id,
            json.dumps(history),
        )