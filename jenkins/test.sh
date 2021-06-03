sudo apt update 
#sudo apt install chromium-chromedriver -y
#sudo apt install python3-venv

sudo apt install python3 python3-pip python3-venv -y 
python3 -m venv venv
source venv/bin/activate
#install pip requirements 
pip3 install -r service-1/requirements.txt
#run pytest
python3 -m pytest service-1 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service-2 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service-3 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
python3 -m pytest service-4 --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing

#run app
#docker-compose up -d build
