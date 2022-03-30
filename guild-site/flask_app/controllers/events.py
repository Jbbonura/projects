from flask_app import app
from flask import render_template, request, redirect, session, flash
from pprint import pprint
from flask_app.models.event import Event