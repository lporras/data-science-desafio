import json
import requests
from os import environ

def request(requested_url):
    payload = ""
    headers = {
        'cache-control': "no-cache",
        'app_id': "e13c7e6b",
        'app_key': environ['OXFORD_API_KEY']
    }
    response = requests.request("GET", requested_url, data=payload, headers=headers)
    return json.loads(response.text)

data = request("https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/{}".format("hedgehog"))

print(data)
'''
{
    'id':'hedgehog',
    'metadata':{
        'operation':'retrieve',
        'provider':'Oxford University Press',
        'schema':'RetrieveEntry'
    },
    'results':[
        {
            'id':'hedgehog',
            'language':'en-gb',
            'lexicalEntries':[
                {
                    'entries':[
                        {
                            'etymologies':[
                                'late Middle English: from hedge(from its habitat) + hog (from its piglike snout)'
                            ],
                            'senses':[
                                {
                                    'definitions':[
                                        'a small nocturnal Old World mammal with a spiny coat and short legs, able to roll itself into a ball for defence.'
                                    ],
                                    'domains':[
                                        {
                                            'id':'mammal',
                                            'text':'Mammal'
                                        }
                                    ],
                                    'id':'m_en_gbus0459110.006',
                                    'notes':[
                                        {
                                            'text':'Family Erinaceidae: four genera and several species, including the common Erinaceus europaeus (which is predominantly insectivorous) of western and northern Europe',
                                            'type':'technicalNote'
                                        }
                                    ],
                                    'shortDefinitions':[
                                        'nocturnal insectivorous Old World mammal with spiny coat and short legs'
                                    ],
                                    'subsenses':[
                                        {
                                            'definitions':[
                                                'a porcupine.'
                                            ],
                                            'domains':[
                                                {
                                                    'id':'zoology',
                                                    'text':'Zoology'
                                                }
                                            ],
                                            'id':'m_en_gbus0459110.012',
                                            'regions':[
                                                {
                                                    'id':'north_american',
                                                    'text':'North_American'
                                                }
                                            ],
                                            'shortDefinitions':[
                                                'porcupine'
                                            ]
                                        },
                                        {
                                            'definitions':[
                                                'used in names of plants or fruits resembling a hedgehog in having spines, e.g. hedgehog cactus, hedgehog holly.'
                                            ],
                                            'domains':[
                                                {
                                                    'id':'plant',
                                                    'text':'Plant'
                                                }
                                            ],
                                            'id':'m_en_gbus0459110.013',
                                            'shortDefinitions':[
                                                'used in names of plants or fruits resembling hedgehog in having spines'
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    'language':'en-gb',
                    'lexicalCategory':{
                        'id':'noun',
                        'text':'Noun'
                    },
                    'pronunciations':[
                        {
                            'audioFile':'http://audio.oxforddictionaries.com/en/mp3/hedgehog_gb_1.mp3',
                            'dialects':[
                                'British English'
                            ],
                            'phoneticNotation':'IPA',
                            'phoneticSpelling':'ˈhɛdʒ(h)ɒɡ'
                        }
                    ],
                    'text':'hedgehog'
                }
            ],
            'type':'headword',
            'word':'hedgehog'
        }
    ],
    'word':'hedgehog'
}
'''

print(data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
# ['a small nocturnal Old World mammal with a spiny coat and short legs, able to roll itself into a ball for defence.']

# para usar una variable de entorno
# export a=5
# from os import environ
# environ["a"]
# '5'