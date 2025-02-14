# import streamlit as st
# import google.generativeai as genai
# from langdetect import detect
# from googletrans import Translator
# import time
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # api_key = os.getenv("GEMINI_API_KEY")
# api_key = st.secrets["GEMINI_API_KEY"]


# # Set your Gemini API key
# genai.configure(api_key=api_key)

# # Initialize the model
# model = genai.GenerativeModel('gemini-pro')

# # Function to detect language
# def detect_language(text):
#     try:
#         lang = detect(text)
#         # Map Gujarati text (which might be detected as other Indian languages) to 'gu'
#         if any(char in text for char in 'અાીુૂેૈોૌંઃ્'):
#             return 'gu'
#         return lang
#     except:
#         return 'en'  # Default to English if detection fails

# # Function to translate text with retry mechanism
# def translate_text(text, dest_language, max_retries=3):
#     translator = Translator()
#     for attempt in range(max_retries):
#         try:
#             translation = translator.translate(text, dest=dest_language)
#             return translation.text
#         except Exception as e:
#             if attempt == max_retries - 1:
#                 st.error(f"Translation error: {str(e)}")
#                 return text
#             time.sleep(1)  # Wait before retrying

# # Function to generate responses
# def generate_response(prompt, input_language):
#     try:
#         # Add language-specific context
#         if input_language == 'hi':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Hindi language with proper terminology.
#             Question: """
#         elif input_language == 'gu':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Gujarati language with proper terminology.
#             Question: """
#         else:
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming,
#             crops, and weather.
#             Question: """
            
#         full_prompt = context + prompt

#         # Generate response using Gemini API
#         response = model.generate_content(full_prompt)
        
#         # Check if translation is needed
#         response_language = detect_language(response.text)
#         if input_language in ['hi', 'gu'] and response_language == 'en':
#             return translate_text(response.text, input_language)
        
#         return response.text
#     except Exception as e:
#         return f"Error generating response: {str(e)}"

# # Function to get language name for display
# def get_language_name(lang_code):
#     language_names = {
#         'en': 'English',
#         'hi': 'हिंदी',
#         'gu': 'ગુજરાતી'
#     }
#     return language_names.get(lang_code, 'English')

# # Streamlit UI
# def main():
#     st.title("કૃષિ સહાયક ચેટબોટ 🌾")
#     st.title("कृषि सहायक चैटबॉट 🌾")
#     st.title("Agriculture Assistant Chatbot 🌾")
    
#     # Language selection
#     selected_language = st.selectbox(
#         "Select your preferred language / भाषा चुनें / તમારી પસંદગીની ભાષા પસંદ કરો",
#         ['en', 'hi', 'gu'],
#         format_func=get_language_name
#     )

#     # Multilingual welcome message
#     welcome_messages = {
#         'en': "Ask me anything about agriculture, crop production, or weather!",
#         'hi': "कृषि, फसल उत्पादन, या मौसम के बारे में कुछ भी पूछें!",
#         'gu': "ખેતી, પાક ઉત્પાદન અથવા હવામાન વિશે કંઈપણ પૂછો!"
#     }
#     st.write(welcome_messages[selected_language])

#     # Initialize chat history
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []

#     # User input placeholder text in multiple languages
#     placeholder_text = {
#         'en': "Type your question here...",
#         'hi': "अपना प्रश्न यहां टाइप करें...",
#         'gu': "તમારો પ્રશ્ન અહીં ટાઈપ કરો..."
#     }

#     # User input
#     user_input = st.text_input(
#         "💭",
#         placeholder=placeholder_text[selected_language]
#     )

#     if user_input:
#         # Detect language of the input
#         input_language = detect_language(user_input)
        
#         # Generate response
#         response = generate_response(user_input, input_language)
        
#         # Add to chat history
#         st.session_state.chat_history.append(("user", user_input))
#         st.session_state.chat_history.append(("bot", response))

