# Avia-Hack-2022-RealityX-ML

Micro service to predict results from `csv` file.

### Content

0. [Download project](#results)
1. [Download project](#download)
2. [Install requirements](#deps)
3. [Run API service](#run)
4. [Available models](#models)
5. [ML/DS developing](#mlds)

### ML/DS results <a name="results"></a>

See `CHECKME.ipynb` file.

### Download <a name="download"></a>

```
git clone https://github.com/AlexGeniusMan/Avia-Hack-2022-RealityX-ML.git avia
cd avia
```

### Install requirements <a name="deps"></a>:

1.  For start API service:
    ```
    pip install -r requirements.txt
    ```
2.  For ML/DS developing:
    ```
    pip install -r dev-requirements.txt
    ```

### Run API service <a name="run"></a>:

Available settings by environment variables (create `.env` file in root dir for run with python):

```
DEBUG: # if want to reload service in developing set 1 else 0. Default is 0.
ROOT_PATH: # string: FastAPI root_path setting for proxy. Default is ''.
```

Run:

```
python run.py
```

or

```
docker compose up --build
```

> API documentation (Swagger UI) is located at http://localhost:8000/docs.
> Don`t use API from browser, may crash it because of huge response size. Instead use Insomnia or Postman

### Available models <a name="models"></a>:

Models available in `/app/models` directory.

### ML/DS developing <a name="mlds"></a>

See `neural.ipynb` file.
