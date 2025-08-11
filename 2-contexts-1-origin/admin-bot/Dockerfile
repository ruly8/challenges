FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY admin-bot.py .
COPY templates/ ./templates/

USER root
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install selenium Flask

USER seluser

CMD ["python3", "admin-bot.py"]

