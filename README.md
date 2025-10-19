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

______________________________________________

We will start to add our Features 
 1- allow to upload files in our app 
      so need the endpoint : UploadeFile

- build or architecture to make the system easy to maintanince 
    --> separate the logic and route 
    so used MVC (Model - view - controller)
    until now we donot have view Just APIs
   
    --> pydantic settings 
    --> make your app depended on depence in python 


- Now i will start to add the uploadFile Endpoint 
    - validate endpoint when 
    - return json response 
    - save all files in or machine with projectid and make git ignore this files 
___________________________________________________________

Now we finished the endpoint of uploading endpoint 
YAAAAAA

so the next step will validate the file 
pydantic response to validate the schema of project 


