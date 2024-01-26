import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np


#-------------------------------------------Section1 (Articles by name)--------------------------------
def check(s,mv):
    cv=CountVectorizer(max_features=500,stop_words='english')
    vector = cv.fit_transform(mv['tags']).toarray().astype(float)   
    mv['tags'] = mv['tags'].apply(lambda x: " ".join(map(str, x)))
    user_input=s.lower().strip()
    user_vector = cv.transform([user_input]).toarray()
    cosine_similarities = cosine_similarity(user_vector, vector)
    top_indices = cosine_similarities.argsort()[0][-3:][::-1]
    for index in top_indices:
        num=mv['article'][index]
        title = mv['title'][index]
        description = mv['description'][index]
        styled_text = f'''
            <div style='border: 2px solid blue; padding: 10px;'>
                <span style='color:red;font-weight: bold;'>Article: {num}</span><br>
                <span style='color:green;font-weight: bold;'>Title: {title}</span><br>
                {description}
            '''
        st.markdown(styled_text, unsafe_allow_html=True)
def show_articles():
    title = st.text_input('Search Article', '0')
    title=title.upper().strip()
    mv=pd.read_csv('main.csv')
    for article, description,ttl in zip(mv['article'], mv['description'],mv['title']):
        if article == title:
            styled_text = f'''
            <div style='border: 2px solid blue; padding: 10px;'>
                <span style='color:red;font-weight: bold;'>Article: {article}</span><br>
                <span style='color:green;font-weight: bold;'>Title: {ttl}</span><br>
                {description}
            '''
            st.markdown(styled_text, unsafe_allow_html=True)
            break
    else:
        check(title,mv)




#-------------------------------------------Section2 (Articles by Parts)--------------------------------
def caller(s,e,mv):
    for index in range(s,e+1):
        num=mv['article'][index]
        title = mv['title'][index]
        description = mv['description'][index]
        styled_text = f'''
            <div style='border: 2px solid blue; padding: 10px;'>
                <span style='color:red;font-weight: bold;'>Article: {num}</span><br>
                <span style='color:green;font-weight: bold;'>Title: {title}</span><br>
                {description}
            '''
        st.markdown(styled_text, unsafe_allow_html=True)
def showpartaticle(part):
    part_indices = {'Preamble':(0,0),'Part I': (1,4),'Part II': (5,11),'Part III': (12,41),'Part IV': (42,60),'Part IV A': (61,61),'Part V': (62,163),'Part VI': (164,250),'Part VII': (251,251),'Part VIII': (252,258),'Part IX': (259,274),'Part IX A': (275,292),'Part IX B': (293,305),'Part X': (306,307),'Part XI': (308,327),'Part XII': (328,365),'Part XIII': (366,371),'Part XIV': (372,386),'Part XIV A': (387,388),'Part XV': (389,394),'Part XVI': (395,408),'Part XVII': (409,419),'Part XVIII': (420,428),'Part XIX': (429,437),'Part XX': (438,438),'Part XXI': (439,460),'Part XXII': (461,464),}
    mv = pd.read_csv('main.csv')
    if part in part_indices:
        start_index, end_index = part_indices[part]
        caller(start_index, end_index,mv)
    else:
        st.write(f"Part '{part}' not found.")
        caller(0,0,mv)
def show_sections():
    df = pd.read_csv("structure.csv", encoding='latin1')
    st.write("The constitution's articles are grouped into the following parts:")
    st.write(df) 
    options = ["Preamble","Part I", "Part II", "Part III", "Part IV", "Part IV A",
    "Part V", "Part VI", "Part VII", "Part VIII", "Part IX",
    "Part IX A", "Part IX B", "Part X", "Part XI", "Part XII",
    "Part XIII", "Part XIV", "Part XIV A", "Part XV", "Part XVI",
    "Part XVII", "Part XVIII", "Part XIX", "Part XX", "Part XXI",
    "Part XXII"]
    selected_option = st.selectbox("Explore Parts of Sections", options)
    showpartaticle(selected_option)





#-------------------------------------------Section3 (Amendments)--------------------------------
def show_amendments():
    st.write("List of Amendments:")
    df = pd.read_csv("amend.csv", encoding='latin1')
    st.write(df) 
