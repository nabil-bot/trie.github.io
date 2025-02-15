import re
import pickle
import os
from collections import defaultdict

# with open("banglaWords.pkl", "rb") as f:
#     word_set = pickle.load(f)

# print(f"length: {len(word_set)}")

char_set = ['া', 'ফ', '\u200c', 'ং', 'ঞ', '্', 'ৎ', 'দ', 'ঐ', 'ঔ', 'ৌ', 'ঋ', 'জ', 'ৗ', 'এ', 'ঢ', 'ড়', 'ে', 'স', 'চ', 'প', 'ক', 'ি', 'ঠ', 'ষ', 'ূ', 'ছ', 'ো', 'য', 'ল', 'ই', 'ঝ', 'ঘ', 'থ', 'হ', 'ও', 'ঙ', 'ঈ', 'আ', 'ৰ', 'য়', 'ত', 'ড', 'ঃ', '\u200d', 'ভ', 'গ', 'উ', 'শ', 'ু', 'খ', 'ৈ', 'ঢ়', 'ধ', 'ট', 'ম', 'ঁ', 'র', 'ৃ', 'ণ', 'অ', 'ঊ', 'ব', 'ী', 'ন']

convertion_map = {}

for i in range(len(char_set)):
    convertion_map[char_set[i]] = i

# for word in word_set:
#     if len(word) > 3:
#         dir_path = os.path.join(*(str(convertion_map[char]) for char in word))
#         os.makedirs(dir_path, exist_ok=True)
        
#         file_path = os.path.join(dir_path, 'words.html')
        
#         with open(file_path, 'a', encoding='utf-8') as f:
#             f.write(word + '\n')
        
#         # Update words.txt in each prefix directory
#         for i in range(1, len(word) + 1):
#             prefix_dir = os.path.join(*(str(convertion_map[char]) for char in word[:i]))
#             os.makedirs(prefix_dir, exist_ok=True)
            
#             words_txt_path = os.path.join(prefix_dir, 'words.html')
            
#             with open(words_txt_path, 'a', encoding='utf-8') as f:
#                 f.write(word + '\n')


# unique_chars = set()
# for word in word_set:
#     for char in word:
#         unique_chars.add(char)

# print(unique_chars)
# print(len(unique_chars))

