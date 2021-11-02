# Grafana Custom Notification for SMS sending

## Requirements

- Python 3 (python 3.9 is used for develop environment)
- Pip (if you would like to use virtualenv)

## Preparing environment

- Goto project dir
- Install `virtualenv`

  ```bash
  pip install virtualenv
  ```

- Create `virtualenv` for this project

  ```bash
  virtualenv .env
  ```

- Activate `virtualenv`

  ```bash
  source .env/bin/activate
  ```

- Deactivate `virtualenv`

  ```bash
  deactivate
  ```

## Install python libs

- Goto project dir
- Run pip command to install

  ```bash
  make install-requirements
  ```

## Run application

- Goto project dir
- Start the app

  ```bash
  make run
  ```

### Docker

- Goto project dir
- Build image

  ```bash
  make docker-build
  ```

- Run application with `docker-compose`

  ```bash
  cd docker
  docker-compose up -d
  ```

- Login Grafana UI at [http://localhost:3000](http://localhost:3000) with username `admin` and password `admin`

- Setup a notification channel with these information:
  - Type: `Webhook`
  - URL: `http://host.docker.internal:5000/grafana` (Running with docker-compose)
  - Optional Webhook settings:
    - Http Method: `POST`
    - Username: `grafana`
    - Password: `grafana`
