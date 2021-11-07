#### CancerHealthcare - A website dedicated to cancer patients in Bangladesh

# Contribute :
- Fork the repo.
- clone it.
- open the folder.
# For windows:
- create a virtual environment
```
py -m venv venv
```
- activate the virtual environment
```
cd venv/Scripts
.\activate
```
- install dependencies
```
pip install -r requirements.txt
```
- make migrations (optional for the initial setup)
- run the server
```
cd cancercare
py manage.py runserver
```
# For linux:
- create a virtual environment
```
python3 -m venv venv
```
- source the virtual environment
```
source venv/bin/activate
```
- install dependencies:
```
pip install -r requirements.txt
```
- run the server:
```
cd cancercare
python manage.py runserver
```