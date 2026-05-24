from collections import Counter
import re
from modules.skill_extractor import load_nlp_model


def keyword_frequency(text, top_n=15):
    nlp = load_nlp_model()
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    counts = Counter(tokens)
    top_keywords = counts.most_common(top_n)
    import pandas as pd

    return pd.DataFrame(top_keywords, columns=["Keyword", "Frequency"])
