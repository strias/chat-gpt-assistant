import os
from typing import List

from loguru import logger
import openai
from dotenv import load_dotenv

load_dotenv()


class OpenAI:

    _client = openai
    _client.organization = os.getenv("OPENAI_ORGANIZATION")
    _client.api_key = os.getenv("OPENAI_API_KEY")

    _usage: int = 0

    def chat_completion_messages(self, messages: List[dict], log: bool = True) -> str:
        response = self._client.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages
        )
        if log:
            logger.info(response)
        self._usage += response['usage']['total_tokens']
        return dict(response.choices[0]['message'])

    """
    messages = [
        {"role": "system", "content": ""},
        {"role": "assistant", "content": ""},
        {"role": "user", "content": ""}
    ]
    """

    def get_usage(self):
        return self._usage
