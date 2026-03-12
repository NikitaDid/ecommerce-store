#Version pf Python
FROM python:latest

#Your work directory
WORKDIR /app

#Uprading pip to the last version
RUN pip install --upgrade pip

#Copying requirements file with all instancies
COPY requirements.txt .

#Installing whole requirements file
RUN pip install -r requirements.txt

#Copying the whole project
COPY . .

EXPOSE 8000

#Running terminal command to start a server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=online_store_project.settings"]