"""
{'দ', 'ৎ', 'ঠ', 'ঢ', 'অ', 'ী', 'ষ', 'শ', 'ণ', 'স', 'ধ', 'ভ', 'ু', 'ছ', 'ড়', 'ি', 'ব', 'ও', 'থ', 'র', 'উ', 'য', '\u200d', 'ঢ়', '\u200c', '়', 'ঋ', 'ৈ', 'ঞ', 'ঊ', 'প', 'ই', 'এ', 'ঐ', 'আ', 'ন', 'ফ', 'খ', 'ো', 'য়', 'ঃ', 'ৃ', 'চ', 'ং', 'ঙ', 'ঁ', 'া', 'ে', 'ক', 'ড', '্', 'ূ', 'ৌ', 'জ', 'ঝ', 'ঈ', 'ট', 'ল', 'ম', 'হ', 'ঘ', 'ঔ', 'গ', 'ত'}

{'া', 'ফ', '\u200c', 'ং', 'ঞ', '্', 'ৎ', 'দ', 'ঐ', 'ঔ', 'ৌ', 'ঋ', 'জ', 'ৗ', 'এ', 'ঢ', 'ড়', 'ে', 'স', 'চ', 'প', 'ক', 'ি', 'ঠ', 'ষ', 'ূ', 'ছ', 'ো', 'য', 'ল', 'ই', 'ঝ', 'ঘ', 'থ', 'হ', 'ও', 'ঙ', 'ঈ', 'আ', 'ৰ', 'য়', 'ত', 'ড', 'ঃ', '\u200d', 'ভ', 'গ', 'উ', 'শ', 'ু', 'খ', 'ৈ', 'ঢ়', 'ধ', 'ট', 'ম', 'ঁ', 'র', 'ৃ', 'ণ', 'অ', 'ঊ', 'ব', 'ী', 'ন'}
{'্', 'ফ', 'হ', '\u200c', 'ৃ', 'ৗ', 'ঠ', 'য', 'ঃ', 'ঞ', 'ঝ', 'ঋ', 'প', 'আ', 'গ', 'ড়', 'ষ', 'ো', 'ং', 'ূ', 'য়', 'ৎ', 'ঔ', 'ঁ', 'চ', 'ণ', 'ৈ', 'ৰ', 'ঙ', 'ভ', 'ঐ', 'ঢ', 'উ', 'ঊ', 'ৌ', 'ছ', 'দ', 'ঢ়', 'ক', 'এ', 'ঈ', 'ড', 'ল', 'া', 'ন', 'ব', 'অ', 'ি', 'ু', 'ও', '\\', 'ধ', 'ট', 'ই', 'n', 'থ', 'ী', 'ত', 'শ', '.', '-', '\u200d', 'ে', 'র', 'খ', 'স', 'জ', 'ম', "'", 'ঘ'}

{'া': 0, 'ফ': 1, '\u200c': 2, 'ং': 3, 'ঞ': 4, '্': 5, 'ৎ': 6, 'দ': 7, 'ঐ': 8, 'ঔ': 9, 'ৌ': 10, 'ঋ': 11, 'জ': 12, 'ৗৗ': 13, 'এ': 14, 'ঢ': 15, 'ড়': 16, 'ে': 17, 'স': 18, 'চ': 19, 'প': 20, 'ক': 21, 'ি': 22, 'ঠ': 23, 'ষ': 24, 'ূ': 25,  'ছ': 26, 'ো': 27, 'য': 28, 'ল': 29, 'ই': 30, 'ঝ': 31, 'ঘ': 32, 'থ': 33, 'হ': 34, 'ও': 35, 'ঙ': 36, 'ঈ': 37, 'আ': 38, 'ৰ': 39, 'য়': 40, 'ত': 41, 'ড': 42, 'ঃ': 43, '\u200d': 44, 'ভ': 45, 'গ': 46, 'উ': 47, 'শ': 48, 'ু': 49, 'খ': 50,  'ৈ': 51, 'ঢ়': 52, 'ধ': 53, 'ট': 54, 'ম': 55, 'ঁ': 56, 'র': 57, 'ৃ': 58, 'ণ': 59, 'অ': 60, 'ঊ': 61, 'ব': 62, 'ী': 63 3, 'ন': 64}

"""

# trie_dict = trieObj.to_dict()
# # trie_items = list(trie_dict.items())[:100]

# print(len(trie_dict))

# with open("banglaWords.pkl", 'rb') as f:
#     words_set, freq = pickle.load(f)

# print(words_set)
# print(len(words_set))


# global secondary_app, db
# from firebase_admin import db, credentials, initialize_app
# import json

