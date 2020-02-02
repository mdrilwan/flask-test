#!/bin/bash
if [ -d build ]
then
	echo "Deleting build/ directory";
	rm -rf build
fi
if [ -d dist ]
then
	echo "Deleting dist directory";
	rm -rf dist
fi
if [ -d flaskr.egg-info ]
then
	echo "Deleting flaskr.egg-info directory";
	rm -rf flaskr.egg-info
fi
if [ -f test_report.html ]
then
	echo "Removing the file test_report.html";
	rm test_report.html
fi
. venv/bin/activate
pytest --html=test_report.html --self-contained-html
if [ $? -eq 0 ]
then
	 python3 setup.py sdist bdist_wheel
fi
