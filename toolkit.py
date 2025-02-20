import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv
import csv
import markdown


class kit():
    def __init__(self) -> None:
        load_dotenv()
        api_key = os.environ.get("Key")
        genai.configure(api_key=api_key)
        self.modle = genai.GenerativeModel(model_name="gemini-1.5-flash")
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.join(self.current_dir,'words.csv')
        # self.temp_file = os.path.join(self.current_dir,'temp.csv')
        if os.path.exists(self.path) == False:
            create_file_path = self.path
            with open (create_file_path,'w',newline='') as source:
                writer = csv.DictWriter(source,fieldnames = ['word','explain'])
                writer.writeheader()
        # if os.path.exists(self.temp_file) == False:
        #     with open (self.temp_file,'w',newline='') as source:
        #             writer = csv.DictWriter(source,fieldnames = ['word','explain'])
        #             writer.writeheader()    
                
    def prompting_sequence(self,Qnumber:int):
        pass
    def add_and_show_word(self,word:str):
        [is_exist,explanation] = self.word_in_DB(word)
        if is_exist:
            print('give ex')

            return explanation
                # mark_text = explanation
                # html = markdown.markdown(mark_text)
                # return html
            
        else:
            prompt = f'can you explain the meaning of {word},you can add more markdowns to emphasize the words'
            response = self.modle.generate_content(prompt)
            result = response.text
            with open(self.path,'a',newline='') as file:
                field_name = ['word','explain']
                writer = csv.DictWriter(file,fieldnames=field_name)
                # writer.writeheader()
                writer.writerow({'word':word,'explain':result})
                # print(self.row_counter())
            print("written else")
            return result     
               
    def word_in_DB(self,word_to_be_check:str):
        with open (self.path,newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['word'] == word_to_be_check :
                    return [True,row['explain']]
        return [False,None]

    
    def row_counter(self) -> int:
        row_num = 0
        with open(self.path,'r',newline='') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                row_num += 1
        return row_num
    














# class Client():
#     def __init__(self) -> None:
#         pass
#     def show_word_explanation(self,file_path) ->None:
#         pass