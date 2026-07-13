import re

class TextCleaner:
    
    @staticmethod
    def clean_text(text):
        # Implement your text cleaning logic here
        text = text.strip()  # Example: remove leading/trailing whitespace
        text = re.sub(r'-\n', '', text)
        text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single newline
        text = re.sub(r' +', ' ', text)  # Replace multiple spaces with a single space
        return text