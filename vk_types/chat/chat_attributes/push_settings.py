from datetime import datetime


class ChatsPustSettings:
    def __init__(self, sound: bool, disabled_until_unix: int):
        """
        Represents an attribute PushSettings of object Chat

        :param sound: Is sound notifications available
        :param disabled_until_unix: Until which time the sound notifications are disabled(in unix_time)
        """
        self.sound = sound
        self.is_disabled, self.disabled_until_datetime = ChatsPustSettings.count_disabled(disabled_until_unix)

    @staticmethod
    def count_disabled(disabled_until_unix: int):
        if disabled_until_unix == -1:
            is_disabled = True
            disabled_until_datetime = None
        else:
            is_disabled = False
            disabled_until_datetime = datetime.fromtimestamp(disabled_until_unix)
        return is_disabled, disabled_until_datetime

