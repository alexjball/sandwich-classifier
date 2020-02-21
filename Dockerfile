FROM pytorch/pytorch

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5050
CMD ["gunicorn", "--chdir", "src", "-w", "4", "-b", "0.0.0.0:5050", "endpoint:app"]