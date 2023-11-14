import constants
import os
from os import path
from docx import Document
import shutil

def check_word_file():
    return path.isfile( f"./{constants.REPORT_FILE}" )

def clone_word_file( src, output ):
    if path.isfile( output ):
        os.remove( output )
    return shutil.copy( src, output )


def edit_word_file(file, param, value):
    document = Document( file )
    match param:
        case "author":
            table = document.tables[0]
            author_row = table.rows[1]
            author_cell = author_row.cells[1]
            for paragraph in author_cell.paragraphs:
                if paragraph.text == f"<{param}>":
                    paragraph.text = value 
        case "task_number":
            table = document.tables[0]
            author_row = table.rows[0]
            author_cell = author_row.cells[3]
            for paragraph in author_cell.paragraphs:
                if paragraph.text == f"<{param}>":
                    paragraph.text = value 
        case "task_title":
            table = document.tables[0]
            author_row = table.rows[2]
            author_cell = author_row.cells[1]
            for paragraph in author_cell.paragraphs:
                if paragraph.text == f"<{param}>":
                    paragraph.text = value 
        case _:
            for paragraph in document.paragraphs:
                if paragraph.text == f"<{param}>":
                    paragraph.text = value
                print(paragraph.text)
            pass
    document.save(file)

def start_report( userData ):
    if not check_word_file():
        print( f"No report file. File should be in program folder with name: {constants.REPORT_FILE }" )
        return
    taskNumber = input( "Podaj numer zadania: " )
    taskTitle = input("Podaj nazwe zadania: " )

    outputFile = clone_word_file( f"./{constants.REPORT_FILE}", outputName := constants.OUTPUT_FILE( taskNumber ) )

    edit_word_file( outputName, "author", f"{userData.name} {userData.surname}" )
    edit_word_file( outputName, "group_name", userData.groupNumber )
    edit_word_file( outputName, "task_number", taskNumber )
    edit_word_file( outputName, "task_title", taskTitle )

    realisationMethod = input( "Podaj metodę realizacji: ")
    edit_word_file( outputName, "realisation_method", realisationMethod )

    entryData = input( "Podaj dane wejsciowe zadania: ")
    edit_word_file( outputName, "entry_data", entryData )

    exitData = input( "Podaj dane wyjściowe zadania: ")
    edit_word_file( outputName, "exit_data", exitData )

    return