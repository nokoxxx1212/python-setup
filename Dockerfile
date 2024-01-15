FROM python:3.12

# install python package
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# mount dir
RUN mkdir -p /opt/mnt
WORKDIR /opt/mnt

# expose port
EXPOSE 8888