#     # Display chat history with localized labels
#     chat_labels = {
#         'en': {'user': 'You', 'bot': 'Bot'},
#         'hi': {'user': 'आप', 'bot': 'बॉट'},
#         'gu': {'user': 'તમે', 'bot': 'બોટ'}
#     }

#     for role, message in st.session_state.chat_history:
#         if role == "user":
#             st.write(f"👤 {chat_labels[selected_language]['user']}: {message}")
#         else:
#             st.write(f"🤖 {chat_labels[selected_language]['bot']}: {message}")



# import streamlit as st
# import google.generativeai as genai
# from langdetect import detect
# from googletrans import Translator
# import time
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # api_key = os.getenv("GEMINI_API_KEY")
# api_key = st.secrets["GEMINI_API_KEY"]

# # Set your Gemini API key
# genai.configure(api_key=api_key)

# # Initialize the model
# model = genai.GenerativeModel('gemini-pro')

# # Function to detect language
# def detect_language(text):
#     try:
#         lang = detect(text)
#         # Map Gujarati text (which might be detected as other Indian languages) to 'gu'
#         if any(char in text for char in 'અાીુૂેૈોૌંઃ્'):
#             return 'gu'
#         return lang
#     except:
#         return 'en'  # Default to English if detection fails

# # Function to translate text with retry mechanism
# def translate_text(text, dest_language, max_retries=3):
#     translator = Translator()
#     for attempt in range(max_retries):
#         try:
#             translation = translator.translate(text, dest=dest_language)
#             return translation.text
#         except Exception as e:
#             if attempt == max_retries - 1:
#                 st.error(f"Translation error: {str(e)}")
#                 return text
#             time.sleep(1)  # Wait before retrying

# # Function to check if the input is agriculture-related
# def is_agriculture_related(text):
#     """Semantic analysis to determine if the input is agriculture-related"""
#     prompt = f"""
#     Analyze the following input and determine if it is related to agriculture, farming, crops, weather, soil, fertilizers, or farmers. 
#     Respond with only 'yes' or 'no'.

#     Input: {text}
#     """
#     try:
#         response = model.generate_content(prompt)
#         return response.text.strip().lower() == 'yes'
#     except Exception as e:
#         st.error(f"Error in semantic analysis: {str(e)}")
#         return False

# # Function to generate responses
# def generate_response(prompt, input_language):
#     try:
#         # Add language-specific context
#         if input_language == 'hi':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Hindi language with proper terminology.
#             Question: """
#         elif input_language == 'gu':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Gujarati language with proper terminology.
#             Question: """
#         else:
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming,
#             crops, and weather.
#             Question: """
            
#         full_prompt = context + prompt

#         # Generate response using Gemini API
#         response = model.generate_content(full_prompt)
        
#         # Check if translation is needed
#         response_language = detect_language(response.text)
#         if input_language in ['hi', 'gu'] and response_language == 'en':
#             return translate_text(response.text, input_language)
        
#         return response.text
#     except Exception as e:
#         return f"Error generating response: {str(e)}"

# # Function to get language name for display
# def get_language_name(lang_code):
#     language_names = {
#         'en': 'English',
#         'hi': 'हिंदी',
#         'gu': 'ગુજરાતી'
#     }
#     return language_names.get(lang_code, 'English')

# # Streamlit UI
# def main():
#     st.title("કૃષિ સહાયક ચેટબોટ 🌾")
#     st.title("कृषि सहायक चैटबॉट 🌾")
#     st.title("Agriculture Assistant Chatbot 🌾")
    
#     # Language selection
#     selected_language = st.selectbox(
#         "Select your preferred language / भाषा चुनें / તમારી પસંદગીની ભાષા પસંદ કરો",
#         ['en', 'hi', 'gu'],
#         format_func=get_language_name
#     )

#     # Multilingual welcome message
#     welcome_messages = {
#         'en': "Ask me anything about agriculture, crop production, or weather!",
#         'hi': "कृषि, फसल उत्पादन, या मौसम के बारे में कुछ भी पूछें!",
#         'gu': "ખેતી, પાક ઉત્પાદન અથવા હવામાન વિશે કંઈપણ પૂછો!"
#     }
#     st.write(welcome_messages[selected_language])

