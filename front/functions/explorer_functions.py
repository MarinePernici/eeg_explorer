import os
import re
import requests

from dotenv import load_dotenv

load_dotenv()


def translate_sentence(sentence, target_language, api_key):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": api_key,
        "text": sentence,
        "target_lang": target_language
    }
    response = requests.post(url, data=data)

    translated_text = response.json()["translations"][0]["text"]
    detected_language = response.json()["translations"][0]["detected_source_language"].upper()

    return translated_text, detected_language


def check_keywords(text):
    # Expressions régulières pour les différentes catégories de mots
    data_manipulation_regex = r"(?i)\b(creat|add|insert|delet|remov|drop|updat|modif|chang|alter|truncat|merg)"
    transaction_control_regex = r"(?i)\b(commit|rollback|savepoint)"
    structure_manipulation_regex = r"(?i)\b(create\s+(index|table|view)|drop\s+(index|table|view)|renam)"
    access_control_regex = r"(?i)\b(grant|revok|privileg)"
    specific_sql_commands_regex = r"(?i)\b(lock|unlock|execut|call|set)"

    # Vérifier si un des mots clés est présent dans la phrase traduite
    is_safe = not any(re.search(regex, text) for regex in [
        data_manipulation_regex,
        transaction_control_regex,
        structure_manipulation_regex,
        access_control_regex,
        specific_sql_commands_regex
    ])

    return is_safe


def is_query_safe(query):
    try:
        translated_query, source_language = translate_sentence(
            query,
            "EN",
            os.environ.get("DEEPL_API_KEY")
        )
        print(translated_query, '\n' + source_language)
    except Exception as e:
        print(e)
        return False, "Une erreur s'est produite."

    # Vérifier si un des mots clés est présent dans la phrase traduite
    is_safe = check_keywords(translated_query)

    # Message à retourner
    message = "Authorised request" if is_safe else "Unauthorised request"
    print(message)
    # Traduire le message dans la langue d'origine
    if source_language != "EN":
        message = translate_sentence(
            message,
            source_language,
            os.environ.get("DEEPL_API_KEY")
        )[0]
    return is_safe, message
