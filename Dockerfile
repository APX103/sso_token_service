FROM python:3.10-slim

ADD . /workspace
WORKDIR /workspace

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD [ "python", "main.py" ]
