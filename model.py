import pandas as pd 


df = pd.read_csv("data\movies_metadata.csv" , low_memory=False)

# print(df.head())

df = df.drop_duplicates().reset_index(drop=True)

df = df[['title','overview','genres' , 'tagline','vote_average' , 'popularity']]

df = df.dropna(subset = ['title' , 'vote_average', 'popularity'])

df['overview'] = df['overview'].fillna(" ")

df['tagline'] = df['tagline'].fillna(" ")

# print(df.isnull().sum())

import ast
df['genres'] = df['genres'].apply(
    lambda x: " ".join(d['name'] for d in ast.literal_eval(x)))

df['Tags'] = df['overview'] + " "+df['genres'] + " "+ df['tagline']

# print(df['Tags'][0])

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import string
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
def NLP(text):
    text = str(text).lower()

    text = re.sub(r'http\S+', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = ' '.join([word for word in text.split() if word not in stop_words])

    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

    return text

df['Tags'] = df['Tags'].apply(NLP)

# print(df['Tags'][10])

df = df.reset_index(drop= True)

indices = pd.Series(df.index , index = df['title'])


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=50000,ngram_range=(1,2),stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Tags'])


# Now we have to use COsin similarity to predict our recommendation


from sklearn.metrics.pairwise import cosine_similarity

def recommend(title , n = 10):
    idx = indices[title]
    similar_scores = cosine_similarity(tfidf_matrix[idx] , tfidf_matrix).flatten()
    similar_movies = similar_scores.argsort()[::-1][1:n+1]
    return df['title'].iloc[similar_movies]

print(recommend('The Dark Knight Rises'))


import pickle

pickle.dump(tfidf_matrix , open('tfidf_matrix.pkl' , 'wb'))
pickle.dump(indices , open('indices.pkl' , 'wb'))
df.to_pickle('df.pkl')
pickle.dump(tfidf , open('tfidf.pkl' , 'wb'))




"191dcd0ee1772b533673233a4ee367d1"