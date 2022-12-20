djangoVenv := ~/sandbox/django_venv

ProjectName := pict_warehouse
ProjectDir := ~/sandbox/pict_warehouse
AppName := pware

.ONESHELL:

generate:
	mkdir -p ${djangoVenv}
	cd ${djangoVenv}
	python3 -m venv venv
	. venv/bin/activate
	pip install -U pip
	pip install Django
	cd ~/sandbox
	django-admin startproject ${ProjectName}
	cd ${ProjectName}
	python manage.py startapp ${AppName}
	python manage.py migrate
	@echo "Created project in: ${ProjectDir}"

run:
	python3 manage.py runserver

.PHONY: clean
clean:
	rm -rf ${ProjectDir}

.PHONY: check
check:
	python manage.py test