#     # Initialize chat history
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []

#     # User input placeholder text in multiple languages
#     placeholder_text = {
#         'en': "Type your question here...",
#         'hi': "अपना प्रश्न यहां टाइप करें...",
#         'gu': "તમારો પ્રશ્ન અહીં ટાઈપ કરો..."
#     }

#     # User input
#     user_input = st.text_input(
#         "💭",
#         placeholder=placeholder_text[selected_language]
#     )

#     if user_input:
#         # Detect language of the input
#         input_language = detect_language(user_input)
        
#         # Check if the question is agriculture-related
#         if not is_agriculture_related(user_input):
#             error_messages = {
#                 'en': "Please ask a question related to agriculture, farming, crops, weather, soil, fertilizers, or farmers.",
#                 'hi': "कृपया कृषि, खेती, फसल, मौसम, मिट्टी, उर्वरक, या किसानों से संबंधित प्रश्न पूछें।",
#                 'gu': "કૃપા કરીને ખેતી, પાક, હવામાન, માટી, ખાતર અથવા ખેડૂતો સંબંધિત પ્રશ્ન પૂછો."
#             }
#             st.error(error_messages[selected_language])
#         else:
#             # Generate response
#             response = generate_response(user_input, input_language)
            
#             # Add to chat history
#             st.session_state.chat_history.append(("user", user_input))
#             st.session_state.chat_history.append(("bot", response))

#     # Display chat history with localized labels
#     chat_labels = {
#         'en': {'user': 'You', 'bot': 'Bot'},
#         'hi': {'user': 'आप', 'bot': 'बॉट'},
#         'gu': {'user': 'તમે', 'bot': 'બોટ'}
#     }

#     for role, message in st.session_state.chat_history:
#         if role == "user":
#             st.write(f"👤 {chat_labels[selected_language]['user']}: {message}")
#         else:
#             st.write(f"🤖 {chat_labels[selected_language]['bot']}: {message}")

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     main()




# import streamlit as st
# import google.generativeai as genai
# from langdetect import detect
# from googletrans import Translator
# import time
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # api_key = os.getenv("GEMINI_API_KEY")
# api_key = st.secrets["GEMINI_API_KEY"]

# # Set your Gemini API key
# genai.configure(api_key=api_key)

# # Initialize the model
# model = genai.GenerativeModel('gemini-pro')

# # Function to detect language
# def detect_language(text):
#     try:
#         lang = detect(text)
#         # Map Gujarati text (which might be detected as other Indian languages) to 'gu'
#         if any(char in text for char in 'અાીુૂેૈોૌંઃ્'):
#             return 'gu'
#         return lang
#     except:
#         return 'en'  # Default to English if detection fails

# # Function to translate text with retry mechanism
# def translate_text(text, dest_language, max_retries=3):
#     translator = Translator()
#     for attempt in range(max_retries):
#         try:
#             translation = translator.translate(text, dest=dest_language)
#             return translation.text
#         except Exception as e:
#             if attempt == max_retries - 1:
#                 st.error(f"Translation error: {str(e)}")
#                 return text
#             time.sleep(1)  # Wait before retrying

# # Function to check if the input is a greeting
# def is_greeting(text):
#     """Check if the input is a greeting"""
#     greetings = {
#         'en': ['hello', 'hi', 'good morning', 'good afternoon', 'good evening', 'hey'],
#         'hi': ['नमस्ते', 'हाय', 'नमस्कार', 'सुप्रभात', 'शुभ संध्या'],
#         'gu': ['નમસ્તે', 'હાય', 'ગુડ મોર્નિંગ', 'ગુડ આફ્ટરનૂન', 'ગુડ ઈવનિંગ']
#     }
#     text_lower = text.lower()
#     input_language = detect_language(text)
#     return any(greeting in text_lower for greeting in greetings[input_language])

