import re
import nltk
wn = nltk.WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')


def review_clean(review: str):
    # changing to lower case
    lower = review.lower()
    
    # Replacing the repeating pattern of '&#039;' which is meant to be an apostrophe
    pattern_remove = lower.replace("&#039;", "'")
    
    # Removing all the special Characters
    special_remove = pattern_remove.replace(r'[^\w\d\s]',' ')
    
    # Removing all the non ASCII characters
    ascii_remove = special_remove.replace(r'[^\x00-\x7F]+',' ')
    
    # Removing the leading and trailing Whitespaces
    whitespace_remove = ascii_remove.replace(r'^\s+|\s+?$','')
    
    # Replacing multiple Spaces with Single Space
    multiw_remove = whitespace_remove.replace(r'\s+',' ')
    
    # Replacing Two or more dots with one
    replace_dots = multiw_remove.replace(r'\.{2,}', ' ')

    # removing double quotesfrom string
    cleaned = replace_dots.strip('\"')
    
    return cleaned

def review_clean_lematize(review: str):

    year_pattern = r"\b(200[5-9]|201[0-9])\b" # Define a regex pattern to match numeric years from 2005 to 2020
    year_regex = re.compile(year_pattern)

    review_cleaned = review_clean(review)
    # Remove years
    review_no_year = year_regex.sub("", review_cleaned)

    # Remove stopwords
    review_no_stopwords = ' '.join([w for w in review_no_year.split() if w.lower() not in stopwords])

    # Lemmatization
    review = ' '.join([wn.lemmatize(w) for w in review_no_stopwords.split() if w not in stopwords])

    return review