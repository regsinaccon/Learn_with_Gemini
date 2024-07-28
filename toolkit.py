import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv
import csv
import markdown


class evaluation():
    def __init__(self) -> None:
        load_dotenv()
        api_key = os.environ.get("Key")
        genai.configure(api_key=api_key)
        self.modle = genai.GenerativeModel(model_name="gemini-1.5-flash")
        self.path = f"words.csv"
        # self.DisplayPath = 'C:\\Users\\CHH\\Desktop\\LearnwithGe\\Gecore\\display.html"
        if os.path.exists(self.path) == False:
            create_file_path = self.path
            with open (create_file_path,'w',newline='') as source:
                writer = csv.DictWriter(source,fieldnames = ['word','explain'])
                writer.writeheader()
                pass
    def prompting_sequence(self,Qnumber:int):
        pass
    def add_word(self,word:str):
        [is_exist,explanation] = self.word_in_DB(word)
        if is_exist:
            # print(explanation)
            mark_text = explanation
            html = markdown.markdown(mark_text)
            # print(type(html))
            with open ('C:\\Users\\CHH\\Desktop\\LearnwithGe\\Gecore\\display.html','r') as writer:
                writer.write(html)
            self.show_word_explanation()            
        else:
            prompt = f'what is the meaning of {word}'
            response = self.modle.generate_content(prompt)
            result = response.text
            with open(self.path,'a',newline='') as file:
                field_name = ['word','explain']
                writer = csv.DictWriter(file,fieldnames=field_name)
                # writer.writeheader()
                writer.writerow({'word':word,'explain':result})
                # print(self.row_counter())
            with open ('C:\\Users\\CHH\\Desktop\\LearnwithGe\\Gecore\\display.html','r') as writer:
                writer.write(result)
            self.show_word_explanation()
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
    def show_word_explanation(self,file_path) ->None:
        os.startfile("C:\\Users\\CHH\\Desktop\\LearnwithGe\\Gecore\\display.html")
