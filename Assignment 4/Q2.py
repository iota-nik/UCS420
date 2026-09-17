"""
Q2) Generate and Score a Hypothesis - Implement a scoring function that takes a query
string and returns all matching entries ranked by confidence.
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
    return result


print(score_query("what is the fee", df))
