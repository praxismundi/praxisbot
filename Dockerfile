FROM python:3.10.2-slim-bullseye
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY . /praxisbot_src
WORKDIR /praxisbot_src
RUN pip install -r requirements.txt
EXPOSE 8443