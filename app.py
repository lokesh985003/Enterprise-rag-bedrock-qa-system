import streamlit as st
import boto3

# -----------------------------
# CONFIG (Based on your setup)
# -----------------------------
REGION = "ca-central-1"
KNOWLEDGE_BASE_ID = "OPQIFTPSBV"
MODEL_ARN = "arn:aws:bedrock:ca-central-1:404068502751:application-inference-profile/35wlozlhd579"

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Bedrock KB Chat", page_icon="💬")
st.title("💬 Bedrock Knowledge Base Chatbot")

st.write("Ask questions from your Knowledge Base (policyKB)")

# Input box
question = st.text_input("Enter your question:")

# Button click
if st.button("Ask"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        try:
            # Create Bedrock client
            client = boto3.client(
                "bedrock-agent-runtime",
                region_name="ca-central-1"
            )

            # Call Knowledge Base
            response = client.retrieve_and_generate(
                input={"text": question},
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": "OPQIFTPSBV",
                        "modelArn": MODEL_ARN,
                    },
                },
            )

            # Extract answer
            answer = response["output"]["text"]

            # Display
            st.subheader("Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")