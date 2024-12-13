from streamlit_monaco import st_monaco
import streamlit as st
from ollama import chat
import os


def main():
    st.title("Korrektor")
    st.subheader("An AI Code Assistant")

    # Read the system prompt from a file
    if os.path.exists("system_prompt.txt"):
        with open("system_prompt.txt", "r") as file:
            system_prompt = file.read()
    else:
        system_prompt = ""
        st.warning("'system_prompt.txt' not found. Using empty system prompt.")

    # UI for displaying and modifying the system prompt
    with st.expander("View and Edit System Prompt"):
        st.write("**Current System Prompt:**")
        # Use a text area to allow editing of the system prompt
        system_prompt_area = st.text_area(
            "Edit System Prompt:", value=system_prompt, height=200
        )

        if st.button(
            "Get AI Suggestions to Enhance Prompt (🚧 Highly Experimental - does not work everytime)"
        ):
            # Get AI suggestions using Ollama
            suggestions = get_ai_suggestions(system_prompt_area)
            if suggestions:
                selected_suggestions = st.multiselect(
                    "Select suggestions to add to the prompt:",
                    suggestions,
                )
                if selected_suggestions:
                    # Update the system prompt
                    additional_text = "\n" + "\n".join(selected_suggestions)
                    system_prompt_area += additional_text
                    st.success("Selected suggestions have been added to the prompt.")
            else:
                st.info("No suggestions were generated.")

        # Add a save button to save the updated prompt
        if st.button("Save Updated Prompt"):
            # Save the updated prompt back to the file
            with open("system_prompt.txt", "w") as file:
                file.write(system_prompt_area)
            st.success("System prompt saved to 'system_prompt.txt'.")

    # Input for custom extra instructions
    extra_instructions = st.text_area("Add custom instructions (optional):", height=100)

    # Combine system prompt and extra instructions
    if extra_instructions.strip():
        final_system_prompt = system_prompt + "\n" + extra_instructions
    else:
        final_system_prompt = system_prompt

    # Code editor for user input
    content = st_monaco(
        value="/* YOUR CODE HERE */",
        height="300px",
        lineNumbers=True,
        minimap={"enabled": False},
        theme="vs-dark",
    )

    if st.button("Process code", icon="✨"):
        # Placeholder for streaming the response
        response_placeholder = st.empty()
        full_response = ""

        # Simulate streaming with the 'stream' parameter
        for response_chunk in chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": final_system_prompt},
                {"role": "user", "content": content},
            ],
            stream=True,  # Enable streaming
        ):
            if response_chunk.message:
                chunk_text = response_chunk.message.content
                full_response += chunk_text
                response_placeholder.markdown(full_response)


def get_ai_suggestions(prompt):
    # Use Ollama to generate AI suggestions
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI assistant that provides concise suggestions to enhance system prompts for code refactoring assistants. Provide each suggestion as a bullet point starting with '- '.",
            },
            {
                "role": "user",
                "content": f"Given the following system prompt:\n'''\n{prompt}\n'''\n\nProvide suggestions to improve and enhance it.",
            },
        ],
        stream=False,
    )

    suggestions = []
    if response and response.message:
        suggestions_text = response.message.content
        # Parse the suggestions assuming they are bullet points starting with '- '
        suggestions = [
            line.strip("- ").strip()
            for line in suggestions_text.split("\n")
            if line.strip().startswith("- ")
        ]
    return suggestions


if __name__ == "__main__":
    main()
