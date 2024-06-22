from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

class Middle(BaseMiddleware):
    def __init__(self):
        self.id = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if self.id == 0:
            self.id = event.message_id
        else:
            data['prev'] = self.id
            self.id = event.message_id
        return await handler(event, data)
