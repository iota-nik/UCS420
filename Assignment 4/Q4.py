"""
Q4) Pick any one entry in your knowledge base. Ask the user to input a new keyword, add
it to that entry's keywords, and save your entire updated DataFrame to a CSV file named
<your_roll_number>_faq_data.csv.
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

roll_number = "1024170030"

new_keyword = input("Enter a new keyword to add to the 'what is the annual fee' entry: ")
idx = df[df["question"] == "what is the annual fee"].index[0]
df.at[idx, "keywords"] = df.at[idx, "keywords"] + " " + new_keyword

print(df)

csv_name = f"{roll_number}_faq_data.csv"
df.to_csv(csv_name, index=False)
print(f"Saved updated DataFrame to {csv_name}")
