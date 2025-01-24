from openai import OpenAI
import os

def askgpt(prompt):
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

    stream = client.beta.threads.create_and_run(
        assistant_id=assistantID,
        model= "gpt-4o-mini",
        instructions= "You are acting as a sustainability tool.",
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
                {"role": "user", "content": prompt}
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
            
#askgpt("Explain BPs stance to sustainability")
