from mem0 import MemoryClient
import streamlit as st
import os
from groq import Groq
groq_client = Groq(
    api_key="NA",
    )

client = MemoryClient(api_key="NA")

def storing_memory(user_mgs,llm_msg, user_id):
    messages=[{"role":"user","content":user_mgs},
              {"role":"assistant","content":llm_msg}]
    client.add(messages, user_id=user_id)
    #print("Memory store successfully")

def retrieving_memory(query,user_id):
    results=client.search(query, user_id=user_id)
    #print("Memory retrieved successfully")
    formatted_results = ""
    for memory in results:    
        formatted_results += f"- {memory['memory']}\n"
    return  formatted_results

def groq_agent(retrieved_memory,query):
    
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"You are a helpful assisstant.You always have to be friendly and give customized responses based on the user's query and the retrieved memory.",
            },
            {
               
                "role": "user",
                "content":f"The question of the user is {query}.You have to answer the question of the user based on the :{retrieved_memory} ,if no information is found there then answer it by your own.Only give answer to the user question without bluffing or saying anything else.",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print(chat_completion.choices[0].message.content) 
    return chat_completion.choices[0].message.content

def run_memory_agent():
    user_id="john"
    query=st.text_input("Enter the query")
    #print(f"user query:{query}")
    if(st.button("generate")):
        if query:
            retrieved_memory=retrieving_memory(query,user_id)
            #print(f"Retrieved memory: {retrieved_memory}")
            result=groq_agent(retrieved_memory,query)
            st.write(result)
            storing_memory(query,result,user_id)
           

run_memory_agent()