# # Function to check if the input is agriculture-related
# def is_agriculture_related(text):
#     """Semantic analysis to determine if the input is agriculture-related"""
#     prompt = f"""
#     Analyze the following input and determine if it is related to agriculture, farming, crops, weather, soil, fertilizers, or farmers. 
#     Respond with only 'yes' or 'no'.

#     Input: {text}
#     """
#     try:
#         response = model.generate_content(prompt)
#         return response.text.strip().lower() == 'yes'
#     except Exception as e:
#         st.error(f"Error in semantic analysis: {str(e)}")
#         return False

# # Function to generate responses
# def generate_response(prompt, input_language):
#     try:
#         # Add language-specific context
#         if input_language == 'hi':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Hindi language with proper terminology.
#             Question: """
#         elif input_language == 'gu':
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming, 
#             crops, and weather. Respond in Gujarati language with proper terminology.
#             Question: """
#         else:
#             context = """
#             You are an agricultural expert chatbot. Provide detailed answers about farming,
#             crops, and weather.
#             Question: """
            
#         full_prompt = context + prompt

#         # Generate response using Gemini API
#         response = model.generate_content(full_prompt)
        
#         # Check if translation is needed
#         response_language = detect_language(response.text)
#         if input_language in ['hi', 'gu'] and response_language == 'en':
#             return translate_text(response.text, input_language)
        
#         return response.text
#     except Exception as e:
#         return f"Error generating response: {str(e)}"

# # Function to get language name for display
# def get_language_name(lang_code):
#     language_names = {
#         'en': 'English',
#         'hi': 'हिंदी',
#         'gu': 'ગુજરાતી'
#     }
#     return language_names.get(lang_code, 'English')

# # Streamlit UI
# def main():
#     st.title("કૃષિ સહાયક ચેટબોટ 🌾")
#     st.title("कृषि सहायक चैटबॉट 🌾")
#     st.title("Agriculture Assistant Chatbot 🌾")
    
#     # Language selection
#     selected_language = st.selectbox(
#         "Select your preferred language / भाषा चुनें / તમારી પસંદગીની ભાષા પસંદ કરો",
#         ['en', 'hi', 'gu'],
#         format_func=get_language_name
#     )

#     # Multilingual welcome message
#     welcome_messages = {
#         'en': "Ask me anything about agriculture, crop production, or weather!",
#         'hi': "कृषि, फसल उत्पादन, या मौसम के बारे में कुछ भी पूछें!",
#         'gu': "ખેતી, પાક ઉત્પાદન અથવા હવામાન વિશે કંઈપણ પૂછો!"
#     }
#     st.write(welcome_messages[selected_language])

#     # Initialize chat history
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []

#     # User input placeholder text in multiple languages
#     placeholder_text = {
#         'en': "Type your question here...",
#         'hi': "अपना प्रश्न यहां टाइप करें...",
#         'gu': "તમારો પ્રશ્ન અહીં ટાઈપ કરો..."
#     }

#     # User input
#     user_input = st.text_input(
#         "💭",
#         placeholder=placeholder_text[selected_language]
#     )

#     if user_input:
#         # Detect language of the input
#         input_language = detect_language(user_input)
        
#         # Check if the input is a greeting
#         if is_greeting(user_input):
#             greetings = {
#                 'en': ["Hello! How can I assist you with agriculture today?", "Hi there! What's your agriculture-related question?"],
#                 'hi': ["नमस्ते! आज मैं आपकी कृषि संबंधी मदद कैसे कर सकता हूँ?", "हाय! आपका कृषि संबंधी प्रश्न क्या है?"],
#                 'gu': ["નમસ્તે! આજે હું તમારી ખેતી સંબંધિત મદદ કેવી રીતે કરી શકું?", "હાય! તમારો ખેતી સંબંધિત પ્રશ્ન શું છે?"]
#             }
#             import random
#             response = random.choice(greetings[input_language])
#         else:
#             # Check if the question is agriculture-related
#             if not is_agriculture_related(user_input):
#                 error_messages = {
#                     'en': "Please ask a question related to agriculture, farming, crops, weather, soil, fertilizers, or farmers.",
#                     'hi': "कृपया कृषि, खेती, फसल, मौसम, मिट्टी, उर्वरक, या किसानों से संबंधित प्रश्न पूछें।",
#                     'gu': "કૃપા કરીને ખેતી, પાક, હવામાન, માટી, ખાતર અથવા ખેડૂતો સંબંધિત પ્રશ્ન પૂછો."
#                 }
#                 st.error(error_messages[selected_language])
#                 return
#             else:
#                 # Generate response
#                 response = generate_response(user_input, input_language)
        
