class PollsAnswer:
    def __init__(self, answer_id: int, text: str, votes: int, rate: int):
        self.id = answer_id
        self.text = text
        self.votes = votes
        self.rate = rate

    def to_dict(self) -> dict:
        """Returns the poll answer object as a dictionary."""
        return {
            "id": self.id,
            "text": self.text,
            "votes": self.votes,
            "rate": self.rate
        }
