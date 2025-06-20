# Rag

## Requirments 
**python,** we will use Python 3.12.7 

**Create virtual environment** 

```bash
python -m venv venv
```

to **activate** the virtual environment in Vs code terminal :
```bash
venv/Scripts/activate 
```
Add **Requirments.txt** file to add all the packages and libraries with them versions.
Just create txt file.

and if you cloned the repo you need to run this command in your terminal to install all packages:

```bash
pip install -r requirments.txt
```


## Run the FastAPI App
To run the FastAPI application using uvicorn, use the following command:

 ```bash
 uvicorn main:app --reload --host 127.0.0.1 --port 8081 ``` 

