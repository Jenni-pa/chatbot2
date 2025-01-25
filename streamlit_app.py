import streamlit as st
import pydeck
import pandas as pd
import streamlit.components.v1 as components
from streamlit import session_state as ss
from cod import askgpt, fileupload

st.title("Find companies you are looking for")

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

#reformatting companies to be in the same format as Names with their latitude and longitude
companies = pd.DataFrame(companies.items(), columns=["Name", "properties"])
#setting latitude and longitude,  the country and city:
companies[["Latitude", "Longitude", "Country", "City"]] = pd.DataFrame(companies["properties"].tolist(), index=companies.index)
#adding a size column to the companies dataframe
companies["size"] = 90000

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

addedCompany = None
addedCompanyChosen = None

# add check that map added companies less than 3
try:
    selectedcompanies = event.selection["objects"]["companies"]
except :
    selectedcompanies = []

st.session_state["allCompanies"] = companies
if len(selectedcompanies) > 0:
    company_names = [company["Name"] for company in selectedcompanies]
    pickedCompanies = st.multiselect("Selected Companie(s)", companies, company_names, max_selections=3)
else:
    pickedCompanies = st.multiselect("Selected Companie(s)", companies, max_selections=3)

prompts = {
        "one company": 
                "Regarding the {category}, what does {company} say in their annual report and ESG report? Perform a thorough analysis.",
        "2 companies":
                "Regarding the {category}, what do {companyA} and {companyB} say in their annual report and ESG report? Perform a thorough analysis and compare the companies.",
        "3 companies":
                "Regarding the {category}, what do {companyA}, {companyB} and {companyC} say in their annual report and ESG report? Perform a thorough analysis and compare the companies." 
}       

options = ["Ecological", "Social", "Governance", "Overall"]
selection = st.segmented_control("Select the focus area", options, selection_mode="single")
if selection == "Ecological":
        chosenCategory = st.radio("Select the subcategory", ["CO2 emissions", "Decarbonization Strategies & Initiatives", "Natural Resource Management"])
elif selection == "Social":
        chosenCategory = st.radio("Select the subcategory", ["Workers Rights", "Health & Safety Compliance", "Diversity, Equality and Inclusion"])
elif selection == "Governance":
        chosenCategory = st.radio("Select the subcategory", ["Regulatory Compliance", "Sustainability Reporting"])
elif selection == "Overall":
        chosenCategory = st.radio("Select the subcategory", ["Key Milestones & Achievements", "ESG-related Initiatives", "Awareness Regarding ESG-Responsibilities"])
else:
        chosenCategory = st.radio("Select the subcategory", ["CO2 emissions", "Decarbonization Strategies & Initiatives", "Natural Resource Management", "Workers Rights", "Health & Safety Compliance", "Diversity, Equality and Inclusion", "Regulatory Compliance", "Sustainability Reporting", "Key Milestones & Achievements", "ESG-related Initiatives", "Awareness Regarding ESG-Responsibilities"])

newCompany = None
if len(pickedCompanies) > 2:
    st.markdown("You can not add another company, please deselect at least one of your chosen companies to upload your own.")
else :
    st.markdown("Do you want to add a company?")
    with st.popover("📎",use_container_width=True):
                #file upload:
                uploaded_file = st.file_uploader("Choose a file",type=['txt'])
                NameOfCmpny = st.text_input('Company name:')
                
                if st.button("add company"):
                        st.write("Company added successfully")
                        new_company = {
                        "Name": NameOfCmpny,  # The name of the company
                        "Latitude": None,   # Missing latitude
                        "Longitude": None,  # Missing longitude
                        "Country": None,      # Missing country
                        "City": None,         # Missing city
                        "size": 90000         # Default size
                        }
                        newCompany = fileupload(uploaded_file.read())
                        companies._append(new_company, ignore_index=True)
                        addedCompany = True


if addedCompany == True :
    addedCompanyChosen = st.radio(f"Select your added company {NameOfCmpny}?", ["yes","no"])
if addedCompanyChosen == "yes":
    pickedCompanies.append(NameOfCmpny)

# muss noch vor add company
graphicalOutput = None
graphicalOutput = st.radio("Do you want to visualize your question with a graph?", ["yes","no"])
result = None

if len(pickedCompanies) == 1:
    if graphicalOutput == "yes":
        st.markdown(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0])+" Also show me a meaningful graph to visualize key numbers.")
        if st.button("send question"):
            st.write(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0])+" Also show me a meaningful graph to visualize key numbers.")
            st.write(newCompany.id if newCompany is not None else None )
            result = askgpt(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0])+" Also show me a meaningful graph to visualize key numbers.", newCompany.id if newCompany is not None else None )
    else:
        st.markdown(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0]))
        if st.button("send question"):
            st.write(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0]))
            st.write(newCompany.id if newCompany is not None else None )
            result = askgpt(prompts["one company"].format(category=chosenCategory, company=pickedCompanies[0]), newCompany.id if newCompany is not None else None)
elif len(pickedCompanies) == 2:
    if graphicalOutput == "yes":
        st.markdown(prompts["2 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1])+" Also show me a meaningful graph to visualize key numbers and differences.")
        if st.button("send question"):
            result = askgpt(prompts["2 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1])+" Also show me a meaningful graph to visualize key numbers and differences.", newCompany.id if newCompany is not None else None)
    else:
        st.markdown(prompts["2 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1]))
        if st.button("send question"):
            result = askgpt(prompts["2 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1]), newCompany.id if newCompany is not None else None)
elif len(pickedCompanies) == 3:
    if graphicalOutput == "yes":
        st.markdown(prompts["3 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1], companyC=pickedCompanies[2])+" Also show me a meaningful graph to visualize key numbers and differences.")
        if st.button("send question"):
            result = askgpt(prompts["3 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1], companyC=pickedCompanies[2])+" Also show me a meaningful graph to visualize key numbers and differences.", newCompany.id if newCompany is not None else None)
    else:
        st.markdown(prompts["3 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1], companyC=pickedCompanies[2]))
        if st.button("send question"):
            result = askgpt(prompts["3 companies"].format(category=chosenCategory, companyA=pickedCompanies[0], companyB=pickedCompanies[1], companyC=pickedCompanies[2]), newCompany.id if newCompany is not None else None)

st.markdown(f"Command Output: {result}", unsafe_allow_html=True)

# ASCI doc parser? 

#def run_command_page():
#    st.title("Ask GPT")
#    st.write("Testing calling the script to interact with the openai api")
#
#    uploaded_file = st.file_uploader("Choose a file",type=['txt'])
#    NameOfCompany = st.text_input('Company name:')
#    st.session_state.newCompany = None
#
#    if st.button("add company"):
#        st.session_state.newCompany = fileupload(uploaded_file.read())
#        st.write("Company added successfully")        
#
#
#    if st.button("Send request now", "without_attach,emt") and st.session_state.newCompany is None:
#        result = askgpt(f"Explain BPs stance to sustainability and compare with {NameOfCompany}" , None)
#        st.write(f"Command Output: {result}")
#
#    if st.button("Send request now", "with_attachment") and st.session_state.newCompany is not None:
#        result = askgpt(f"Explain BPs stance to sustainability and compare with {NameOfCompany}" , st.session_state.newCompany.id)
#        st.write(f"Command Output: {result}")
#
#run_command_page()
