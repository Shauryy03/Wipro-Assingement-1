
import re
import requests

# 1. Check if strings have only octal digits
def check_octal(strings):
    print("Octal check:")
    for s in strings:
        if re.fullmatch(r'[0-7]+', s):
            print(f"'{s}' is octal")
        else:
            print(f"'{s}' is NOT octal")

# 2. Extract user ID, domain name, and suffix from emails
def extract_email_parts(emails):
    print("\nExtracted email parts:")
    matches = re.findall(r'(\w+)@(\w+)\.(\w+)', emails)
    for user, domain, suffix in matches:
        print(f"User: {user}, Domain: {domain}, Suffix: {suffix}")

# 3. Split irregular sentence into proper words
def clean_sentence(sentence):
    words = re.split(r'[;,_\s]+', sentence)
    cleaned = ' '.join(words)
    print(f"\nCleaned sentence: {cleaned}")

# 4. Clean tweet to remove URLs, hashtags, mentions, punctuation, RTs, and CCs
def clean_tweet(tweet):
    cleaned = re.sub(r"(RT|cc|@\w+|#\w+|http\S+|\W+)", " ", tweet)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    print(f"\nCleaned Tweet: {cleaned}")

# 5. Extract text portions from HTML page using regex
def extract_html_text():
    r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
    text = re.findall(r'>([^<>]+)<', r.text)
    clean_text = [t.strip() for t in text if t.strip()]
    print(f"\nExtracted HTML Text: {clean_text}")

# 6. Identify words that begin and end with the same character
def same_start_end(words):
    print("\nWords that begin and end with same character:")
    for word in words:
        w = word.strip()
        if len(w) >= 2 and w[0].lower() == w[-1].lower():
            print(w)

# Call functions
check_octal(['789','123','004'])
extract_email_parts("""zuck@facebook.com\nsunder33@google.com\njeff42@amazon.com""")
clean_sentence("A, very   very; irregular_sentence")
clean_tweet("""Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats""")
extract_html_text()
same_start_end(["civic", "trust", "widows", "maximum", "museums", "aa", "as"])
