from glob import glob
import os
import shutil

from credentials import service_account_json_path
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_json_path
translate_client = translate.Client()

paths = glob("../data/svg/*.svg")
for the_path in paths:
    arabic_name = os.path.basename(the_path.replace('.svg', ''))
    result = translate_client.translate(arabic_name, target_language='en')
    result = result['translatedText']
    input = arabic_name
    new_name = f"{result} | {input}.svg"

    new_path = os.path.join('../data/svg/svg_translated', new_name)
    print(new_path)
    shutil.copy2(the_path, new_path)
