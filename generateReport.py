import constants
from os import path

def check_word_file():
    return path.isfile( f"/{constants.REPORT_FILE}" )

def edit_word_file():
    pass

def start_report( userData ):
    if not check_word_file():
        print( f"No report file. File should be in program folder with name: {constants.REPORT_FILE}" )
        return
    taskNumber = input( "Podaj numer zadania: " )
    taskTitle = input("Podaj nazwe zadania: " )

    return