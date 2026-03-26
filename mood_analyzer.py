# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""
import string

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

        # Starter mapping of emojis to words.
        self.EMOJI_MAP = {
              "😂": "funny",
              "🥲": "sad",
              "💀": "exhausted",
              ":)": "happy",
              ":-)": "happy",
              ":(": "sad",
              ":-(": "sad",
        }

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")

        Ideas to improve:
          - Handle more emojis and slang (for example "lol" or "sigh" or "smh")
          - Normalize repeated characters ("soooo" -> "soo")
        """

        for emoji, replacement in self.EMOJI_MAP.items():
            text = text.replace(emoji, f" {replacement} ")

        cleaned = text.strip().lower().translate(str.maketrans("", "", ".,!?;:\"()"))
        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    # Words that flip the sentiment of the next word.
    NEGATORS = {"not", "never", "no"}

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score; negative words decrease it.
        Enhancement: simple negation — "not happy" scores -1, "not bad" scores +1.

        See the alternative implementations below for a readability comparison.
        """
        # --- Version A: Simple baseline (most readable, no negation) ----------
        tokens = self.preprocess(text)
        score = 0
        for token in tokens:
            if token in self.positive_words:
                score += 1
            elif token in self.negative_words:
                score -= 1
        return score
        # Correctness gap: "not happy" → +1 (wrong; expected -1)

        # --- Version B: Negation via index ------------
        # Readable because the index makes "look at the previous word" explicit.
        # tokens = self.preprocess(text)
        # score = 0
        # for i, token in enumerate(tokens):
        #     multiplier = -1 if i > 0 and tokens[i - 1] in self.NEGATORS else 1
        #     if token in self.positive_words:
        #         score += multiplier
        #     elif token in self.negative_words:
        #         score -= multiplier
        # return score

        # --- Version C: Negation via bigram zip (idiomatic Python) ------------
        # Concise, but requires familiarity with the zip sliding-window pattern.
        # Correctness is identical to Version B.
        # tokens = self.preprocess(text)
        # score = 0
        # for prev, curr in zip([""] + tokens[:-1], tokens):
        #     multiplier = -1 if prev in self.NEGATORS else 1
        #     if curr in self.positive_words:
        #         score += multiplier
        #     elif curr in self.negative_words:
        #         score -= multiplier
        # return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        score = self.score_text(text)
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
