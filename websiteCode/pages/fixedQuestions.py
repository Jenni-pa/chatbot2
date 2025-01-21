import streamlit as st
import streamlit.components.v1 as components

#this page will be used to display the fixed questions to ask chatGPT

st.set_page_config(page_title="Questions", page_icon="🧊", layout="wide")

def main():
    st.write('Here are some recommended questions you can ask:')
    #adding drop down menu to select the fixed questions
    
    col1, col2, col3,col4 = st.columns(4)

    with col1:
        #drop down menu of who what where when why how
        option1=st.selectbox('First', ['How', 'When', 'What', 'Explain', 'Compare', 'List'])

    with col2:
        #showing different types of questions based on option1
        match option1:
            case 'How':
                option2=st.selectbox('Second',['do the companies address','are the companies improving','effective were the companies in'])
            case 'When':
                option2=st.selectbox('Second',['did/will the companies achieve'])
            case 'What':
                option2=st.selectbox('Second',['is the companies focus in the area of','improvements will the companies make regarding','initiatives have the companies undertaken in'])
            case 'Explain':
                option2=st.selectbox('Second',['the companies efforts in the area of','how the companies operations affect','the companies focus on'])
            case 'Compare':
                option2=st.selectbox('Second',['the companies performance regarding','the companies performance against industry averages in'])
            case 'List':
                option2=st.selectbox('Second',['the companies','the challenges faced by the companies in the area of'])

    with col3:
        match option1:
            case 'How':
                match option2:
                    case 'do the companies address':
                        option3=st.selectbox('Third',['Decarbonization Initiatives','Natural Resource Management','Diversity, Equity, and Inclusion (DEI)','Health, Safety, and Environmental Compliance','Community Development Programs'])
                    case 'are the companies improving':
                        option3=st.selectbox('Third',['Emissions output','Efficiency in Operations','Carbon Neutral Operations','Sustainability Reporting Standards'])
                    case 'effective were the companies in':
                        option3=st.selectbox('Third',['Greenhouse Gas (GHG) Emissions Management','Climate Goals and Carbon Neutrality Targets','Energy Transition Strategies','Renewable Energy Investments','Technological Innovations in Operations','Environmental, Social, and Governance (ESG) Initiatives'])
            case 'When':
                option3=st.selectbox('Third',['Net zero emissions','Carbon Neutral Output'])
            case 'What':
                match option2:
                    case 'is the companies focus in the area of':
                        option3=st.selectbox('Third',['Sustainability','Reducing emissions'])
                    case 'improvements will the companies make regarding':
                        option3=st.selectbox('Third',['Climate Goals and Carbon Neutrality Targets','Environmental, Social, and Governance (ESG) Initiatives','Technological Innovations in Operations','Health, Safety, and Environmental Compliance'])
                    case 'initiatives have the companies undertaken in':
                        option3=st.selectbox('Third',['Climate Goals and Carbon Neutrality Targets','Environmental, Social, and Governance (ESG) Initiatives','Technological Innovations in Operations','Health, Safety, and Environmental Compliance'])
            case 'Explain':
                match option2:
                    case 'the companies efforts in the area of':
                        option3=st.selectbox('Third',['Health, Safety, and Environmental Compliance','Climate Goals and Carbon Neutrality Targets','Natural Resource Management','Diversity, Equity, and Inclusion (DEI)','Greenhouse Gas (GHG) Emissions Management'])
                    case 'how the companies operations affect':
                        option3=st.selectbox('Third',['world climate','the environment','the community where operations are based'])
                    case 'the companies focus on':
                        option3=st.selectbox('Third',['Health, Safety, and Environmental Compliance','Climate Goals and Carbon Neutrality Targets','Greenhouse Gas (GHG) Emissions Management','Environmental, Social, and Governance (ESG) Initiatives'])
            case 'Compare':
                match option2:
                    case 'the companies performance regarding':
                        option3=st.selectbox('Third',['Climate Goals and Carbon Neutrality Targets','Key Milestones and Achievements','Regulatory Compliance','Renewable Energy Projects','Emissions output','Decarbonization Initiatives'])
                    case 'the companies performance against industry averages in':
                        option3=st.selectbox('Third',['Climate Goals and Carbon Neutrality Targets','Emissions output','Natural Resource Management'])
            case 'List':
                match option2:
                    case 'the companies':
                        option3=st.selectbox('Third',['Decarbonization Initiatives','Environmental Sustainability Initiatives','Community Development Programs','Climate Goals and Carbon Neutrality Targets','Energy Transition Strategies','Renewable Energy Investments','Environmental, Social, and Governance (ESG) Initiatives'])
                    case 'the challenges faced by the companies in the area of':
                        option3=st.selectbox('Third',['Natural Resource Management','Carbon Neutral Operations','Greenhouse Gas (GHG) Emissions Management','Energy Transition Strategies','Reducing emissions'])

    with col4:
        match option1:
            case 'How':
                match option2:
                    case 'do the companies address':
                        match option3:
                            case 'Decarbonization Initiatives':
                                option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                            case 'Natural Resource Management':
                                option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                            case 'Diversity, Equity, and Inclusion (DEI)':
                                option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                            case 'Health, Safety, and Environmental Compliance':
                                option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                            case 'Community Development Programs':
                                option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                    case 'are the companies improving':
                        match option3:
                            case 'Emissions output':
                                option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
                            case 'Efficiency in Operations':
                                option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
                            case 'Carbon Neutral Operations':
                                option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
                            case 'Sustainability Reporting Standards':
                                option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
                    case 'effective were the companies in':
                        match option3:
                            case 'Greenhouse Gas (GHG) Emissions Management':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                            case 'Climate Goals and Carbon Neutrality Targets':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                            case 'Energy Transition Strategies':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                            case 'Renewable Energy Investments':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                            case 'Technological Innovations in Operations':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                            case 'Environmental, Social, and Governance (ESG) Initiatives':
                                option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
            case 'When':
                option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
            case 'What':
                match option2:
                    case 'is the companies focus in the area of':
                        option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                    case 'improvements will the companies make regarding':
                        option4=st.selectbox('Fourth',['Next year','In the next 3 years','In the future','-'])
                    case 'initiatives have the companies undertaken in':
                        option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
            case 'Explain':
                match option2:
                    case 'the companies efforts in the area of':
                        option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                    case 'how the companies operations affect':
                        option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
                    case 'the companies focus on':
                        option4=st.selectbox('Fourth',['Currently','Under new regulations','Given current economic conditions','-'])
            case 'Compare':
                match option2:
                    case 'the companies performance regarding':
                        option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                    case 'the companies performance against industry averages in':
                        option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
            case 'List':
                match option2:
                    case 'the companies':
                        option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])
                    case 'the challenges faced by the companies in the area of':
                        option4=st.selectbox('Fourth',['Last year','Over the past 3 years','In the past','-'])


    #with col5:
    #    #showing the selected question
    #    st.write(f'You selected:{option1} {option2} {option3} {option4}')
    default_chat_input_value = f"{option1} {option2} {option3} {option4}"


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    chatBox = st.container(height=300)  

    # React to user input
    prompt = st.chat_input("Chat input Here")


    with chatBox:
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt:
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            st.session_state.messages.append({"role": "user", "content": prompt})

    #now after getting user options, we can pick which lines to feed chatgpt with this question:
    #opening file sustainability_template.json to be shown with st.json:
    import json
    with open('pages/sustainability_template.json') as f:
        data = json.load(f)
    #st.json(data)

    #inside the json there is a key called companies, list them and add checkbox to select which company(s) to ask the question to
    companies = data['companies']

    companyCheckboxes = []
    #2d array for topics checkboxes per company
    topicCheckboxesPerCompany = [[]]

    for key, company_info in companies.items():
        company_name = company_info['name']
        companyCheckboxes.append(
        st.checkbox(company_name)
        )

    #show all topics in the json file and add checkbox to select which topic(s) to ask the question about:
    topics = data['topics']
    for i, company in enumerate(companies.keys()):
        topicCheckboxesPerCompany.append([])
        if companyCheckboxes[i]:
            st.write(f'Topics for: {companies[company]["name"]}')
            for key, topic_info in topics.items():
                topicsForCompany = topic_info[str(i)]
                topicCheckboxesPerCompany[i].append(
                st.checkbox(topicsForCompany, key=topicsForCompany)
                )

    default_chat_input_value = f"{option1} {option2} {option3} {option4}. answe using the following companies: {companyCheckboxes} and topics: {topicCheckboxesPerCompany}"


    js = f"""
        <script>
            function insertText(dummy_var_to_force_repeat_execution) {{
                var chatInput = parent.document.querySelector('textarea[data-testid="stChatInputTextArea"]');
                var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
                nativeInputValueSetter.call(chatInput, "{default_chat_input_value}");
                var event = new Event('input', {{ bubbles: true}});
                chatInput.dispatchEvent(event);
            }}
            insertText({len(st.session_state.messages)});
        </script>
        """
    components.html(js, height=0)




if __name__ == "__main__":
    main()