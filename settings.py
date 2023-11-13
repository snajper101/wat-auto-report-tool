import pickle
import constants
from userDataClass import UserData
from os import path

def load_settings():
    try:
        with open(constants.USER_DATA_FILE, "rb") as f:
            userData = pickle.load(f)
            if not isinstance( userData, UserData ):
                return False
            return userData
    except Exception as ex:
        print(f"Error while loading user data. {ex}")
        return False
    
def save_settings( userData ) -> bool:
    try:
        with open(constants.USER_DATA_FILE, "wb") as f:
            pickle.dump(userData, f, protocol=pickle.HIGHEST_PROTOCOL)
        return True
    except Exception as ex:
        print(f"Error while saving user data. {ex}")
        return False

def get_settings_status():
    return path.isfile(f"./{constants.USER_DATA_FILE}")