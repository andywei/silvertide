FROM python:3
ADD run.py /
RUN pip3 install -r requirements.txt
CMD [ "python", "./run.py" ]