# Y2K_stylist_chatbot

For this project i wanted to play around with making my own chatbot on one of my favourite topics, y2k fashion

My learnings from this project so far:

**Prompt Engineering**
* I used prompt engineering to give the model a role as a stylist called Cherry specialising in y2k fashion
* ```prompt = f"You are a fashion stylist specialising in Y2K looks. Answer this style request: {user_imput}" ```

**Virtual Environments**
* It's important to keep your dependencies isolated and aviod version conflicts with other projects
* Easier to set up your project across different machines
* General best practice for Python projects

**Hugging Face Transformers**
* The transformers library is used to load my large pre-trained language model, GPT-2
* Once the model was downloaded it's cached locally for reuse
* I used pipeline() to abstract the model into a more usable interface for text generation

**Handeling User Input and Responses**
* When the user types a message, it's combined with the prompt and then passed into the model
*  The model then generates text, and only produces the new part of the response by removing the original prompt so the bots reply can sound more natural
  ```response[len(prompt):] ```

Example:
* User input: "Hi Cherry, what should I wear today?"
* Chatbot output version 1: "Hi Cherry, what should I wear today? You should definitely wear something bright and comfy!"
* Chatbot output version 2 (removing prompt) : "You should definitely wear something bright and comfy!"
  
**Streamlit for Building a Web Interface**
* It's a python library
* I created an input box for user input
  ```user_imput = st.text_input("You:", "")```
* The convo updates dynamically using ```st.session_state``` to store and display chat history
* Each new message is added as a tuple: ("You", message) or ("Stylist", response)
* Tuple is an immutable data structure that stores a collection of values, text, numbers, booleans


