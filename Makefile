init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
 
run:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate && python app.py
 
test:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate && python -m unittest \ test.py
