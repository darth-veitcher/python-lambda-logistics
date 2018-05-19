init:
	pip install -r requirements.txt

package-test:
	rm -rf dist/*
	pip install wheel
	python setup.py sdist
	python setup.py bdist_wheel  # use additional --universal flag if works on python2 and 3
	gpg --detach-sign -a dist/*.gz
	twine upload --repository testpypi --config-file .pypirc dist/*.gz dist/*.gz.asc dist/*.whl

package-prod:
	rm -rf dist/*
	pip install wheel
	python setup.py sdist
	python setup.py bdist_wheel  # use additional --universal flag if works on python2 and 3
	gpg --detach-sign -a dist/*.gz
	twine upload --config-file .pypirc --repository pypi dist/*.gz dist/*.gz.asc dist/*.whl