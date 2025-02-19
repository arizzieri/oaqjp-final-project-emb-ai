import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=headers)
    
    if response.status_code == 400:
        formatted_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_response

    json_obj = json.loads(response.text)
    formatted_response = json_obj["emotionPredictions"][0]["emotion"]
    formatted_response['dominant_emotion'] = max(formatted_response, key=formatted_response.get)
    return formatted_response
