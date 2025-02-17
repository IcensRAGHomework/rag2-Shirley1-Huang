from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    #print(docs)
    
    text_splitter = CharacterTextSplitter(chunk_overlap  = 0)
    split_text = text_splitter.split_documents(docs)
    
    return split_text[len(split_text)-1]

def hw02_2(q2_pdf):
    pass
