import streamlit as st
import ollama
import base64

st.set_page_config(page_title="CareGuide")

def get_base64(background):
    with open(background,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str=get_base64("background.png")


st.markdown("""
    <style>
        .navbar {
            background-color: #004080;
            overflow: hidden;
            display: flex;
            justify-content: center;
            padding: 10px 0;
        }

        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
            font-family: Arial, sans-serif;
        }

        .navbar a:hover {
            background-color: #0066cc;
            border-radius: 5px;
        }

        .header-space {
            margin-bottom: 20px;
        }
    </style>

    <div class="navbar">
        <a href="#">Home</a>
        <a href="#">Services</a>
        <a href="#">About Us</a>
        <a href="#">Contact Us</a>
        <a href="#">Find Doctor</a>
    </div>
    <div class="header-space"></div>
""", unsafe_allow_html=True)


st.markdown(f"""
        <style>
            .main{{
            background-image:url("data:image/png;base64,{bin_str}");
            background-style:cover;
            background-position:center;
            background-repeat:no-repeat;

            }}
        </style>
        """,unsafe_allow_html=True)

st.session_state.setdefault('conversation_history',[])

def generate_response(user_input):
    st.session_state['conversation_history'].append({"role":"user", "content":user_input})

    response = ollama.chat(model="gemma2:2b", messages=st.session_state['conversation_history'])
    ai_response= response['message']['content']

    st.session_state['conversation_history'].append({"role":"assistant", "content":ai_response})
    return ai_response

def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed"
    response = ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    response=ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_diet_plans():
    prompt = "You are a heathcare ai agent, Provide a 4 to 5 diet plan for healthy life."
    response=ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_symptoms():
    prompt = "You are a heathcare ai agent that Provide fever symptoms and steps to cure it"
    response = ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_exercise_guide():
    prompt = "Provide 5 effective exercises for reducing stress that can be done at home"
    response=ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_plantbased_diet():
    prompt = "Provide a 4 to 5 plant based diet plan for healthy life."
    response=ollama.chat(model="gemma2:2b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']


st.title("CareGuide Chatbot")

for msg in st.session_state['conversation_history']:
    role= "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

user_message = st.text_input("Welcome! I'm here to help with any health and well being related questions or concerns.")

if user_message:
    with st.spinner("Generating"):
        ai_response = generate_response(user_message)
        st.markdown(f"**AI:** {ai_response}")

col1 , col2 , col3 = st.columns(3)
col4 , col5 , col6 = st.columns(3)

with col1:
    if st.button("Provide Positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"**Affirmation:** {affirmation}")

with col2:
    if st.button("Provide Guided meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"**Guided Meditation:** {meditation_guide}")       

with col3:
    if st.button("Provide a Healthy diet plan"):
        diet_plans = generate_diet_plans()
        st.markdown(f"**Diet Plans:** {diet_plans}")    

with col4:
    if st.button("Provide Fever symptoms"):
        symptoms = generate_symptoms()
        st.markdown(f"**Symptoms:** {symptoms}")

with col5:
    if st.button("Provide Exercise plans"):
        exercise_guide = generate_exercise_guide()
        st.markdown(f"**Guided Exercises:** {exercise_guide}")       

with col6:
    if st.button("Provide plant based Healthy diet plan"):
        plantbased_diet= generate_plantbased_diet()
        st.markdown(f"**Diet Plans:** {plantbased_diet}") 