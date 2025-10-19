from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResponseSignal
import os

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir

    



# function will take the file and save this file in our machine and return the path_file 
# and save the path of project to allow BaseController or DataController used it 
# used OS library to find the dir name of the current name 