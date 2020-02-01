#!/bin/bash
pytest --html=test_report.html
if [ $? -eq 0 ]
then
	echo "All test cases passed"
	 python3 setup.py sdist bdist_wheel
else
	echo "some test cases have failed"
fi
