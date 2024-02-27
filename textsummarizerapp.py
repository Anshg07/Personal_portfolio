import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

# Define the main function to generate the summary
def generate_summary(article):
    summary = summarizer(article, max_length=200, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Streamlit app
def main():
    st.title("Text Summarization App")
    st.write("Enter your text below:")
    article = st.text_area("Text", height=400)
    
    if st.button("Summarize"):
        if not article:
            st.warning("Please enter some text to summarize.")
        else:
            summary = generate_summary(article)
            st.subheader("Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
