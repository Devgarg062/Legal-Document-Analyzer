import spacy
import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    filtered_words = [word for word in words if word not in stop_words]
    common_words = Counter(filtered_words).most_common(10)
    return ", ".join([word[0] for word in common_words])

def extract_entities(text):
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return str(entities)
