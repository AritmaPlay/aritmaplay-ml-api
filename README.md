# AritmaPlay - Handwriting Digit Recognizer Model REST API

## Installation

### Requirement
- Docker
- Curl / REST API Client (Postman)

### Installation Step
1. Clone the repository to your local device.
```bash
git clone https://github.com/AritmaPlay/aritmaplay-ml-api.git
```
```bash
cd aritmaplay-ml-api
```

2. Build the docker image.
```bash
docker build -t ml-api .
```
3. Run the docker container.
```bash
docker run -d --name api-container -p 8080:8080 ml-api
```
## Api Endpoints
### GET Health
Endpoint to check the status of the Rest API app.
#### Endpoint
```/health```
#### Response
```bash
curl -X GET http://localhost:8080/health
```
```json
{
    "status":"healthy"
}
```

### POST Predict
Endpoint to predict/recognize the digit 0-9 of a handwriting image. </br>
Makesure your image spesification is:
1. Size 48x48 pixels.
2. JPEG/JPG format.
#### Endpoint
```/predict```
#### Response
```bash
curl -X POST -F "image=@[PATH/TO/YOUR/IMAGE.JPG]" http://localhost:8080/predict
```
```json
{
    "data": {
        "digit": 3,
        "probabilities": [
            2.76264107425933e-20,
            2.0730851450904046e-31,
            3.7685306264467755e-11,
            1.0,
            7.193383360587104e-19,
            5.878114401475232e-12,
            1.1354770578376593e-14,
            7.980349020497712e-12,
            7.5117299533356e-12,
            7.348617374336452e-12
        ]
    },
    "message": "Image recognized successfully",
    "response_code": 200,
    "success": true
}
```