FROM python:slim as builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM python:slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app
EXPOSE 8080
CMD ["python","app.py"]