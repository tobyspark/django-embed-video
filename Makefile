.PHONY: flake8 test coverage

flake8:
	flake8 embed_video example_project tests

isort:
	isort -rc embed_video example_project tests

isort_check_only:
	isort -rc -c embed_video example_project tests

coverage:
	python --version
	coverage erase
	coverage run `which django-admin` test -v2 tests
	coverage report
	codecov --token=2ee6ace6-361e-4b71-91f4-9f07aef28628

test:
	PYTHONPATH=. DJANGO_SETTINGS_MODULE=tests.settings \
		django-admin test tests
