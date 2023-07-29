import aiohttp
import base64
import json
import sys
import asyncio

class ImageOCR:
    def __init__(self, google_cloud_api_key):
        self.google_cloud_api_key = google_cloud_api_key
    async def do_image_ocr(self, filepath):
        # encode image to base64
        if not self.google_cloud_api_key:
            return "None"
        with open(filepath, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

        # payload
        payload = {
            "requests": [
                {
                    "image": {"content": encoded_image},
                    "features": [{"type": "TEXT_DETECTION"}],
                }
            ]
        }
        header = {
            "Content-Type": "application/json; charset=utf-8",
        }
        url = f"https://vision.googleapis.com/v1/images:annotate?key={self.google_cloud_api_key}"

        # Send the async request
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=header, data=json.dumps(payload)
            ) as response:
                result = await response.json()
                if response.status == 200:
                    full_text_annotation = result.get("responses", [])[0].get(
                        "fullTextAnnotation"
                    )
                    if full_text_annotation:
                        extracted_text = full_text_annotation.get("text")
                        return extracted_text
                    else:
                        return ""
                else:
                    raise Exception(
                        f"Google Cloud Vision API returned an error. Status code: {response.status}, Error: {result}"
                    )

if __name__ == "__main__":
    with open("token.json") as token_file:
        google_cloud_api_key = json.load(token_file)["api_key"]
    image_file_path = sys.argv[1]
    image_ocr = ImageOCR(google_cloud_api_key)
    extracted_text = asyncio.run(image_ocr.do_image_ocr(image_file_path))
    print(extracted_text)