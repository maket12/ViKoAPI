class VoiceMessage:
    def __init__(self, duration: int, waveform: list[int], link_ogg: str, link_mp3: str):
        self.duration = duration
        self.waveform = waveform
        self.link_ogg = link_ogg
        self.link_mp3 = link_mp3

    def to_dict(self) -> dict:
        """Returns the voice message object as a dictionary."""
        return {
            "duration": self.duration,
            "waveform": self.waveform,
            "link_ogg": self.link_ogg,
            "link_mp3": self.link_mp3
        }
