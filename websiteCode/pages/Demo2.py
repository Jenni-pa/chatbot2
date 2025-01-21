import numpy as np
import streamlit as st
import streamlit.components.v1 as components

from streamlit import session_state as ss

from browser_detection import browser_detection_engine as get_browser


# Define a variable to enable/disable chat_input()
if 'is_chat_input_disabled' not in ss:
    ss.is_chat_input_disabled = True

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'


def change():
    ss.sidebar_state = (
        "collapsed" if ss.sidebar_state == "expanded" else "expanded"
    )


st.set_page_config(page_title="Ask Sustaino-AI demo2", page_icon="🍃", layout="wide", initial_sidebar_state=ss.sidebar_state)

def main():
    browser = get_browser()
    #st.write('Here are some recommended questions you can ask:')
    #adding drop down menu to select the fixed questions

        #now after getting user options, we can pick which lines to feed chatgpt with this question:

    col50 = st.columns([100])[0]
    from streamlit import _bottom

    with _bottom:
        # browser is a json file, there is a key called 'isMobile' which is a boolean:
        if browser['isMobile']:
            bottomEnable = st.checkbox("Hide Bottom (for mobile)", value=True)
        else:
            bottomEnable = True
            # add markdown to remove div with class="stElementContainer element-container st-key-browser_engine st-emotion-cache-zin1ta e1f1d6gn4"
            st.markdown("""<style>.st-key-browser_engine.st-emotion-cache-zin1ta.e1f1d6gn4{display:none;}</style>""", unsafe_allow_html=True)

        if bottomEnable:
            col1, col2, col3,col4,col5,col6 = st.columns([40,100,100,40,60,20],gap='small',vertical_alignment='bottom')
        else:
            col1, col2, col3,col4,col5,col6 = None, None, None, None, None, None

    try:

        with col1:
            #drop down menu of who what where when why how
            option1=st.selectbox('Prefix',options=['How', 'When', 'What', 'Explain', 'Compare', 'List'])

        with col2:
            #showing different types of questions based on option1
            match option1:
                case 'How':
                    option2=st.selectbox('Time1',['do the companies address','are the companies improving','effective were the companies in'])
                case 'When':
                    option2=st.selectbox('Time1',['did/will the companies achieve'])
                case 'What':
                    option2=st.selectbox('Time1',['is the companies focus in the area of','improvements will the companies make regarding','initiatives have the companies undertaken in'])
                case 'Explain':
                    option2=st.selectbox('Time1',['the companies efforts in the area of','how the companies operations affect','the companies focus on'])
                case 'Compare':
                    option2=st.selectbox('Time1',['the companies performance regarding','the companies performance against industry averages in'])
                case 'List':
                    option2=st.selectbox('Time1',['the companies','the challenges faced by the companies in the area of'])

        with col3:
            match option1:
                case 'How':
                    match option2:
                        case 'do the companies address':
                            option3=st.selectbox('Topic',['Decarbonization Initiatives','Natural Resource Management','Diversity, Equity, and Inclusion (DEI)','Health, Safety, and Environmental Compliance','Community Development Programs'])
                        case 'are the companies improving':
                            option3=st.selectbox('Topic',['Emissions output','Efficiency in Operations','Carbon Neutral Operations','Sustainability Reporting Standards'])
                        case 'effective were the companies in':
                            option3=st.selectbox('Topic',['Greenhouse Gas (GHG) Emissions Management','Climate Goals and Carbon Neutrality Targets','Energy Transition Strategies','Renewable Energy Investments','Technological Innovations in Operations','Environmental, Social, and Governance (ESG) Initiatives'])
                case 'When':
                    option3=st.selectbox('Topic',['Net zero emissions','Carbon Neutral Output'])
                case 'What':
                    match option2:
                        case 'is the companies focus in the area of':
                            option3=st.selectbox('Topic',['Sustainability','Reducing emissions'])
                        case 'improvements will the companies make regarding':
                            option3=st.selectbox('Topic',['Climate Goals and Carbon Neutrality Targets','Environmental, Social, and Governance (ESG) Initiatives','Technological Innovations in Operations','Health, Safety, and Environmental Compliance'])
                        case 'initiatives have the companies undertaken in':
                            option3=st.selectbox('Topic',['Climate Goals and Carbon Neutrality Targets','Environmental, Social, and Governance (ESG) Initiatives','Technological Innovations in Operations','Health, Safety, and Environmental Compliance'])
                case 'Explain':
                    match option2:
                        case 'the companies efforts in the area of':
                            option3=st.selectbox('Topic',['Health, Safety, and Environmental Compliance','Climate Goals and Carbon Neutrality Targets','Natural Resource Management','Diversity, Equity, and Inclusion (DEI)','Greenhouse Gas (GHG) Emissions Management'])
                        case 'how the companies operations affect':
                            option3=st.selectbox('Topic',['world climate','the environment','the community where operations are based'])
                        case 'the companies focus on':
                            option3=st.selectbox('Topic',['Health, Safety, and Environmental Compliance','Climate Goals and Carbon Neutrality Targets','Greenhouse Gas (GHG) Emissions Management','Environmental, Social, and Governance (ESG) Initiatives'])
                case 'Compare':
                    match option2:
                        case 'the companies performance regarding':
                            option3=st.selectbox('Topic',['Climate Goals and Carbon Neutrality Targets','Key Milestones and Achievements','Regulatory Compliance','Renewable Energy Projects','Emissions output','Decarbonization Initiatives'])
                        case 'the companies performance against industry averages in':
                            option3=st.selectbox('Topic',['Climate Goals and Carbon Neutrality Targets','Emissions output','Natural Resource Management'])
                case 'List':
                    match option2:
                        case 'the companies':
                            option3=st.selectbox('Topic',['Decarbonization Initiatives','Environmental Sustainability Initiatives','Community Development Programs','Climate Goals and Carbon Neutrality Targets','Energy Transition Strategies','Renewable Energy Investments','Environmental, Social, and Governance (ESG) Initiatives'])
                        case 'the challenges faced by the companies in the area of':
                            option3=st.selectbox('Topic',['Natural Resource Management','Carbon Neutral Operations','Greenhouse Gas (GHG) Emissions Management','Energy Transition Strategies','Reducing emissions'])

        with col4:
            match option1:
                case 'How':
                    match option2:
                        case 'do the companies address':
                            match option3:
                                case 'Decarbonization Initiatives':
                                    option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                                case 'Natural Resource Management':
                                    option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                                case 'Diversity, Equity, and Inclusion (DEI)':
                                    option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                                case 'Health, Safety, and Environmental Compliance':
                                    option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                                case 'Community Development Programs':
                                    option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                        case 'are the companies improving':
                            match option3:
                                case 'Emissions output':
                                    option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                                case 'Efficiency in Operations':
                                    option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                                case 'Carbon Neutral Operations':
                                    option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                                case 'Sustainability Reporting Standards':
                                    option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                        case 'effective were the companies in':
                            match option3:
                                case 'Greenhouse Gas (GHG) Emissions Management':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                                case 'Climate Goals and Carbon Neutrality Targets':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                                case 'Energy Transition Strategies':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                                case 'Renewable Energy Investments':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                                case 'Technological Innovations in Operations':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                                case 'Environmental, Social, and Governance (ESG) Initiatives':
                                    option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                case 'When':
                    option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                case 'What':
                    match option2:
                        case 'is the companies focus in the area of':
                            option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                        case 'improvements will the companies make regarding':
                            option4=st.selectbox('Time2',['Next year','In the next 3 years','In the future','-'])
                        case 'initiatives have the companies undertaken in':
                            option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                case 'Explain':
                    match option2:
                        case 'the companies efforts in the area of':
                            option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                        case 'how the companies operations affect':
                            option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                        case 'the companies focus on':
                            option4=st.selectbox('Time2',['Currently','Under new regulations','Given current economic conditions','-'])
                case 'Compare':
                    match option2:
                        case 'the companies performance regarding':
                            option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                        case 'the companies performance against industry averages in':
                            option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                case 'List':
                    match option2:
                        case 'the companies':
                            option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])
                        case 'the challenges faced by the companies in the area of':
                            option4=st.selectbox('Time2',['Last year','Over the past 3 years','In the past','-'])


        with col5:
            #opening file sustainability_template.json to be shown with st.json:
            import json
            with open('pages/sustainability_template.json') as f:
                data = json.load(f)
            #st.json(data)

            #inside the json there is a key called companies, list them and add checkbox to select which company(s) to ask the question to
            companies = data['companies']

            selectedCmpnies= st.multiselect('Select companies:', [company_info['name'] for company_info in companies.values()])
            selectedCompanies = ', '.join(selectedCmpnies)


            if len(selectedCompanies) == 0:
                ss.is_chat_input_disabled = True
            else:
                ss.is_chat_input_disabled = False

        with col6:
            with st.popover("📎",use_container_width=True):
                #file upload:
                uploaded_file = st.file_uploader("Choose a file",type=['txt'])
                NameOfCmpny = st.text_input('Company name:')
                if st.button("add company"):
                    #add the company to the json file:
                    data['companies'].append({'name': NameOfCmpny,'file':'file path'})
                    with open('pages/sustainability_template.json', 'w') as f:
                        json.dump(data, f)
                    st.write("Company added successfully")
            
            prompt = st.button("➤",disabled=ss.is_chat_input_disabled,use_container_width=True)#st.chat_input("Chat input Here",disabled=ss.is_chat_input_disabled)
    # end try
    except:
        print('error')

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
                            st.markdown(f"{option1} {option2} {option3} {option4}. answer using the following companies: {selectedCompanies} and provide values for a graph in")

                        with st.chat_message("assistant"):
                            st.markdown(f"{option1} {option2} {option3} {option4}. answer using the following companies: {selectedCompanies} and provide values for a graph in")
                            st.bar_chart(assistantGraph)

            
                st.session_state.Chats.append([])
                st.session_state.Chats[j].append({"role": "user", "content": f"{option1} {option2} {option3} {option4}. answer using the following companies: {selectedCompanies} and provide values for a graph in"})
                st.session_state.Chats[j].append({"role": "ai", "content": f"{option1} {option2} {option3} {option4}. answer using the following companies: {selectedCompanies} and provide values for a graph in", "assistantGraph": assistantGraph})



        
            default_chat_input_value = f"{option1} {option2} {option3} {option4}. answer using the following companies: {selectedCompanies} and provide values for a graph in"



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
                }
                </style>
                """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
    cssFix()