FROM python:3.10.2-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install pip --upgrade

COPY ./backend/requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY ./backend /backend

WORKDIR /backend

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8443"]