import re 

def remove_chat_metadata(chat_export_file): 
    """Defining regular expressions and removing metadata"""
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)" #Pattern for 09/16/22: 22:35 
    dash_whitespace = r"\s-\s" #for "-" in "09/16/22: 22:35 - "
    username = r"([\w\s]+)" #for e.g., "User1"
    metadata_end = r":\s" #for ": " in "User1: "
    single_pattern = date_time + dash_whitespace + username + metadata_end
   
    """Reading the file and removing metadata by replacing them with empty strings"""
    with open(chat_export_file, "r" ) as corpus_file:
        content = corpus_file.read()
        cleaned_corpus = re.sub(single_pattern, "", content)
        return tuple(cleaned_corpus.split("\n")) 
    
#Inspecting the output of the function 
if __name__ == "__main__":
    chat_file_path = "/Users/fatimaisaeva/Downloads/materials-chatterbot-2/source_code_step_3/chat.txt"
    print(remove_chat_metadata(chat_file_path))

#Additional function to remove complete lines (metadata) at the very start of the file
def remove_non_message_text(export_text_lines):
    """Removes the first introduction line and the final extra lines of a WhatsApp chat """
    messages = export_text_lines[1: -1]

    filter_out_msgs = ("<Media omitted>",) #Excluding a string from the data
    return tuple((msg for msg in messages if msg not in filter_out_msgs)) #including messages that are not filtered out


    

#Creating a generalized function for further importing it as a module 
import re
def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus