FROM python:3.9
WORKDIR code
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
