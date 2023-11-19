import json
from openAI_call import openAI_class
import textReader
from openAI_call import api_Call
import os

def main():
    ruta_pdf_files = r'C:\Users\cristianbenalcazar\PycharmProjects\OCR\Purebas IA\Nombramientos'
    ruta_answer = r'C:\Users\cristianbenalcazar\PycharmProjects\OCR\Answer_file\List_dictionary.json'

    dict_resp = {'beneficiario': [], 'compania': [], 'cargo': [], 'vigencia': [], 'fecha': [], 'RLJE': []}
    list_objects = []
    for pdf_name in os.listdir(ruta_pdf_files):
        pdf_name_path = os.path.join(ruta_pdf_files,pdf_name)
        text_pages = textReader.text_recognize(pdf_name_path)
        dict_resp = output_info(api_Call(text_pages), dict_resp)

    with open(ruta_answer, 'w') as archivo:
        json.dump(dict_resp,archivo)



def output_info(objectAPI,dict_resp):
    dict_resp['beneficiario'].append(objectAPI.beneficiario)
    dict_resp['compania'].append(objectAPI.compania)
    dict_resp['cargo'].append(objectAPI.cargo)
    dict_resp['vigencia'].append(objectAPI.vigencia)
    dict_resp['fecha'].append(objectAPI.fecha)
    dict_resp['RLJE'].append(objectAPI.RLJE)
    print(dict_resp)
    return dict_resp






if __name__ == '__main__':
    main()


