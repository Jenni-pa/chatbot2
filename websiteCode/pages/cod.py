from openai import OpenAI
import os

def askgpt(prompt):
    apiKey = os.getenv("OPEN_AI_API_KEY")

    client = OpenAI(
        api_key=apiKey,
        organization='org-u9i9OwAXA07gcPQKEuegv0O9',
        project='proj_KRs4JboRE6pdsFCWKMiChsqj',
    )

    stream = client.beta.threads.create_and_run(
        assistant_id="asst_tNrPc2cTx22OHcF4kXnVOqic",
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
                        "vs_OcLmRv10mqbD15nrcp0zk2Az"
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