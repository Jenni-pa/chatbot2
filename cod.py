from openai import OpenAI
import os

apiKey = os.getenv("OPEN_AI_API_KEY")
orgKey = os.getenv("OPEN_AI_ORG_KEY")
projectKey = os.getenv("OPEN_AI_PROJECT_KEY")
vectorStoreID = os.getenv("OPEN_AI_VECTOR_STORE_ID")
assistantID = os.getenv("OPEN_AI_ASSISTANT_ID")

client = OpenAI(
    api_key=apiKey,
    organization=orgKey,
    project=projectKey,
)

def fileupload(uploaded_file_name, uploaded_file_contents):
    return client.files.create(
        file= (uploaded_file_name, uploaded_file_contents),
        purpose="assistants"
    )

def askgpt(prompt, newCompanyId):
    attachment = None if newCompanyId is None else [{
        "file_id": newCompanyId,
        "tools": [{"type": "file_search"}]
        }]

    stream = client.beta.threads.create_and_run(
        assistant_id=assistantID,
        model= "gpt-4o-mini",
        instructions= "You are a Sustainability Analysis Assistant that provides objective, data-driven insights based on PDFs stored in a vector database. Your role is to extract, summarize, and compare factual sustainability data without speculation or opinion.If no relevant data is found, state this clearly rather than guessing.",
        tools= [
            {"type": "file_search"}
        ],
        tool_choice= {
            "type": "file_search"
        },
        thread={
            "tool_resources": {
                "file_search" : {
                    "vector_store_ids": [
                        vectorStoreID
                    ]
                }
            }, 
            "messages": [
                {
                    "role": "user", 
                    "content": prompt, 
                    "attachments": attachment
                }
            ]
        },
        stream=True
    )

    finishedResponse = ""

    for event in stream:
        if event.event == "thread.message.delta":
            eventText = event.data.delta.content[0].text.value
            print(eventText, end="")
            finishedResponse += eventText
    
    return finishedResponse
