from collections import Counter
import pandas as pd


def keyword_frequency(text):

    if not text:

        return pd.DataFrame(
            columns=["Keyword", "Count"]
        )

    words = text.lower().split()

    filtered_words = []

    stop_words = {

        "the",
        "and",
        "is",
        "in",
        "to",
        "of",
        "for",
        "a",
        "on",
        "with",
        "as",
        "by",
        "an",
        "at"

    }

    for word in words:

        clean_word = word.strip(
            ".,!?():;/"
        )

        if (
            len(clean_word) > 2
            and clean_word not in stop_words
        ):

            filtered_words.append(
                clean_word
            )

    counter = Counter(
        filtered_words
    )

    most_common = counter.most_common(10)

    return pd.DataFrame(

        most_common,

        columns=[
            "Keyword",
            "Count"
        ]

    )