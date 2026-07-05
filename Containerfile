FROM python:3.13-slim
WORKDIR /project
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install --no-cache-dir -e .
CMD ["python", "-m", "pdac_alert_wedge.commands.audit"]
