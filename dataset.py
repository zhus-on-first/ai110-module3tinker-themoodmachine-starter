"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# --- Additional posts and labels ---
SAMPLE_POSTS += [
    "Lowkey stressed but kind of proud of myself",
    "I absolutely love when my wifi cuts out mid-call",
    "just found a $20 in my old jacket 😂",
    "cant believe i have to do this again 💀",
    "It is what it is",
    "no cap this was the best meal of my life",
    "im fine. totally fine. everything is fine :)",
    "tired but we keep going I guess 🥲",
    "highkey obsessed with this new song",
    "woke up late, spilled my coffee, missed the bus",
]

TRUE_LABELS += [
    "mixed",     # "Lowkey stressed but kind of proud of myself"
    "negative",  # "I absolutely love when my wifi cuts out mid-call"
    "positive",  # "just found a $20 in my old jacket 😂"
    "negative",  # "cant believe i have to do this again 💀"
    "neutral",   # "It is what it is"
    "positive",  # "no cap this was the best meal of my life"
    "mixed",     # "im fine. totally fine. everything is fine :)"
    "mixed",     # "tired but we keep going I guess 🥲"
    "positive",  # "highkey obsessed with this new song"
    "negative",  # "woke up late, spilled my coffee, missed the bus"
]

assert len(SAMPLE_POSTS) == len(TRUE_LABELS), (
    f"Mismatched dataset: {len(SAMPLE_POSTS)} posts vs {len(TRUE_LABELS)} labels"
)
