run: app.py
	python app.py

install: requirements.txt
	pip install -r requirements.txt

build:
	python setup.py build bdist_wheel

clean:
	rd /s /q build
	rd /s /q dist
	rd /s /q myprojectname.egg-info