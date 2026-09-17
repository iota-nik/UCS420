"""
Q1) Build Your Personalized Knowledge Base: Take your college roll number. Extract its
digits. Build a pandas DataFrame with exactly 6 FAQ entries: 4 fixed entries and other 2
entries constructed from your own roll number digits as follows:
    - Take the LAST TWO DIGITS of your roll number. For each digit d, compute
      category = ["billing", "account", "general"][d % 3].
    Roll number: 1024170030 -> last two digits: 3, 0
    digit 3 -> category[3 % 3] = billing
    digit 0 -> category[0 % 3] = billing
Output: Print your final 6-row DataFrame.
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
print(df)
