import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name="mlProject"


list_of_files=[
	f"scr/{project_name}/__init__.py",
	f"scr/{project_name}/components/__init__.py",
	f"scr/{project_name}/utils/__init__.py",
	f"scr/{project_name}/utils/common.py",
	f"scr/{project_name}/config/__init__.py",
	f"scr/{project_name}/config/configuration.py",
	f"scr/{project_name}/pipeline/__init__.py",
	f"scr/{project_name}/entity/__init__.py",
	f"scr/{project_name}/entity/config_entity.py",
	f"scr/{project_name}/constants/__init__.py",
	"config/config.yaml",
    	"params.yaml",
    	"schema.yaml",
    	"main.py",
   	"app.py",
   	"requirements.txt",
    	"setup.py",
    	"research/trials.ipynb",
    	"templates/index.html"
]


for filepath in list_of_files:
	filepath = Path(filepath)        
	filedir,filename=os.path.split(filepath)
	if filedir !="":
		os.makedirs(filedir, exist_ok=True)
		logging.info(f"creating directory; {filedir} for the file :{filename}")
		
	if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
		with open(filepath, "w") as f:
			pass
			logging.info(f"creating empty file : {filepath}")
	
	else:
		logging.info(f"{filena,e} is already exists")
		
		
		
