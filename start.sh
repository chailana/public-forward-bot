#!/bin/sh
gunicorn app:app & python3 main.py