# string_data = '{\n  "type": "service_account",\n  "project_id": "konthowordcontributionlocked",\n  "private_key_id": "d4b26d2c5f27e790e703086f8b630d2c98083328",\n  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCXM0HIu/kaCNH8\\nDaYVOPmC8mCobBapE8Y2C5zPRTjm0zE/E/aSiKQbNdxcrI7V1SoJxOKiLu4rm7CU\\npoV3aAT4yCbvzXDw84lZIObObwPk5o0GhwOqnCa7ngA5mALIewcswkkxfA7gZ2Mq\\nGkmCuYfXfrlVH7F/mvifYIwVMaa5VuaB7TK6520JB13pCI9yBSevSRJzwX6otBNO\\nA3gnTxNDtyCr66Oj5tBNDcvhSuA+6c8ZzOiX4iOfzinkVrsGAAKqzOcZ36mr1mTn\\n/cUkTkjc1/Q+OXPAMjiSyIQgmruF9vZ6ZEaVRBq6Ma+OOa1YlwOR/SwpePNnhNyg\\nAmUD038xAgMBAAECggEAAVOazScRDXBsXzjDb0Y7sjFsNa4VGNCqmYjKjGsAD85k\\njTggnrKCNhbn4wxEiI3BO6q1jlS5FDredr9rRlvsRz6CUPJNfl+0ocqPG9qPfy+i\\npx8CIjoSgOzm9Zpm09l4e6UMvVloTAG8Nf9bC8GS9ooPGDcZ+JOkgMl5ESqJWvDr\\nya41SGFq63fU2MGCipydwOARWkAqNO9ic9Qij3DVaPDBvsa21LMcCBqk5e3CPpNl\\nkqL+0gfcxorajD8pUt5yCPrXy8G6q0atZWs5UHY0e9gAv7l11PgFaSTULstloBCH\\nE3D8jpfKzTgHHmnUqFK6K2JFQkZkF5cTMzTFVRo0nQKBgQDP4IxVW1VdDzK+kTHG\\n3G8H+LDwhjRNl+zdfNB/QRQ0CW6RhngMUMDapftFJ0Iw7HJH69eyjJTaT3oaGX5X\\ndZvk6hP458fUSi04l3tilT36jnq4/b69fK+xMkDhqLlJgrTHVnS5Gcuqw2X+viAF\\nNJAUT3q+eWxNMH0UKWmClkEH7wKBgQC6M9tQ3iVLr5cK0wFkWzFXl4I3KBcBYf1a\\nrN/9GF04XymIrQnN5vysirkJXZTZ6gAkxYYmATP+yEHEgYOLLMPhdYjyYX9hLWqL\\nGlypCwxSvI+47K9x9FOcrI4q31uxeSxOUcPsDjyaQTkQVpQPXNf3q2KIKGn7QogZ\\nXh+LqsXK3wKBgCE8N3OWLKm6OlS5hgnTSHUvz6pE6qvVNGuc/wC5eO9w6pqdsyfU\\n6WCL1QaTZkPIKeVR0aScUVguCMmPdeGpzgjlW9gZxpssWNqJbZKvZb9fdEOLXimR\\ne82KyVDK1wTnvtt3+SV2+FcO8omuABSU+MwmgOtfIm+c5wKINHRKbY9FAoGAcB2r\\nT60C3eizVKQqsWerdSdYE6gC+iUrbP6su/OApeG+23n9bkpIGAhLVBVR/EhGn92D\\nYbzVtvKTjyPAtftVUpr3w6HrFfNHtMxBwNNTLzo0e8+f8EiCU9MeozfsORdSEzJu\\neuMzoFnnZywKaJmpvIoogP18mvq7gjLHYcyI3hcCgYBlF7RyB5gfMhpia+386H90\\neyYe83qpKNZ+NArScYkH/vc7C0DCNWqO/klwTccLGfZOCrc882D4I5KqnFZhQc4m\\nj1k8q+j5ExgJZqwu801dqN7FLLjfa9IOPvlSxw4kCJ0aj2Fn1HxqYSN7n79H/CqI\\n2JPsKZqK7RO9JUzSN2Ym5Q==\\n-----END PRIVATE KEY-----\\n",\n  "client_email": "firebase-adminsdk-cqjf5@konthowordcontributionlocked.iam.gserviceaccount.com",\n  "client_id": "117776642190727561857",\n  "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n  "token_uri": "https://oauth2.googleapis.com/token",\n  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cqjf5%40konthowordcontributionlocked.iam.gserviceaccount.com",\n  "universe_domain": "googleapis.com"\n}'
# json_data = json.loads(string_data)
# credContriBution = credentials.Certificate(json_data)
# secondary_app = initialize_app(credContriBution, {"databaseURL": "https://konthowordcontributionlocked-default-rtdb.asia-southeast1.firebasedatabase.app/"}, 'wordContribution')
# ref = db.reference('word', app=secondary_app)


