from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from src.functions import start, add_group
from src.logger_handler import get_logger


class TelegramBot:
    def __init__(self, bot_token: str):
        self._token = bot_token
        self.logger = get_logger(__file__)

    def init_updater(self) -> Updater:
        return Updater(token=self.token, use_context=True)

    @staticmethod
    def registry_command_handler(updater: Updater, command: str, fun: callable):
        command_handler = CommandHandler(command, fun)
        updater.dispatcher.add_handler(command_handler)

    @staticmethod
    def registry_message_handler(updater: Updater, fun: callable):
        add_group_handle = MessageHandler(Filters.status_update.new_chat_members, fun)
        updater.dispatcher.add_handler(add_group_handle)

    @property
    def token(self):
        return self._token

    def run(self):
        self.logger.info("Initiating bot...")
        updater = self.init_updater()
        self.logger.info("Let's registry commands...")
        self.registry_command_handler(updater, "go", start)
        self.registry_message_handler(updater, add_group)
        self.logger.info("Running...")
        updater.start_polling()
        updater.idle()
        self.logger.info("Bot out!")
        updater.stop()


if __name__ == "__main__":
    token = input("Please insert bot Token: ")
    wedding_bot = TelegramBot(token)
    wedding_bot.run()

