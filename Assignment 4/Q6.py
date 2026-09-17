"""
Q6) Modify your Q2 scoring function so that if two or more entries tie for the highest
score, it does not silently pick one - it prints all matching entries instead, so the
user can see every equally good match. Demonstrate with one query that produces a tie
(e.g. a query matching both "fee" entries) and one that doesn't.
"""

import pandas as pd

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee", "category": "billing"},
]

personalized_entries = [
    {"question": "why was my payment declined", "answer": "Your payment may be declined due to insufficient balance or a bank server issue.",
     "keywords": "payment declined failed", "category": "billing"},
    {"question": "how do i get a refund for the annual fee", "answer": "Refunds are processed within 7 working days after approval.",
     "keywords": "refund fee return", "category": "billing"},
]

faq_entries = fixed_entries + personalized_entries
df = pd.DataFrame(faq_entries)


def score_query(query, df):
    query_words = set(query.lower().split())
    scores = []
    for _, row in df.iterrows():
        entry_words = set(row["question"].lower().split()) | set(row["keywords"].lower().split())
        score = len(query_words & entry_words)
        scores.append(score)
    result = df.copy()
    result["confidence"] = scores
    result = result[result["confidence"] > 0].sort_values(by="confidence", ascending=False)

    if result.empty:
        print(f"No matches found for query: '{query}'")
        return result

    top_score = result["confidence"].max()
    top_matches = result[result["confidence"] == top_score]

    if len(top_matches) > 1:
        print(f"Query '{query}' produced a tie between {len(top_matches)} entries with confidence {top_score}:")
        print(top_matches)
    else:
        print(f"Query '{query}' best match:")
        print(top_matches)

    return result


score_query("fee", df)

print()

score_query("password", df)
