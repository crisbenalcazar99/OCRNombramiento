# Importacion de Librerias
import openai
import json
import csv


class openAI_class():

    def __init__(self):
        self._RLJE = None
        self._fecha = None
        self._vigencia = None
        self._compania = None
        self._cargo = None
        self._beneficiario = None

    @property
    def beneficiario(self):
        return self._beneficiario

    @property
    def compania(self):
        return self._compania

    @property
    def cargo(self):
        return self._cargo

    @property
    def vigencia(self):
        return self._vigencia

    @property
    def fecha(self):
        return self._fecha

    @property
    def RLJE(self):
        return self._RLJE

    @beneficiario.setter
    def beneficiario(self, beneficiario):
        self._beneficiario = beneficiario

    @compania.setter
    def compania(self, compania):
        self._compania = compania

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @vigencia.setter
    def vigencia(self, vigencia):
        self._vigencia = vigencia

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @RLJE.setter
    def RLJE(self, RLJE):
        self._RLJE = RLJE


def api_Call(text_pages):
    # Se define la key de OPEN AI y el Prompt principal
    openai.api_key = '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'
    # mensaje = "Tomando en cuenta que el siguiente texto corresponde al Nombramiento de representante Legal de una empresa, responde: \n¿Quien es el beneficiario del nombramiento?,  ¿Cual es el nombre o razon social de la compania?. ¿Que nombramiento se le otorga?,  ¿Cuantos años tiene de vigencia el nombramiento?,  ¿Cual es la fecha del nombramiento? TIene la representacion legal de la compania?\npresenta esta información separada por comas, para indicar un periodo de tiempo solo indica el digito y omite la palabra años"
    mensaje = "Genera un archivo CVS con la siguiente informacion extraida del texto y omite la palabra 'años': \nbeneficiario: [beneficiario]\n compania: [nombre compania]\n, cargo:[vargo]\n, vigencia: [Vigencia]\n, fecha:[fecha]\n, RLJE : [¿El beneficiario del nombramiento tiene la representación legal, judicial y extrajudicial según el contenido del documento responde unicamnete si/no?]\n completa la informacion faltante sin comillas en los espacios entre llaves y la salida debe ser en formato JSON donde la pregunta es la clave y la respuesta el valor"

    prompt = ''
    for text_page in text_pages:
        prompt = prompt + text_page
        print(text_page)

    # Se envia el mensaje y el prompt por el api de chat gpt

    return_openAI = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": mensaje},
                  {"role": "user", "content": prompt},
                  {"role": "assistant", "content": "I am doing well"}],

        temperature=0.1
    )

    with open(r"C:\Users\cristianbenalcazar\PycharmProjects\OCR\PruebaPY\RespuestaAI.json", 'w') as archivo_json:
        json.dump(return_openAI, archivo_json)

    specified_answer = return_openAI['choices'][0]['message']['content']
    specified_answer = json.loads(specified_answer)
    print(type(specified_answer))

    clase_openAI = openAI_class
    try:
        clase_openAI.beneficiario = specified_answer['beneficiario']
    except KeyError:
        clase_openAI.beneficiario = None
    try:
        clase_openAI.cargo = specified_answer['cargo']
    except KeyError:
        clase_openAI.cargo = None
    try:
        clase_openAI.compania = specified_answer['compania']
    except KeyError:
        clase_openAI.compania = None
    try:
        clase_openAI.fecha = specified_answer['fecha']
    except KeyError:
        clase_openAI.fecha = None
    try:
        clase_openAI.vigencia = specified_answer['vigencia']
    except KeyError:
        clase_openAI.vigencia = None
    try:
        clase_openAI.RLJE = specified_answer['RLJE']
    except KeyError:
        clase_openAI.RLJE = None

    return clase_openAI

