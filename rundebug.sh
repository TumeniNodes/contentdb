#!/bin/bash

FLASK_APP=app/__init__.py FLASK_CONFIG=../config.cfg FLASK_DEBUG=1 python3 -m flask run -h 0.0.0.0 -p 5123
