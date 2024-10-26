import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import random

import sqlite3
conn = sqlite3.connect("Reviews.db") # db - database
cursor = conn.cursor() # Cursor object

# Import nltk files
import NLTK_download
NLTK_download.download()

from Sentiment import get_sentiment # Sentiment
from Topic import get_topic # Topic
from SideEffect import describe_age # Side Effect

image = Image.open('images/logo-no-background 1.png')
st.image(image)

selected = option_menu(
    menu_title = None,
    options = ["Home", "Sentiment Identifier", "Topics", "Side Effect Identifier"],
    icons = ["house-fill", "sign-intersection", "journal-medical", "x-square"],
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    col1, col2 = st.columns(2)

    with col1:
        st.title(':green[Find A Contraceptive Pill That Suits You]')
        st.caption(unsafe_allow_html=True,
                body="<b>1. There is no one way to have safe sex.\n\n2. To prevent unplanned pregnancies take a look at various contraceptive options.\n3. Use our review feature to see which method fit your needs.\n4. Compare it to other options and decide what works for you.</b>")

    with col2:
        image = Image.open('images/Frame 52358.png')
        st.image(image)

elif selected == "Sentiment Identifier":
    
    st.header(':green[Sentiment Identifier]')
    st.caption(unsafe_allow_html=True, body="<b>Use this feature to compare :green[reviews by sentiment] across different contraceptives.\nWith this you would see :green[experiences] by other contraceptive users.\n\nThis should help you decide what works best for you.</b>")
    
    drugs = ["<Choose One>","Etonogestrel","Skyla","Ethinyl estradiol / norethindrone","Ethinyl estradiol / levonorgestrel","Implanon","Levonorgestrel","Ethinyl estradiol / norgestimate","Lo Loestrin Fe","Nexplanon","Mirena"]
    option = st.selectbox(label='Start by choosing a contraceptive?',placeholder='Choose',options=drugs)
    
    contraceptive_dict = {
    "Etonogestrel": "Etonogestrel is a synthetic progestin hormone used as a long-acting reversible contraceptive implant.",
    "Skyla": "Skyla is a hormonal intrauterine device (IUD) that releases progestin to prevent pregnancy.",
    "Ethinyl estradiol / norethindrone": "Ethinyl estradiol/norethindrone is a combination contraceptive pill that contains both estrogen and progestin hormones.",
    "Ethinyl estradiol / levonorgestrel": "Ethinyl estradiol/levonorgestrel is a combination contraceptive pill that contains both estrogen and progestin hormones.",
    "Implanon": "Implanon is a progestin-only contraceptive implant that is inserted under the skin to prevent pregnancy.",
    "Levonorgestrel": "Levonorgestrel is a progestin hormone commonly used in birth control pills and emergency contraception.",
    "Ethinyl estradiol / norgestimate": "Ethinyl estradiol/norgestimate is a combination contraceptive pill that contains both estrogen and progestin hormones.",
    "Lo Loestrin Fe": "Lo Loestrin Fe is a low-dose combination contraceptive pill that provides a lower amount of hormones.",
    "Nexplanon": "Nexplanon is a contraceptive implant that releases progestin to prevent pregnancy and is effective for several years.",
    "Mirena": "Mirena is a hormonal intrauterine device (IUD) that releases progestin to prevent pregnancy and is effective for several years."
    }

    # SQL
    def get_reviews(sentiment: str,order: str,drug: str):
        
        if order == "recent": # The most recent
            response = cursor.execute("""SELECT review_clean, day, month, Year FROM Table_reviews
                                            WHERE Review_Sentiment='{}' and drugName='{}'
                                            ORDER BY CAST(year AS DATETIME) DESC, CAST(month AS DATETIME) DESC, CAST(day AS DATETIME) DESC
                                            LIMIT 3;""".format(sentiment, drug))
        return response.fetchall()
    
    def sentiment_widgets(choice):
        st.subheader(':green['+choice+'] Contraceptive Reviews By Users')
        about_col1, about_col2 = st.columns(2)
        with about_col1:
            st.caption(contraceptive_dict[choice])
        with about_col2:
            image = Image.open('images/{}.jpg'.format(choice.replace("/",":")))
            st.image(image)
        
        pos_reviews = get_reviews(sentiment="Positive", order="recent", drug=choice)
        neu_reviews = get_reviews(sentiment="Neutral", order="recent", drug=choice)
        neg_reviews = get_reviews(sentiment="Negative", order="recent", drug=choice)

        tab1, tab2, tab3 = st.tabs(["😃:green[Positive]", "😐Neutral", "😫:red[Negative]"])

        with tab1:
                st.caption(unsafe_allow_html=True, body=pos_reviews[0][0]+'\n\n<b>'+str(pos_reviews[0][1])+','+str(pos_reviews[0][2])+','+str(pos_reviews[0][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=pos_reviews[1][0]+'\n\n<b>'+str(pos_reviews[1][1])+','+str(pos_reviews[1][2])+','+str(pos_reviews[1][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=pos_reviews[2][0]+'\n\n<b>'+str(pos_reviews[2][1])+','+str(pos_reviews[2][2])+','+str(pos_reviews[2][3])+'</b>')
        with tab2:
                st.caption(unsafe_allow_html=True, body=neu_reviews[0][0]+'\n\n<b>'+str(neu_reviews[0][1])+','+str(neu_reviews[0][2])+','+str(neu_reviews[0][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=neu_reviews[1][0]+'\n\n<b>'+str(neu_reviews[1][1])+','+str(neu_reviews[1][2])+','+str(neu_reviews[1][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=neu_reviews[2][0]+'\n\n<b>'+str(neu_reviews[2][1])+','+str(neu_reviews[2][2])+','+str(neu_reviews[2][3])+'</b>')
        with tab3:
                st.caption(unsafe_allow_html=True, body=neg_reviews[0][0]+'\n\n<b>'+str(neg_reviews[0][1])+','+str(neg_reviews[0][2])+','+str(neg_reviews[0][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=neg_reviews[1][0]+'\n\n<b>'+str(neg_reviews[1][1])+','+str(neg_reviews[1][2])+','+str(neg_reviews[1][3])+'</b>')
                st.caption(unsafe_allow_html=True, body=neg_reviews[2][0]+'\n\n<b>'+str(neg_reviews[2][1])+','+str(neg_reviews[2][2])+','+str(neg_reviews[2][3])+'</b>')

        collect_review = st.text_area(label='Share your experience with {}'.format(choice))
        if st.button("Send"):
            if collect_review == '':
                st.toast('You cant submit an empty review', icon='❌')
            elif collect_review.isdigit():
                 st.toast('You cant submit a number as a review', icon='❌')
            elif len(collect_review.split()) < 10:
                 st.toast('Insufficient words', icon='❌')
            else:
                try:
                    response1 = get_sentiment(collect_review, choice)
                    response2 = get_topic(collect_review)

                    # Insert into sentiment reviews table
                    cursor.execute("""INSERT INTO Table_reviews VALUES ({},"{}",{},{},"{}","{}",{},{},{});
                                    """.format(random.randint(1, 50000), response1["drugName"], response1["rating"],response1["usefulCount"],
                                                response1["Review_Sentiment"][0], response1["review_clean"],response1["Year"],response1["month"],response1["day"]))
                    # Insert into topic reviews table
                    # First get the max index as column doesn't autoincrement
                    cursor.execute("""SELECT MAX(`index`) FROM Table_topics""")
                    max_index = cursor.fetchone()[0]
                    next_index = max_index + 1 if max_index is not None else 1
                    cursor.execute("""INSERT INTO Table_topics VALUES ({},"{}",{},{},{},"{}");
                                    """.format(next_index, response2["review_clean"], response2["Year"],response2["month"], response2["day"], response2["topics"]))
                    conn.commit()
                    conn.close()
                    st.toast('Response recorded, Thank you', icon='✅')
                except Exception as e:
                    st.toast('ERROR: '+str(e)+'', icon='❌')

    if option == "Etonogestrel":
        sentiment_widgets("Etonogestrel")
    elif option == "Skyla":
        sentiment_widgets("Skyla")
    elif option == "Ethinyl estradiol / norethindrone":
         sentiment_widgets("Ethinyl estradiol / norethindrone")
    elif option == "Ethinyl estradiol / levonorgestrel":
         sentiment_widgets("Ethinyl estradiol / levonorgestrel")
    elif option == "Implanon":
         sentiment_widgets("Implanon")
    elif option == "Levonorgestrel":
        sentiment_widgets("Levonorgestrel")
    elif option == "Ethinyl estradiol / norgestimate":
         sentiment_widgets("Ethinyl estradiol / norgestimate")
    elif option == "Lo Loestrin Fe":
        sentiment_widgets("Lo Loestrin Fe")
    elif option == "Nexplanon":
         sentiment_widgets("Nexplanon")
    elif option == "Mirena":
         sentiment_widgets("Mirena")

    #col1, col2, col3, col4 = st.columns(4)

elif selected == "Topics":
    st.header(':green[Topics]')
    st.caption(unsafe_allow_html=True, body="<b>Find contraceptive reviews based on the most relevant :green[topics].\nWith our clustering and topic modelling algorithms you can see reviews most similar to each other.\n\nThis should help you view users experiences from topics that concern you.</b>")
    
    def topics(topic: str):
        response = cursor.execute("""SELECT DISTINCT review_clean, day, month, Year FROM Table_topics
                                                WHERE topics='{}'
                                                ORDER BY CAST(Year AS DATETIME) DESC, CAST(month AS DATETIME) DESC, CAST(day AS DATETIME) DESC
                                                LIMIT 10;""".format(topic))
        return response.fetchall()
                                            
    tab1, tab2, tab3, tab4 = st.tabs(["Acne", "Implants", "Adverse effects", "Weight"])

    with tab1:
        Acnes = topics("Acne")
        for i in range(0, len(Acnes)):
            st.caption(unsafe_allow_html=True, body=str(i+1)+'. '+Acnes[i][0]+'. - <i>reviewed on</i> <b>('+str(Acnes[i][1])+','+str(Acnes[i][2])+','+str(Acnes[i][3])+')</b>')
    with tab2:
         Implants = topics("Implants")
         for i in range(0, len(Implants)):
            st.caption(unsafe_allow_html=True, body=str(i+1)+'. '+Implants[i][0]+'. - <i>reviewed on</i> <b>('+str(Implants[i][1])+','+str(Implants[i][2])+','+str(Implants[i][3])+')</b>')
    with tab3:
         Adverse_effects = topics("Adverse effects")
         for i in range(0, len(Adverse_effects)):
            st.caption(unsafe_allow_html=True, body=str(i+1)+'. '+Adverse_effects[i][0]+'. - <i>reviewed on</i> <b>('+str(Adverse_effects[i][1])+','+str(Adverse_effects[i][2])+','+str(Adverse_effects[i][3])+')</b>')
    with tab4:
         Weight = topics("Weight")
         for i in range(0, len(Weight)):
            st.caption(unsafe_allow_html=True, body=str(i+1)+'. '+Weight[i][0]+'. - <i>reviewed on</i> <b>('+str(Weight[i][1])+','+str(Weight[i][2])+','+str(Weight[i][3])+')</b>')

elif selected == "Side Effect Identifier":
    st.header(':green[Side Effect Identifier]')
    st.caption(unsafe_allow_html=True, body="<b>This feature enables reproductive women view :green[contraceptive side effects] experienced by other women within thier age groups.\n\nThis would be useful to women who are new to contraceptive use or looking to change their current contraceptive.</b>")

    number = st.number_input(label='How old are you?',min_value=18,max_value=64,value=18)
    st.write(str(number)+" <b>Years Old</b>", unsafe_allow_html=True)

    if st.button("Identify"):
        response = describe_age(number)

        top_side_effects = ", ".join(f"'{item}'" for item in response["side_effects"])
        st.caption(unsafe_allow_html=True,body="Based on your age group {}, the most complained side effects are <b>{}</b>. \n\nBelow are the top 5 most useful contraceptive reviews from people with your age group: \n".format(response["age_group"], top_side_effects))

        for i in range(0,len(response["sorted_reviews"]["Reviews"])):
            st.caption(unsafe_allow_html=True,body=str(i+1)+'. '+response["sorted_reviews"]["Reviews"][i]+' <b><i>drug used: </i> :green['+response["sorted_reviews"]["Drugs"][i]+']</b>')