#         # Add to chat history
#         st.session_state.chat_history.append(("user", user_input))
#         st.session_state.chat_history.append(("bot", response))

#     # Display chat history with localized labels
#     chat_labels = {
#         'en': {'user': 'You', 'bot': 'Bot'},
#         'hi': {'user': 'आप', 'bot': 'बॉट'},
#         'gu': {'user': 'તમે', 'bot': 'બોટ'}
#     }

#     for role, message in st.session_state.chat_history:
#         if role == "user":
#             st.write(f"👤 {chat_labels[selected_language]['user']}: {message}")
#         else:
#             st.write(f"🤖 {chat_labels[selected_language]['bot']}: {message}")

# if __name__ == "__main__":
#     main()



import streamlit as st
import google.generativeai as genai
from langdetect import detect
from googletrans import Translator
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
api_key = st.secrets["GEMINI_API_KEY"]

# Set your Gemini API key
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Function to detect language
def detect_language(text):
    try:
        lang = detect(text)
        # Map Gujarati text (which might be detected as other Indian languages) to 'gu'
        if any(char in text for char in 'અાીુૂેૈોૌંઃ્'):
            return 'gu'
        # Ensure the detected language is one of the supported languages
        if lang in ['en', 'hi', 'gu']:
            return lang
        else:
            return 'en'  # Default to English if the detected language is not supported
    except:
        return 'en'  # Default to English if detection fails

# Function to translate text with retry mechanism
def translate_text(text, dest_language, max_retries=3):
    translator = Translator()
    for attempt in range(max_retries):
        try:
            translation = translator.translate(text, dest=dest_language)
            return translation.text
        except Exception as e:
            if attempt == max_retries - 1:
                st.error(f"Translation error: {str(e)}")
                return text
            time.sleep(1)  # Wait before retrying

# Function to check if the input is a greeting
def is_greeting(text):
    """Check if the input is a greeting"""
    greetings = {
        'en': ['hello', 'hi', 'good morning', 'good afternoon', 'good evening', 'hey'],
        'hi': ['नमस्ते', 'हाय', 'नमस्कार', 'सुप्रभात', 'शुभ संध्या'],
        'gu': ['નમસ્તે', 'હાય', 'ગુડ મોર્નિંગ', 'ગુડ આફ્ટરનૂન', 'ગુડ ઈવનિંગ']
    }
    text_lower = text.lower()
    input_language = detect_language(text)
    # Default to English if the input language is not in the greetings dictionary
    if input_language not in greetings:
        input_language = 'en'
    return any(greeting in text_lower for greeting in greetings[input_language])

