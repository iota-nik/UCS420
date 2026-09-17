"""
Q5) Using groupby, print how many FAQ entries you have per category.
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

category_counts = df.groupby("category").size()
print(category_counts)
