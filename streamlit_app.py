import pandas as pd
import streamlit as st

if 'init' not in st.session_state:
    st.session_state.init = True
    st.session_state.df = pd.read_csv('data.csv')
    st.session_state.group2occupations = st.session_state.df.groupby('Group')['Occupation'].unique().to_dict()

df = st.session_state.df

st.title("Stanford University Scientific Research Project Survey")

st.caption("""
This survey is part of a Stanford University scientific research project. Your decision to complete this survey is voluntary. There is no way for us to identify you. The only information we will have, in addition to your responses, is the time at which you completed the survey. The results of the research may be presented at scientific meetings or published in scientific journals. Clicking on the 'SUBMIT' button at the bottom of this page indicates that you are at least 18 years of age and agree to complete this survey voluntarily.
""")

st.header("General Information")

age = st.text_input("Q1. What is your age?")

gender = st.selectbox("Q2. What is your gender?",
                      ["", "Male", "Female", "Non-binary / third gender", "Prefer not to say"])

race = st.multiselect("Q3. What is your race?",
                      ["", "White or Caucasian", "Asian or Pacific Islander", "Black or African American",
                       "Hispanic or Latino", "Native American or Alaskan Native",
                       "Native Hawaiian and Other Pacific Islander", "A race or ethnicity not listed here"])

education = st.selectbox("Q4. What is your highest level of education?",
                         ["", "Less than high school", "High school diploma or equivalent (e.g. GED)",
                          "Some college, but no degree", "Associate degree (e.g., AA, AS)",
                          "Bachelor’s degree (e.g. BA, BS)", "Master’s degree (e.g. MA, MS, MEng, MSW)",
                          "Doctoral degree (e.g. PhD, EdD)", "Professional degree (e.g. MD, DDS, DVM, JD)",
                          "Other"])
if education == "Professional degree (e.g. MD, DDS, DVM, JD)" or education == "Other":
    education_specify = st.text_input("Q4a. Please specify your highest level of education.")

field_of_study = st.text_input("Q5. What is your field of study?")

employment_status = st.selectbox("Q6. What is your employment status?",
                                 ["", "Full-time", "Part-time", "Contract", "Other", "Prefer not to say"])
if employment_status == "Other":
    employment_status_specify = st.text_input("Q6a. Please specify your employment status.")

professional_title = st.text_input("Q7. What is your professional title?")

specialty_area = st.text_input("Q8. What is your specialty / area of practice?")

healthcare_experience = st.selectbox("Q9. What are your years of experience in healthcare?",
                                     ["", "Less than 1 year", "1-5 years", "6-10 years", "11-15 years", "16-20 years",
                                      "More than 20 years"])

stanford_experience = st.selectbox("Q10. What are your years of experience at Stanford Hospital?",
                                   ["", "Less than 1 year", "1-5 years", "6-10 years", "11-15 years", "16-20 years",
                                    "More than 20 years"])

work_setting = st.multiselect("Q11. What is your work setting?",
                              ["", "Hospital", "Clinic", "Academic research", "Teaching", "Other"])
if "Other" in work_setting:
    work_setting_specify = st.text_input("Q11a. Please specify your work setting.")

st.header("Exposure to Artificial Intelligence Technologies")

exposure_level = st.selectbox(
    "Q1. Please rate your level of exposure to AI technologies in your professional practice.",
    ["", "I am not aware of any AI technologies",
     "I am aware of AI technologies but have not interacted with or used them",
     "I occasionally interact with or use AI technologies",
     "I frequently interact or use AI technologies",
     "I primarily rely on AI technologies in my professional practice"])

if exposure_level in ["I occasionally interact with or use AI technologies",
                      "I frequently interact or use AI technologies",
                      "I primarily rely on AI technologies in my professional practice"]:
    ai_types = st.multiselect(
        "Q2. If you have interacted with or used AI technologies, please specify the types of AI technology.",
        ["", "Diagnostic (e.g., Imaging)", "Treatment", "Planning", "Predictive Analytics",
         "Natural Language Processing (e.g., Chatbots)", "Other"])
    if "Other" in ai_types:
        ai_types_specify = st.text_input("Q2a. Please specify the types of AI technology.")

    ai_interaction_frequency = st.selectbox(
        "Q3. How often do you interact with or use AI technologies in your professional practice?",
        ["", "Daily", "Weekly", "Monthly", "Infrequently, less than once a month"])

    ai_impact = st.selectbox(
        "Q4. On a scale of 1-5, please rate the impact of AI technologies on your professional practice.",
        ["", "1. Extremely negative", "2. Negative", "3. Neutral", "4. Positive", "5. Extremely positive"])

st.header("Demand in Artificial Intelligence Technologies")

group = st.selectbox("Q0. Which group best describes your professional practice?",
                        [""] + list(st.session_state.group2occupations.keys()))

if group == '':
    st.stop()

occupation = st.selectbox("Q1. Which occupation best describes your daily professional practice",
                          [""] + list(st.session_state.group2occupations[group]))

if occupation != '':
    tasks = list(df[df['Occupation'] == occupation]['Detailed Work Activity'])
    for task in tasks:
        st.subheader(f"Task: {task}")
        job_duty = st.selectbox(f"Q2. Is '{task}' considered a part of your job duty?", ["", "No", "Yes"])
        performed_last_year = st.selectbox(f"Q3. Did you perform '{task}' in the past year?", ["", "No", "Yes"])
        ai_extent = st.selectbox(
            f"Q4. If AI can do '{task}' exactly as you did, to what extent do you want AI to do it?",
            ["", "To no extent", "To a limited extent", "To a moderate extent",
             "To a considerable extent", "To a full extent (completely automated by AI)", "Other"])
        if ai_extent == "Other":
            ai_extent_specify = st.text_input(f"Q3a. Please specify the extent to which you want AI to do '{task}'.")

        confidence = st.selectbox(
            f"Q5. On a scale of 1-5, how confident are you with your answer to Question 3 for '{task}'?",
            ["", "1. Extremely unconfident", "2. Unconfident", "3. Neutral", "4. Confident", "5. Extremely confident"])

submit = st.button("SUBMIT")

if submit:
    st.write("Thank you for your responses!")
