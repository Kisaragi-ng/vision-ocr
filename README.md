# OCR via Google Cloud Vision

## install requirements

```bash
pip3 install -r requirements.txt
```

## setup api_key in token.json

Make sure `Cloud Vision API` is enabled in your google console, and create API key by accessing *APIs & Services -> Credentials -> Create Credentials -> API Key*.

```json
{
  "api_key": "YOUR_API_KEY"
 }
```

## execute script

```bash
python3 ./ocr.py /path/to/image.png
```
![result](https://i.ibb.co/xzT7VdZ/result.png)

---

Credits: LiNa, Aegis, Nivi