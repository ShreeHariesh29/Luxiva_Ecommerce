FROM python:3.13-slim

WORKDIR /app

COPY main.pyc connector.pyc requirements.txt decrypt_and_start.sh ./
RUN chmod +x decrypt_and_start.sh
RUN pip install --no-cache-dir -r requirements.txt

CMD ["./decrypt_and_start.sh"]
