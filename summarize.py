from langchain import HuggingFacePipeline
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate,  LLMChain
from langchain.chat_models import ChatOpenAI
import openai
import re
import pickle

openai.api_key = "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"
model_name = "gpt-3.5-turbo"


with open("shared_variable.pickle", "rb") as f: 
    shared_variable = pickle.load(f) 
 

country = shared_variable["country"]
section = shared_variable["section"]


#Kenya
loader =  PyPDFLoader("./data/Kenya.pdf")
pages = loader.load_and_split()

#split into sections
part_1 = pages[5].page_content + pages[6].page_content + pages[7].page_content + pages[8].page_content + pages[9].page_content
part_2 =  pages[9].page_content + pages[10].page_content + pages[11].page_content + pages[12].page_content + pages[13].page_content + pages[14].page_content
part_3 = pages[14].page_content + pages[15].page_content + pages[16].page_content + pages[17].page_content
part_4 = pages[17].page_content + pages[18].page_content + pages[19].page_content + pages[20].page_content + pages[21].page_content + pages[22].page_content + pages[23].page_content + pages[24].page_content + pages[25].page_content + pages[26].page_content + pages[27].page_content + pages[28].page_content + pages[29].page_content + pages[30].page_content
part_5 = pages[30].page_content + pages[31].page_content
part_6 = pages[31].page_content + pages[32].page_content + pages[33].page_content
part_7 = pages[33].page_content + pages[34].page_content
part_8 = pages[34].page_content + pages[35].page_content +  pages[36].page_content + pages[37].page_content + pages[38].page_content +  pages[39].page_content
part_9 = pages[39].page_content + pages[40].page_content
part_10 = pages[40].page_content + pages[41].page_content
part_11 = pages[41].page_content + pages[42].page_content + pages[43].page_content

#Fucntion to select different parts
def extract_part(part):
  pattern = r"PART .*?(?=PART )"
  match = re.search(pattern, part, flags=re.DOTALL)
  return match.group()

def extract_part_11(part):
  pattern = r"PART .*?(?=amendments.)"
  match = re.search(pattern, part, flags=re.DOTALL)
  return match.group()

part_1 = extract_part(part_1)
part_2 = extract_part(part_2)
part_3 = extract_part(part_3)
part_4 = extract_part(part_4)
part_5 = extract_part(part_5)
part_6 = extract_part(part_6)
part_7 = extract_part(part_7)
part_8 = extract_part(part_8)
part_9 = extract_part(part_9)
part_10 = extract_part(part_10)
part_11 = extract_part_11(part_11)

kenya = {}
for i in range(1, 12):
    kenya['part_' + str(i)] = globals()['part_' + str(i)]

# Full kenyan Document
ke_full_doc = part_1 + part_2 + part_3 + part_4 + part_5 + part_6 + part_7 + part_8 + part_9 + part_10 + part_11

# Rwanda
loader =  PyPDFLoader("./data/Rwanda.pdf")
pages = loader.load_and_split()

chapter_1 = pages[5].page_content + pages[6].page_content + pages[7].page_content + pages[8].page_content + pages[9].page_content + pages[10].page_content
chapter_2 = pages[11].page_content + pages[12].page_content + pages[13].page_content + pages[14].page_content + pages[15].page_content + pages[16].page_content + pages[17].page_content + pages[18].page_content + pages[19].page_content + pages[20].page_content
chapter_3 = pages[21].page_content + pages[22].page_content + pages[23].page_content
chapter_4 = pages[24].page_content + pages[25].page_content + pages[26].page_content + pages[27].page_content + pages[28].page_content
chapter_5 = pages[29].page_content + pages[30].page_content + pages[31].page_content + pages[32].page_content + pages[33].page_content + pages[34].page_content + pages[35].page_content + pages[36].page_content
chapter_6 = pages[37].page_content + pages[38].page_content + pages[39].page_content
chapter_7 = pages[40].page_content + pages[41].page_content + pages[42].page_content + pages[43].page_content + pages[44].page_content + pages[45].page_content
chapter_8 = pages[46].page_content + pages[47].page_content
chapter_9 = pages[48].page_content + pages[49].page_content + pages[50].page_content
chapter_10 = pages[51].page_content

