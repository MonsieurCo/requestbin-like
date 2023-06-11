include .env

make-req:
	python3 -m  pipreqs.pipreqs --force .
install-req:
	pip3 install -r requirements.txt