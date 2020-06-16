FROM python:3.8-slim

# author of file
LABEL "maintainer"="Ang Houfu <houfu@outlook.sg>"

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime

# Packages that we need
COPY poetry.lock pyproject.toml /app/
WORKDIR /app

# Project initialization:
RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy all the files from current source directory(from your system) to
# Docker container in /app directory
COPY . .

# Specifies a command that will always be executed when the
# container starts.
# In this case we want to start the python interpreter
ENTRYPOINT ["python", "/app/daily_sudoku/main.py"]