rw_full_doc = chapter_1 + chapter_2 + chapter_3 + chapter_4 + chapter_5 + chapter_6 + chapter_7 + chapter_8 + chapter_9 + chapter_10

rwanda = {}
for i in range(1, 11):
    rwanda['chapter_' + str(i)] = globals()['chapter_' + str(i)]

# Uganda

loader =  PyPDFLoader("./data/Uganda.pdf")
pages = loader.load_and_split()

ug_part_1 = pages[4].page_content + pages[5].page_content + pages[6].page_content + pages[7].page_content
ug_part_2 =  pages[8].page_content + pages[9].page_content + pages[10].page_content
ug_part_3 = pages[10].page_content + pages[11].page_content + pages[12].page_content + pages[13].page_content + pages[14].page_content+ pages[15].page_content+ pages[16].page_content+ pages[17].page_content+ pages[18].page_content+ pages[19].page_content
ug_part_4 = pages[19].page_content + pages[20].page_content + pages[21].page_content
ug_part_5 = pages[21].page_content + pages[22].page_content + pages[23].page_content + pages[24].page_content + pages[25].page_content + pages[26].page_content
ug_part_6 = pages[26].page_content + pages[27].page_content
ug_part_7 = pages[27].page_content + pages[28].page_content
ug_part_8 = pages[28].page_content + pages[29].page_content

ug_part_1 = ug_part_1[610:]
ug_part_2 = extract_part(ug_part_2)
ug_part_3 = extract_part(ug_part_3)
ug_part_4 = extract_part(ug_part_4)
ug_part_5 = extract_part(ug_part_5)
ug_part_6 = extract_part(ug_part_6)
ug_part_7 = extract_part(ug_part_7)
ug_part_8 = ug_part_8[200:]

uganda = {}
for i in range(1, 9):
    uganda['ug_part_' + str(i)] = globals()['ug_part_' + str(i)]

# Uganda full doc
ug_full_doc = ug_part_1 + ug_part_2 + ug_part_3 + ug_part_4 + ug_part_5 + ug_part_6 + ug_part_7 + ug_part_8


def split_text_into_chunks(text, chunk_size):
    """Split the input text into chunks of a given size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Preprocessing
def preprocess(country,section):
  if country == "Kenya":
    if section == None:
      Text = ke_full_doc
    else:
        Text = kenya[f"part_{section}"]

  elif country == "Rwanda":
    if section == None:
      Text = rw_full_doc
    else:
        Text = rwanda[f"chapter_{section}"]


  elif country == "Uganda":
    if section == None:
      Text = ug_full_doc
    else:
        Text = uganda[f"ug_part_{section}"]


  if len(Text) > 4000:
    chunk_size = 3000
    Text = split_text_into_chunks(Text, chunk_size)

  return Text

Text = preprocess(country,section)

# openAI 
llm = ChatOpenAI(temperature=0, openai_api_key=openai.api_key, model_name=model_name)

# Prpmpt template
template = """
              The text delimited by triple backquotes is an exerpt from the Data protection act of {country}
              Write a concise summary of the following text delimited by triple backquotes.
              Return your response in paragraph which covers the key points of the text.
              ```{text}```
              PARAGRAPH SUMMARY:
           """

prompt = PromptTemplate(template=template, input_variables=["country","text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

# function to summarize
def summarize():
    if type(Text) == str:
        summary = llm_chain.run({"country":country, "text": Text})
    else:
        summary = ""
        for i in range(len(Text)):
            summary = summary + llm_chain.run({"country":country, "text": Text[i]})
    return summary
