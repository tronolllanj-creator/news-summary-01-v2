#!/usr/bin/env python3
"""Write this November news summary entry to the output directory."""

import os

SUMMARY = """Russia and Ukraine held a second day of US-mediated peace talks in Abu Dhabi on Wednesday, their first direct talks in nine months, but ended without a breakthrough. President Donald Trump's envoys Jared Kushner and Steve Witkoff said they will travel to Moscow on Thursday to meet Vladimir Putin, then to Dublin to brief Volodymyr Zelensky. The talks were overshadowed by Russian strikes that killed at least nine people in Ukraine hours earlier, and by an earlier bombing of an aid centre in Zaporizhzhia that killed at least 31.

In Washington, the midterm fallout continued: Democrats have taken the House with 254 seats and at least 54 in the Senate, while Trump conceded in a 60 Minutes interview that strict deportation policy cost Republicans support. The House voted 211-204 to shelve an impeachment effort against Defense Secretary Pete Hegseth, and Republicans elected Jim Jordan as their minority leader.

Tensions in the Strait of Hormuz deepened after three oil tankers caught fire striking naval mines; monitoring firms counted at least 37 attacks on shipping there in November, the most since the Iran war began nine months ago. Tehran says the strait stays closed until Washington answers its seven conditions for talks, and US prosecutors charged three alleged Iranian operatives over plots against Jewish communities and RAF Fairford, a British air base. Brent crude rose to about $92.50 a barrel.

Nvidia chief executive Jensen Huang is under federal investigation over alleged contacts with Chinese intelligence, a senator said he must resign, and the chipmaker has lost about $430 billion in market value over two days. Hotter-than-expected US inflation, with consumer prices up 0.4% in October, has made a December Federal Reserve rate rise look all but certain, pushing the 10-year Treasury yield close to 5%, though Asian shares rallied as strong CoreWeave results eased fears of an AI bubble.
"""

def validate_summary(text):
    """Enforce the entry gate's length and meaningful-content requirements."""
    if not 1 <= len(text) <= 2000:
        raise ValueError("summary length must be between 1 and 2000 characters")
    if not text.strip():
        raise ValueError("summary must contain non-whitespace text")

def main():
    validate_summary(SUMMARY)
    os.makedirs("/output", exist_ok=True)
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(SUMMARY)

if __name__ == "__main__":
    main()