# Function to check if the input is agriculture-related
def is_agriculture_related(text):
    """Semantic analysis to determine if the input is agriculture-related"""
    prompt = f"""
    Analyze the following input and determine if it is related to agriculture, farming, crops, weather, soil, fertilizers, or farmers. 
    Respond with only 'yes' or 'no'.

    Input: {text}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip().lower() == 'yes'
    except Exception as e:
        st.error(f"Error in semantic analysis: {str(e)}")
        return False

# Function to generate responses
def generate_response(prompt, input_language):
    try:
        # Add language-specific context
        if input_language == 'hi':
            context = """
            You are an agricultural expert chatbot. Provide detailed answers about farming, 
            crops, and weather. Respond in Hindi language with proper terminology.
            Question: """
        elif input_language == 'gu':
            context = """
            You are an agricultural expert chatbot. Provide detailed answers about farming, 
            crops, and weather. Respond in Gujarati language with proper terminology.
            Question: """
        else:
            context = """
            You are an agricultural expert chatbot. Provide detailed answers about farming,
            crops, and weather.
            Question: """
            
        full_prompt = context + prompt

        # Generate response using Gemini API
        response = model.generate_content(full_prompt)
        
        # Check if translation is needed
        response_language = detect_language(response.text)
        if input_language in ['hi', 'gu'] and response_language == 'en':
            return translate_text(response.text, input_language)
        
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Function to get language name for display
def get_language_name(lang_code):
    language_names = {
        'en': 'English',
        'hi': 'हिंदी',
        'gu': 'ગુજરાતી'
    }
    return language_names.get(lang_code, 'English')

# Streamlit UI
def main():
    st.title("કૃષિ સહાયક ચેટબોટ 🌾")
    st.title("कृषि सहायक चैटबॉट 🌾")
    st.title("Agriculture Assistant Chatbot 🌾")
    
    # Language selection
    selected_language = st.selectbox(
        "Select your preferred language / भाषा चुनें / તમારી પસંદગીની ભાષા પસંદ કરો",
        ['en', 'hi', 'gu'],
        format_func=get_language_name
    )

    # Multilingual welcome message
    welcome_messages = {
        'en': "Ask me anything about agriculture, crop production, or weather!",
        'hi': "कृषि, फसल उत्पादन, या मौसम के बारे में कुछ भी पूछें!",
        'gu': "ખેતી, પાક ઉત્પાદન અથવા હવામાન વિશે કંઈપણ પૂછો!"
    }
    st.write(welcome_messages[selected_language])

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # User input placeholder text in multiple languages
    placeholder_text = {
        'en': "Type your question here...",
        'hi': "अपना प्रश्न यहां टाइप करें...",
        'gu': "તમારો પ્રશ્ન અહીં ટાઈપ કરો..."
    }

    # User input
    user_input = st.text_input(
        "💭",
        placeholder=placeholder_text[selected_language]
    )

    if user_input:
        # Detect language of the input
        input_language = detect_language(user_input)
        
        # Check if the input is a greeting
        if is_greeting(user_input):
            greetings = {
                'en': ["Hello! How can I assist you with agriculture today?", "Hi there! What's your agriculture-related question?"],
                'hi': ["नमस्ते! आज मैं आपकी कृषि संबंधी मदद कैसे कर सकता हूँ?", "हाय! आपका कृषि संबंधी प्रश्न क्या है?"],
                'gu': ["નમસ્તે! આજે હું તમારી ખેતી સંબંધિત મદદ કેવી રીતે કરી શકું?", "હાય! તમારો ખેતી સંબંધિત પ્રશ્ન શું છે?"]
            }
            import random
            response = random.choice(greetings[input_language])
        else:
            # Check if the question is agriculture-related
            if not is_agriculture_related(user_input):
                error_messages = {
                    'en': "Please ask a question related to agriculture, farming, crops, weather, soil, fertilizers, or farmers.",
                    'hi': "कृपया कृषि, खेती, फसल, मौसम, मिट्टी, उर्वरक, या किसानों से संबंधित प्रश्न पूछें।",
                    'gu': "કૃપા કરીને ખેતી, પાક, હવામાન, માટી, ખાતર અથવા ખેડૂતો સંબંધિત પ્રશ્ન પૂછો."
                }
                st.error(error_messages[selected_language])
                return
            else:
                # Generate response
                response = generate_response(user_input, input_language)
        
        # Add to chat history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

    # Display chat history with localized labels
    chat_labels = {
        'en': {'user': 'You', 'bot': 'Bot'},
        'hi': {'user': 'आप', 'bot': 'बॉट'},
        'gu': {'user': 'તમે', 'bot': 'બોટ'}
    }

    for role, message in st.session_state.chat_history:
        if role == "user":
            st.write(f"👤 {chat_labels[selected_language]['user']}: {message}")
        else:
            st.write(f"🤖 {chat_labels[selected_language]['bot']}: {message}")

if __name__ == "__main__":
    main()
