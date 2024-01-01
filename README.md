# Google Analytics Meow Counter

A counter used to track page views and visitor counts from Google Analytics Reporting API. Users can choose to retrieve only textual data or obtain pixelated images featuring cat girls.

Currently only available in a version implemented using Python built with  Flask framework.

## Pre-requisites

Before getting started, you will need to have an account for Google Cloud and Google Analytics. To learn how to obtain them, please refer to [Google Analytics Reporting API v4](https://developers.google.com/analytics/devguides/reporting/core/v4).

To initiate this project, you will also need to acquire the `client_secrets.json` file and the `property_id`.

## Configuration

Move your `client_secrets.json` to the project directory and rename it as `keys.json`, please follow these steps.

Then create your own `config.py` configuration file in the project's `config` directory by referring to `config/config.py.example`.

To determine whether you are using the development environment or production environment, you can set the environment variable `FLASK_ENV` in the `.env`.

## Build and Run

Recommend to use [venv](https://docs.python.org/3/library/venv.html) virtual environment.

```shell
pip install -r requirements.py
python run.py
```

## Usage

After running the service locally, use curl to send a GET request to fetch the page views of a specific resource：

```shell
curl -X GET http://localhost:5500/api/v1/analytics/pv/your_property_id
```

The returned data should be in a format similar to the following:

```json
{
  "screenPageViews": "840"
}
```

## Todo List

- [ ] Docker deploy
- [ ] add meow image dispaly (important)
- [ ] enhanced functionality

## License

MIT