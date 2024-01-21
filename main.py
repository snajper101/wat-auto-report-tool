# --- IMPORTS ---
from settings import get_settings_status, load_settings, save_settings
from userDataClass import UserData, DEFAULT_CLASS_NUMBER, DEFAULT_GROUP_NUMBER
from generateReport import start_report

# --- VARIABLES --
userData = UserData()

# --- MAIN FUNCTION ---
def get_user_data_form():
    name = input( "Podaj swoje imie: " )
    surname = input( "Podaj swoje nazwisko: " )
    userClass = input( "Podaj numer kierunku: " )
    userClass = DEFAULT_CLASS_NUMBER if userClass == "" else userClass  
    group = input( "Podaj swoja grupe: " )
    group = DEFAULT_GROUP_NUMBER if group == "" else group  
    openAISecret = input( "Podaj klucz API OpenAI: " )
    userData.set( name, surname, userClass, group, openAISecret )
    save_settings( userData )
    return 

def initialise() -> None:
    if not get_settings_status():
        get_user_data_form()
    if not ( userData := load_settings() ):
        get_user_data_form()
    start_report( userData )
    return

initialise() 