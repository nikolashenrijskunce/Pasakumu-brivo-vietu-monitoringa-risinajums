FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers + dependencies
RUN playwright install --with-deps

COPY . .

CMD ["python", "-u", "example.py"]