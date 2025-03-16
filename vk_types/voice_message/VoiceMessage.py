class VoiceMessage:
    def __init__(self, voice_message_id: int, owner_user_id: int, duration: int,
                 waveform: list[int], link_ogg: str, link_mp3: str):
        """
        Represents a voice message.

        :param voice_message_id: Unique identifier of the voice message.
        :param owner_user_id: ID of the user who owns the voice message.
        :param duration: Duration of the voice message in seconds.
        :param waveform: Array of integers representing the waveform of the audio message.
        :param link_ogg: URL to the .ogg version of the audio message.
        :param link_mp3: URL to the .mp3 version of the audio message.
        """
        self.voice_message_id = voice_message_id
        self.owner_user_id = owner_user_id
        self.duration = duration
        self.waveform = waveform
        self.link_ogg = link_ogg
        self.link_mp3 = link_mp3

    def to_dict(self) -> dict:
        """Returns the VoiceMessage object as dictionary"""
        return {
            "voice_message_id": self.voice_message_id,
            "owner_user_id": self.owner_user_id,
            "duration": self.duration,
            "waveform": self.waveform,
            "link_ogg": self.link_ogg,
            "link_mp3": self.link_mp3
        }
