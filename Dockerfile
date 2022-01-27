FROM python:3.9
COPY . code
RUN python3 -m pip install --upgrade pip
WORKDIR code
RUN pip3 install -r requirements.txt
