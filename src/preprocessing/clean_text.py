import re

def clean_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    
    # 3. Remove mentions (@user)
    text = re.sub(r"@\w+", "", text)
    
    # 4. Remove special characters (keep letters and spaces)
    text = re.sub(r"[^a-z\s]", "", text)
    
    # 5. Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text