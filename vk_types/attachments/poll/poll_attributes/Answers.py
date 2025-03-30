class PollsAnswers:
    def __init__(self, answer_id: int, text: str, votes: int, rates: int):
        self.id = answer_id
        self.text = text
        self.votes = votes
        self.rates = rates

    def to_dict(self) -> dict:
        """Returns the poll answers object as a dictionary."""
        return {
            "id": self.id,
            "text": self.text,
            "votes": self.votes,
            "rates": self.rates
        }
