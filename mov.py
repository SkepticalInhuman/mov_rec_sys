import streamlit as st
import pickle 
import pandas as pd

movies_list = pickle.load(open('movie_dict.pkl','rb'))
cos = pickle.load(open('cos.pkl','rb'))
cos2 = pickle.load(open('cos2.pkl','rb'))
movies = pd.DataFrame(movies_list)

def get_rec(title, cosine_sim=cos):
  i = movies[movies['title_x']==title].index[0]
  sim_scores = list(enumerate(cosine_sim[i]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:6]
  mov_ind = [i[0] for i in sim_scores]
  return movies['title_x'].iloc[mov_ind]

st.title("Movie Recommender System")
selected_movie = st.selectbox(
    "How would you like to be contacted?",
    (movies['title_x'].values)
)
if st.button("Recommendations"):
    recommendations = get_rec(selected_movie, cos2)
    for i in recommendations:
        st.write(i)