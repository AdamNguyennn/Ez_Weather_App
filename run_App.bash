#!/bin/bash 

mkdir tempdir 
cp -r App/* tempdir 

echo "FROM python" >> tempdir/Dockerfile
echo "WORKDIR /app" >> tempdir/Dockerfile
echo "COPY requirements.txt requirements.txt" >> tempdir/Dockerfile
echo "RUN pip3 install -r requirements.txt" >> tempdir/Dockerfile
echo "COPY . ." >> tempdir/Dockerfile
echo "CMD [\"python3\", \"manage.py\", \"runserver\", \"0.0.0.0:8000\"]" >> tempdir/Dockerfile

cd tempdir 
docker build -t sampleweather .
docker run -t -d -p 8000:8000 --name weatherRunning sampleweather
docker ps -a