# def emptyDatabase():
#     ref = db.reference('word', app=secondary_app) # word/words
#     words = ref.get()
#     if words:
#         c = 1
#         for key in list(words.keys())[:100]:  # Adjust the chunk size as needed
#             ref.child(key).delete()
#             print(c)
#             c += 1

# for word in words_set:
#     for char in word:


import re
# import requests
import time
filter_dict = {
    "ড়":"ড়",
    "ঢ়":"ঢ়",
    "য়":"য়",
    "ব়":"র"
}

count = 0
BanglaRegEx = "^[‍‌কড়ঢ়য়ব়খগঘঙচছজ‍‌ঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎংঃঁঅআইঈউঊঋএঐওঔািীুূৃেৈোৌ্‍‍]+$"
def add_word(word: str):
    # filter ================================
    for k, v in filter_dict.items():
        word = word.replace(k, v)
    if re.match(BanglaRegEx, word):
        if len(word) > 3:
            dir_path = os.path.join(*(str(convertion_map[char]) for char in word))
            os.makedirs(dir_path, exist_ok=True)
            
            file_path = os.path.join(dir_path, 'words.html')
            
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    words = f.read().splitlines()
            else:
                words = []

            already_exist = False
            if word not in words:
                words.append(word)
                words.sort(key=len)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(words))
            else:
                already_exist = True        

            print(f"file০ path: {file_path}")
            if not already_exist:
                for i in range(1, len(word)):
                    prefix_dir = os.path.join(*(str(convertion_map[char]) for char in word[:i]))
                    os.makedirs(prefix_dir, exist_ok=True)
                    
                    words_txt_path = os.path.join(prefix_dir, 'words.html')
                    
                    if os.path.exists(words_txt_path):
                        with open(words_txt_path, 'r', encoding='utf-8') as f:
                            words = f.read().splitlines()
                    else:
                        words = []

                    if word not in words:
                        words.append(word)
                        words.sort(key=len)

                        with open(words_txt_path, 'w', encoding='utf-8') as f:
                            f.write('\n'.join(words))
                    print(f"file1 path: {words_txt_path}")

            print("Added successfuly")        
    else:
        print(f"Invalid word: {word}")
    # /==================================

# add_word("ফাফরবাজ")




# deleting double words at the end path ==========
# c = 0
# for word in list(word_set):
#     if len(word) > 3:
#         try:
#             dir_path = os.path.join(*(str(convertion_map[char]) for char in word))
#             # os.makedirs(dir_path, exist_ok=True)
#             file_path = os.path.join(dir_path, 'words.html')
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 words = f.read()

#             words = [word for word in words.split('\n') if word]
#             # print(f"words: {words}")    
#             # print(f"words set: {set(words)}")

#             with open(file_path, 'w', encoding='utf-8') as f:
#                 f.write('\n'.join(set(words)))
#             # print("what gonna write: {}".format('\n'.join(set(words))))
#         except Exception as e:
#             print(f"error: {e}")
#             pass  

#         c += 1
#         print(c)


temp = "https://raw.githubusercontent.com/nabil-bot/trie.github.io/refs/heads/main/11/59/words.html"

"""
https://raw.githubusercontent.com/nabil-bot/trie.github.io/refs/heads/main/62/0/3/words.html
"""


# def get_suggestions(prefix):
#     dir_path = (os.path.join(*(str(convertion_map[char]) for char in prefix))).replace('\\', '/')
#     print(f"dir path: {dir_path}")
#     url = "https://raw.githubusercontent.com/nabil-bot/trie.github.io/refs/heads/main/"+dir_path+"/words.html"
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             words = response.text.split('\n')
#             print(f"Suggestions: {words}")
#         else:
#             print(f"Failed to fetch suggestions, status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error fetching suggestions: {e}")


# start_time = time.time()
# get_suggestions("বাং")
# end_time = time.time()

# print(f"Time taken: {end_time - start_time} seconds")