def show_constitution():
    st.markdown(f'''<span style='color:blue;font-weight: bold;'><u>India</u>, also known as Bharat, is a Union of States. It is a Sovereign Socialist Secular Democratic Republic with a parliamentary system of government.</span>''', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown(f'''<span style='color:blue;font-weight: bold;'>The <u>Constitution of India</u> is the longest written national constitution globally, serving as the supreme law. It delineates the fundamental political framework, procedures, powers, and duties of government institutions, including fundamental rights and citizen responsibilities.</span>''', unsafe_allow_html=True)
        
    with col2:
        st.image("bgg.jpg", caption="Bhaarat ka Sanvidhaan", use_column_width=True)
    st.markdown(f'''<span style='color:blue;font-weight: bold;'>India Adopted by the Constituent Assembly on November 26, 1949, and effective from January 26, 1950, it replaced the Government of India Act 1935, marking India's transition to a democratic republic. The constitution, emphasizing constitutional supremacy, declares India as a sovereign, socialist, secular, and democratic republic, guaranteeing justice, equality, liberty, and fraternity to its citizens. The original 1950 constitution is preserved in New Delhi's Parliament House.</span>''', unsafe_allow_html=True)
    st.markdown(f'''<span style='color:whitesmoke;font-size: 20px;font-weight: bold;'>Timeline</span><br>''', unsafe_allow_html=True)
    timeline_data = [
        ("December 6, 1946", "Formation of the Constituent Assembly following French practice."),
        ("December 9, 1946", "First meeting held in the constitution hall, with J. B. Kripalani as the first speaker and Sachchidananda Sinha as the temporary president. The Muslim League boycotted the meeting."),
        ("December 11, 1946", "Rajendra Prasad appointed as the president, H. C. Mukherjee as the vice-president, and B. N. Rau as the constitutional legal adviser. The Assembly initially had 389 members, which later reduced to 299 after partition."),
        ("December 13, 1946", "Jawaharlal Nehru presented the 'Objective Resolution,' outlining the constitution's underlying principles, later becoming the Preamble."),
        ("January 22, 1947", "Objective resolution unanimously adopted."),
        ("July 22, 1947", "National flag adopted."),
        ("August 15, 1947", "India achieved independence, splitting into the Dominion of India and the Dominion of Pakistan."),
        ("August 29, 1947", "Drafting Committee appointed, with B. R. Ambedkar as its chairman."),
        ("July 16, 1948", "V. T. Krishnamachari elected as the second vice-president of the Constituent Assembly."),
        ("November 26, 1949", "The Constitution of India passed and adopted by the assembly."),
        ("January 24, 1950", "Last meeting of the Constituent Assembly. The Constitution, with 395 Articles, 8 Schedules, and 22 Parts, was signed and accepted."),
        ("January 26, 1950", "The Constitution came into force after a process that took 2 years, 11 months, and 18 days, with a total expenditure of ₹6.4 million.")]
    for date, about in timeline_data:
        st.markdown(f'''<span style='color:blue;font-weight: bold;'><u>{date}</u> :  {about} </span>''', unsafe_allow_html=True)
    st.image("rep.jpg", caption="Happy republic Day", use_column_width=True)

def check1(s,mv):
    cv=CountVectorizer(max_features=500,stop_words='english')
    vector = cv.fit_transform(mv['tags']).toarray().astype(float)   
    mv['tags'] = mv['tags'].apply(lambda x: " ".join(map(str, x)))
    user_input=s.lower().strip()
    user_vector = cv.transform([user_input]).toarray()
    cosine_similarities = cosine_similarity(user_vector, vector)
    top_indices = cosine_similarities.argsort()[0][-3:][::-1]
    for index in top_indices:
        que=mv['prompt'][index]
        ans = mv['output'][index]
        styled_text = f'''
            <div style='border: 2px solid blue; padding: 10px;'>
                <span style='color:red;font-weight: bold;'>Question: {que}</span><br>
                <span style='color:green;font-weight: bold;'>Answer: {ans}</span><br>
            '''
        st.markdown(styled_text, unsafe_allow_html=True)





#-------------------------------------------Section5 (QNA)--------------------------------
def show_qna():
    title = st.text_input('Search Your Query','Dev')
    title=title.lower().strip()
    if title=='dev' or title=='adi':
        styled_text = f'''
            <div style='border: 2px solid blue; padding: 10px;'>
                <span style='color:green;font-weight: bold;'>Happy Republic Day</span><br>
            '''
        st.markdown(styled_text, unsafe_allow_html=True)
    else:
        mv=pd.read_csv('que.csv')
        check1(title,mv)





#-------------------------------------------Section6 (Stats)--------------------------------
def show_stats():
    st.write('\n\n\n')
    col1, col2 = st.columns([2, 2])
    with col1:
        labels = ['Men', 'Women']
        sizes = [717100970, 662903415] 
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100),
               startangle=90, wedgeprops=dict(width=0.7))
        ax.axis('equal')
        ax.set_title('Population as per 2023')
        fig.patch.set_facecolor('#45ed53')
        st.pyplot(fig)
    with col2:
        labels = ['Birth Ratio', 'Death Ratio']
        sizes = [16.1, 6.6] 
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100),
               startangle=90, wedgeprops=dict(width=0.7))
        ax.axis('equal')
        ax.set_title('Birth & Death Ratio per 1000 population')
        fig.patch.set_facecolor('#45ed53')
        st.pyplot(fig)
    st.write('\n\n\n')
    
    
    col1, col2, col3 = st.columns([2, 2, 0.5])
    with col1:
        labels = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
        sizes = [3732, 3385, 3150, 2672, 2835, 2702, 2651, 2294, 2103, 2039, 1856, 1827, 1823, 1708]
        fig, ax = plt.subplots()
        ax.plot(labels, sizes, marker='o', linestyle='-', color='blue')
        ax.set_title('India GDP')
        ax.set_xlabel('Year')
        ax.set_ylabel('GDP in Billion $')
        for i, txt in enumerate(sizes):
            ax.annotate(f'{txt}', (labels[i], sizes[i]), textcoords="offset points", xytext=(0, 5), ha='center')
        fig.set_facecolor('#45ed53')
        ax.set_facecolor('whitesmoke')
        st.pyplot(fig)
    with col2:
        labels_bar = ['Men', 'Women']
        sizes_bar = [65.76, 68.89]
        fig_bar, ax_bar = plt.subplots()
        bars = ax_bar.bar(labels_bar, sizes_bar, width=0.6)
        ax_bar.set_title('Life Expectancy')
        ax_bar.set_ylabel('Values')
        for bar in bars:
            yval = bar.get_height()
            ax_bar.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
        fig_bar.set_facecolor('#45ed53')
        st.pyplot(fig_bar)
    with col3:
        st.write("Source: Bahut alg alg site, Kya karoge janke.")

    st.write('\n\n\n')
    st.write('\n\n\n')
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Most Clean City in India<br><span style='color:#e8357d'>Indore</span></div>''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Most Polluted City in India<br><span style='color:#e8357d'>Delhi</span></div>''', unsafe_allow_html=True)
    with col3:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Highest Population State<br><span style='color:#e8357d'>Uttar Pradesh</span></div>''', unsafe_allow_html=True)
    
    st.write('\n\n\n')
    st.write('\n\n\n')
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Highest Literacy Rate<br><span style='color:#e8357d'>Kerala (94%)</span></div>''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Lowest Literacy Rate<br><span style='color:#e8357d'>Bihar(64%)</span></div>''', unsafe_allow_html=True)
    with col3:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Density Per Square KM<br><span style='color:#e8357d'>411.11</span></div>''', unsafe_allow_html=True)
    
    st.write('\n\n\n')
    st.write('\n\n\n')
    col1, col2 = st.columns([2, 2])
    with col1:
        labels = ['Hindi','Marathi', 'Kannada',  'Tamil','Telgu','Bengali','Gujarati','Other']
        sizes = [5283,830,437,690,811,972,554,1716] 
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100),
               startangle=90, wedgeprops=dict(width=0.7))
        ax.axis('equal')
        ax.set_title('Languages Spoken In India In Lakh')
        fig.patch.set_facecolor('#45ed53')
        st.pyplot(fig)
    with col2:
        labels = ['0 to 14 years', '15 to 64 Years' , 'Above 65 Years']
        sizes = [349990,919990,93026] 
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100),
               startangle=90, wedgeprops=dict(width=0.7))
        ax.axis('equal')
        ax.set_title('Age Distribution (In K)')
        fig.patch.set_facecolor('#45ed53')
        st.pyplot(fig)
    st.write('\n\n\n')
    st.write('\n\n\n')

    st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:20px;text-align: center;'>Unverified Facts :)<br></div>''', unsafe_allow_html=True)
    st.write('\n\n\n')
    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Developed BY<br><span style='color:#e8357d'>AdityaSingh</span></div>''', unsafe_allow_html=True)
        st.write('\n\n\n')
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Best Moderator<br><span style='color:#e8357d'>Kaizar & Piyush<br> Macbook & Deepanshu</span><br>
                    <span style='color:white;font-weight: bold;font-size:9px;'>(Ban Ho jaye lekin Chaploosi Na Jaye)</span></div>''', unsafe_allow_html=True)
        st.write('\n\n\n')
        st.markdown(f'''<div style='color:blue;font-weight: bold;font-size:15px; border: 2px solid blue;border-radius: 7px; 
                    padding: 5px; text-align: center;'>Just for Fun<br><span style='color:#e8357d'>Don't Ban</span>
                    <span></span></div>''', unsafe_allow_html=True)
    with col2:
        labels = ['Bhartiya']
        sizes = [1436090238] 
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100),
               startangle=90, wedgeprops=dict(width=0.7),colors=['orange'])
        ax.axis('equal')
        ax.set_title('Religion Distribution')
        fig.patch.set_facecolor('#45ed53')
        st.pyplot(fig)
    st.write('\n\n\n')
    st.write('\n\n\n')
    st.image("rep.jpg", caption="Happy republic Day", use_column_width=True)


    
#-------------------------------------------Main Section--------------------------------
def main():
    st.markdown(
        f"""
        <style>
            body {{
                background-color: #45ed53;
                color: blue;
            }}
            .ezrtsby2{{
                background-color: orange;
            }}
            .eczjsme3 {{
                background-color: lightblue;
            }}
            .stApp {{
                background: none;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    navigation_options = ["Indian Constitution","Articles By Name", "Articles By Parts","Amendments","QnA","Statistics"]
    selected_option = st.sidebar.selectbox("Select Section", navigation_options)

    if selected_option == "Articles By Name":
        show_articles()
    elif selected_option == "Amendments":
        show_amendments()
    elif selected_option == "Articles By Parts":
        show_sections()
    elif selected_option == "Indian Constitution":
        show_constitution()
    elif selected_option == "QnA":
        show_qna()
    elif selected_option == "Statistics":
        show_stats()

if __name__ == "__main__":
    st.title("Learning about Constitution")
    main()
