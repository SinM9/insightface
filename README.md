## Demo [tf-insightface](https://github.com/AIInAi/tf-insightface)

Download pre-trained [frozen model](https://drive.google.com/open?id=1Iw2Ckz_BnHZUi78USlaFreZXylJj7hnP) and put it under [`pretrained` folder](https://github.com/SinM9/insightface/tree/main/pretrained)

### Run with Docker
##### Requirements
* Docker

Build image

```bash
docker build -t insightface .
```

Run image

```bash
docker run --name insightface_run insightface
```

```bash
docker cp insightface_run:/tests .
```

Remove image

```bash
docker rm insightface_run
```

```bash
docker image rm insightface
```


### Run with pipenv
##### Requirements
* Python
* pipenv

Install

```bash
pipenv shell --python 3.8
```

```bash
pip install -r requirements.txt
```

Run
```bash
python test.py
```


