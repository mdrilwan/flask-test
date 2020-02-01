# flask-test
Clone the repository by using the below command,

```git clone https://github.com/mdrilwan/flask-test.git```

Install the dependencies,

```
cd flask-test/

python3 -m venv venv

source venv/bin/activate

pip install Flask

python3 -m pip install --user --upgrade setuptools wheel

pip3 install wheel

pip install pytest-html

pip install -e .
```

Execute build.sh script to run test cases and to generate the build
```
./build.sh
```

Test report will be available as test_report.html

Build will be available in the directory dist/
