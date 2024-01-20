python -m pip install twine wheel
python setup.py sdist bdist_wheel
twine upload --config-file .pypirc -r testpypi dist/*

python -m pip install --index-url https://test.pypi.org/simple/ --no-deps sent
python -m pip uninstall sent -y
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps sent==0.0.23
python -m unittest discover -s tests

twine upload --config-file .pypirc -r dist/*