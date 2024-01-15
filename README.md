# python-setup

## Getting Started
* Set up a container

```
$ docker build -t python312docker .
$ docker run -itd -v $(pwd):/opt/mnt -p 18889:8888 python312docker
```

* Run Python

```
# login container
$ docker ps -a | grep python312
$ docker exec -it XXX /bin/bash

# run python
$ cd src
$ python sample.py 3
```

* Set up Jupyter Lab

```
$ jupyter-lab --allow-root --port=8888 --ip=0.0.0.0 &
# -> http://localhost:18889
```

## Running the tests
* Execute linter, formatter

```
$ poetry run isort src tests
$ poetry run black src tests
$ poetry run flake8 src tests
```

* Execute tests

```
$ poetry install
$ poetry run pytest src tests
```
