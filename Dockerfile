FROM python:3.9
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
WORKDIR "/code/ui_autotests"