import streamlit as st
import pydeck
import pandas as pd
import numpy as np


# took ideas from https://github.com/Sleepless-Samurais/check24-challenge-GUI

if "done_init" not in st.session_state:
    st.session_state["done_init"] = True
    st.set_page_config(
        initial_sidebar_state="collapsed",
        layout="wide"
    )
    st.markdown(
        """
    <style>
        .st-emotion-cache-yfhhig.ef3psqc5 {
            display: none;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

from browser_detection import browser_detection_engine as get_browser
browser = get_browser()
# running get browser creates an unnecessary div in the page adding gap on the top

companies = {
    "Saudi Aramco": {
        "latitude": 26.2777, "longitude": 50.2083, "country": "Saudi Arabia", "city": "Dhahran"
    },
    "China Petroleum & Chemical Corp. (SNPMF)": {
        "latitude": 39.9042, "longitude": 116.4074, "country": "China", "city": "Beijing"
    },
    "PetroChina Co. Ltd. (PCCYF)": {
        "latitude": 39.9042, "longitude": 116.4074, "country": "China", "city": "Beijing"
    },
    "Exxon Mobil Corp. (XOM)": {
        "latitude": 32.8140, "longitude": -96.9489, "country": "USA", "city": "Irving, Texas"
    },
    "Shell PLC (SHEL)": {
        "latitude": 51.5074, "longitude": -0.1278, "country": "UK", "city": "London"
    },
    "TotalEnergies SE (TTE)": {
        "latitude": 48.8955, "longitude": 2.2568, "country": "France", "city": "Courbevoie"
    },
    "Chevron Corp. (CVX)": {
        "latitude": 37.7799, "longitude": -121.9780, "country": "USA", "city": "San Ramon, California"
    },
    "BP PLC (BP)": {
        "latitude": 51.5074, "longitude": -0.1278, "country": "UK", "city": "London"
    },
    "Marathon Petroleum Corp. (MPC)": {
        "latitude": 41.0442, "longitude": -83.6499, "country": "USA", "city": "Findlay, Ohio"
    },
    "Valero Energy Corp. (VLO)": {
        "latitude": 29.4241, "longitude": -98.4936, "country": "USA", "city": "San Antonio, Texas"
    },
    "ConocoPhillips (COP)": {
        "latitude": 29.7604, "longitude": -95.3698, "country": "USA", "city": "Houston, Texas"
    },
    "Petrobras (PBR)": {
        "latitude": -22.9068, "longitude": -43.1729, "country": "Brazil", "city": "Rio de Janeiro"
    },
    "Enbridge (ENB)": {
        "latitude": 51.0447, "longitude": -114.0719, "country": "Canada", "city": "Calgary"
    },
    "Canadian Natural Resources (CNQ)": {
        "latitude": 51.0447, "longitude": -114.0719, "country": "Canada", "city": "Calgary"
    },
    "Equinor (EQNR)": {
        "latitude": 58.9690, "longitude": 5.7331, "country": "Norway", "city": "Stavanger"
    },
    "ENI (E)": {
        "latitude": 41.9028, "longitude": 12.4964, "country": "Italy", "city": "Rome"
    },
    "Woodside Energy (WDS)": {
        "latitude": -31.9505, "longitude": 115.8605, "country": "Australia", "city": "Perth"
    },
    "Repsol (REP.MC)": {
        "latitude": 40.4168, "longitude": -3.7038, "country": "Spain", "city": "Madrid"
    },
    "OMV (OMV.F)": {
        "latitude": 48.2082, "longitude": 16.3738, "country": "Austria", "city": "Vienna"
    },
    "Suncor Energy (SU)": {
        "latitude": 51.0447, "longitude": -114.0719, "country": "Canada", "city": "Calgary"
    }
}



st.markdown("<h1 style='text-align: center;'>Find companies you are looking for</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stMainBlockContainer {
            margin-top: -5em;
        }
            .stAppHeader {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .stAppDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)



#reformatting companies to be in the same format as Names with their latitude and longitude
companies = pd.DataFrame(companies.items(), columns=["Name", "properties"])
#setting latitude and longitude,  the country and city:
companies[["Latitude", "Longitude", "Country", "City"]] = pd.DataFrame(companies["properties"].tolist(), index=companies.index)
#adding a size column to the companies dataframe
companies["size"] = 90000
#st.write(companies)




point_layer2 = pydeck.Layer(
    "ScatterplotLayer",
    data=companies,
    id="companies",
    get_position=["Longitude", "Latitude"],
    get_color="[75, 75, 255, 205]",
    pickable=True,
    auto_highlight=True,
    get_radius="size",
)

view_state = pydeck.ViewState(
    latitude=48.1351, longitude=11.5820, zoom=3, min_zoom=0, max_zoom=20
)


chart2 = pydeck.Deck(
    point_layer2,
    initial_view_state=view_state,
    tooltip={"text": "{Name}\n{Latitude}, {Longitude}"},
)

event = st.pydeck_chart(chart2, on_select="rerun", selection_mode="multi-object")

try:
    selectedcompanies = event.selection["objects"]["companies"]
except :
    selectedcompanies = []

#st.write(selectedcompanies)

st.markdown('<style>.mapboxgl-ctrl-bottom-right{display: none;}</style>', unsafe_allow_html=True)


# create a streamlit multiselect where the previously selected companies should also appear:

st.session_state["allCompanies"] = companies
if len(selectedcompanies) > 0:
    company_names = [company["Name"] for company in selectedcompanies]
    pickedCompanies = st.multiselect("Selected Companie(s)", companies, company_names)
else:
    pickedCompanies = st.multiselect("Selected Companie(s)", companies)

col999 = st.columns([1])[0]


import streamlit.components.v1 as components

from streamlit import session_state as ss


# Define a variable to enable/disable chat_input()
if 'is_chat_input_disabled' not in ss:
    ss.is_chat_input_disabled = True


#st.write('Here are some recommended questions you can ask:')
#adding drop down menu to select the fixed questions

    #now after getting user options, we can pick which lines to feed chatgpt with this question:

col50 = st.columns([100])[0]
from streamlit import _bottom

with _bottom:
    # browser is a json file, there is a key called 'isMobile' which is a boolean:
    if browser['isMobile']:
        bottomEnable = st.checkbox("Show Question (for mobile)", value=False)
    else:
        bottomEnable = True
        # add markdown to remove div with class="stElementContainer element-container st-key-browser_engine st-emotion-cache-zin1ta e1f1d6gn4"
        st.markdown("""<style>.st-key-browser_engine.st-emotion-cache-zin1ta.e1f1d6gn4{display:none;}</style>""", unsafe_allow_html=True)

    if bottomEnable:
        colz = st.columns(1)[0]
        col1,col2,col3,col4 = st.columns([35,45,5,5],gap='small',vertical_alignment='bottom')
    else:
        colz = None
        col1,col6,col3,col4 = None, None, None, None

try:
    prompts = {
    ("Ecological", "CO2 emissions"): "Which performance regarding ecological factors does {company} show according to their annual report and the ESG-report of the company regarding their CO2 emissions? Perform a thorough analysis.",
    ("Ecological", "Decarbonization Strategies & Initiatives"): "Which concrete initiatives and strategies regarding decarbonizations does {company} show according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Ecological", "Natural Resource Management"): "In which specific ways does {company} address the sustainable management of natural resources according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Social", "Workers Rights"): "In which specific ways does {company} address workers rights according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Social", "Health & Safety Compliance"): "In which specific ways does {company} ensure health and safety compliance according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Social", "Diversity, Equality and Inclusion"): "In which specific ways does {company} ensure diversity, equality and inclusion according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Governance", "Regulatory Compliance"): "In which specific ways does {company} ensure regulatory compliance regarding ESG-aspects according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Governance", "Sustainability Reporting"): "Which specific sustainability reports does {company} provide according to their annual report and the ESG-report of the company ? Perform a thorough analysis.",
    ("Overall", "Key Milestones & Achievements"): "Analyze the performance of {company} in regard to key milestones and achievements regarding ESG-aspects according to their annual report and the ESG-report? Perform a thorough analysis.",
    ("Overall", "ESG-related Initiatives"): "Perform a thorough analysis of ESG-related initiatives conducted by {company} according to their annual report and the ESG-report.",
    ("Overall", "Awareness Regarding ESG-Responsibilities"): "Perform a thorough analysis indicating the awareness of {company} regarding their ESG-responsibilities."
}
    lastSelectedCompany = pickedCompanies[-1] if len(pickedCompanies) > 0 else ""


    with col1:
            question1 = st.radio("Select the focus area", ["Ecological", "Social", "Governance", "Overall"],horizontal=True)
    with col2:
        # question2 should only have elements that are in prompts and have the same question1:

        if question1 == "Ecological":
            question2 = st.radio("Select the subcategory", ["CO2 emissions", "Decarbonization Strategies & Initiatives", "Natural Resource Management"],horizontal=True)
        elif question1 == "Social":
            question2 = st.radio("Select the subcategory", ["Workers Rights", "Health & Safety Compliance", "Diversity, Equality and Inclusion"],horizontal=True)
        elif question1 == "Governance":
            question2 = st.radio("Select the subcategory", ["Regulatory Compliance", "Sustainability Reporting"],horizontal=True)
        elif question1 == "Overall":
            question2 = st.radio("Select the subcategory", ["Key Milestones & Achievements", "ESG-related Initiatives", "Awareness Regarding ESG-Responsibilities"],horizontal=True)
        else:
            question2 = st.radio("Select the subcategory", ["CO2 emissions", "Decarbonization Strategies & Initiatives", "Natural Resource Management", "Workers Rights", "Health & Safety Compliance", "Diversity, Equality and Inclusion", "Regulatory Compliance", "Sustainability Reporting", "Key Milestones & Achievements", "ESG-related Initiatives", "Awareness Regarding ESG-Responsibilities"],horizontal=True)
        # Get the prompt based on selections
        promptz = prompts.get((question1, question2), "No prompt available for the selected options.")
        default_chat_input_value = promptz.format(company=lastSelectedCompany)

    with colz:
        st.write(default_chat_input_value)



    with col3:
        with st.popover("📎",use_container_width=True):
            #file upload:
            uploaded_file = st.file_uploader("Choose a file",type=['txt'])
            NameOfCmpny = st.text_input('Company name:')
            if st.button("add company"):
                st.write("Company added successfully")
        #st.write(pickedCompanies)
    with col4:
        if len(pickedCompanies) > 0:
            ss.is_chat_input_disabled = False
        else:
            ss.is_chat_input_disabled = True
        prompt = st.button("➤",disabled=ss.is_chat_input_disabled,use_container_width=True,help="select companie(s) before asking questions")#st.chat_input("Chat input Here",disabled=ss.is_chat_input_disabled)
# end try
except:
    print('error')

#promptz = f"{option1} {option2} {option3} {option4}. answer using the following companies: {pickedCompanies} and provide values for a graph in"

with col50:
    # Initialize chat history
    if "Chats" not in st.session_state:
        st.session_state.Chats = [[]]
        # every chat has a message from user and a response from the AI.
        # every chat is stored in a separate chatbox.
        # adding an initial dummy value:
        st.session_state.Chats[0].append({"role": "AI", "content": "Hello, I am Sustaino-AI. How can I help you today?"})
    
    chatBoxes = st.columns(1)
    
            # a for loop with integers to go through the chats:
    for i, chat in enumerate(st.session_state.Chats):
        if i!=0:
            chatBoxes.append(st.container(height=600))
            with chatBoxes[i]:
                col10,col11 = st.columns([95,5])
                with col10:
                    for message in chat:
                        with st.chat_message(message["role"]):
                            st.markdown(message["content"])
                            if "assistantGraph" in message:
                                st.bar_chart(message["assistantGraph"])


    try:
        if prompt:
            j = len(st.session_state.Chats)
            # Display user message in chat message container
            chatBoxes.append(st.container(height=600))
            assistantGraph = np.random.randn(30, 3)
            with chatBoxes[j]:
                col12,col13 = st.columns([95,5])
                with col12:

                    with st.chat_message("user"):
                        st.markdown(default_chat_input_value)


                    with st.chat_message("assistant"):
                        st.markdown(default_chat_input_value)
                        st.bar_chart(assistantGraph)

        
            st.session_state.Chats.append([])
            st.session_state.Chats[j].append({"role": "user", "content": default_chat_input_value})
            st.session_state.Chats[j].append({"role": "ai", "content": default_chat_input_value, "assistantGraph": assistantGraph})



    

        js = f"""
            <script>
                function insertText(dummy_var_to_force_repeat_execution) {{
                    var chatInput = parent.document.querySelector('textarea[data-testid="stChatInputTextArea"]');
                    var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
                    nativeInputValueSetter.call(chatInput, "{default_chat_input_value}");
                    var event = new Event('input', {{ bubbles: true}});
                    chatInput.dispatchEvent(event);
                }}
                insertText({len(st.session_state.Chats)});
            </script>
            """
        components.html(js, height=0)

    except:
        print('error')



def cssFix():
    # Remove whitespace from the top of the page and sidebar
        st.markdown("""
                <style>
                    .stAppHeader {
                        display: none;
                    }
                    .stMainBlockContainer {
                        padding-top: 10px;
                        padding-bottom: 10px;
                    }
                    .stIFrame {
                        display: none;
                    }
                div[data-testid="stBottomBlockContainer"] {
                    padding-bottom: 10px;
                    padding-top: 0px;
                    padding-right: 40px;
                    padding-left: 40px;
                    margin-top: -15px;
                }
                </style>
                """, unsafe_allow_html=True)

cssFix()