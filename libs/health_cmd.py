import click
import json
import requests


@click.group(name="health")
def health_cmd():
    pass


@health_cmd.command(name="api")
def health_api_cmd():
    try:
        res = requests.get("http://localhost:8080/healthcheck")
        if res.status_code == 200:
            print("webserver is healthy")
    except Exception as e:
        print("webserver is down")


