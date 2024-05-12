# Your Python version
FROM python:3.9

# Web port of the application
EXPOSE 5000

# Install your application
WORKDIR /my_app
COPY . /my_app
RUN pip install -r requirements.txt

# Start up command
CMD python soccer_utils/main.py -P 5000 -H 0.0.0.0 --debug