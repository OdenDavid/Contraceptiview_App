Contraceptiview: AI-Powered Contraceptive Review Analysis
===========================================================

Overview
-----------
Contraceptiview is an innovative web application leveraging Natural Language Processing (NLP) and Machine Learning (ML) to analyze contraceptive reviews and side effects. Empowering women to make informed reproductive health decisions.

![Contraceptiview](https://github.com/OdenDavid/Contraceptiview_App/blob/main/Home.png)

Project Structure
-------------------
```
Contraceptiview_App
├── images
├── weights
├── App.py
├── NLTK_download.py
├── preprocess.py
├── Reviews.db
├── Sentiment.py
├── SideEffect.py
├── Topic.py
├── Project.ipynb
└── requirements.txt
```

Components
------------
1. App.py: Streamlit web application entry point
2. NLTK_download.py: Downloads required NLTK resources (stopwords, wordnet, etc.)
3. preprocess.py: Cleans and preprocesses contraceptive reviews
4. Reviews.db: Database storing contraceptive reviews
5. Sentiment.py: Performs sentiment analysis using SKLLM model
6. SideEffect.py: Identifies side effects using rule-based algorithm
7. Topic.py: Performs topic modeling using BERTopic
8. Project.ipynb: Notebook containing data exploration, model development, and testing
9. requirements.txt: Lists dependencies required to run the application

Technologies Used
--------------------
* Python
* Natural Language Processing (NLTK, spaCy)
* Machine Learning (LLM, Scikit-learn, Light GBM, BERTopic, Latent Dirichlet Allocation (LDA))
* Streamlit
* SQLite (Reviews database)

Getting Started
---------------
* Clone the repository: git clone https://github.com/your-username/Contraceptiview_App.gi
* Install dependencies: pip install -r requirements.txt
* Download NLTK resources: python NLTK_download.py
* Run the application: streamlit run App.py

Features
------------
1. Sentiment Identifier
  * Select a contraceptive method
  * View reviews grouped by sentiment (Positive, Negative, Neutral)
  * Submit your own review for classification
2. Topics
  * Explore reviews categorized into topics (Acne, Implants, Adverse Effects, Weight)
  * Classify new reviews into topics
3. Side Effect Identifier
  * Enter your age
  * View most common side effects and top 5 useful reviews from your age group

Contributing
------------
Contributions are welcome! Please open an issue or submit a pull request.

License
-------
[Insert License]

Author
--------
[David Oden]
