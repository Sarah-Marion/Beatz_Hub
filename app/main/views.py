from flask import render_template, request, redirect, url_for, flash, abort
from . import main

@main.route('/')
def index():
    title = 'Home | Beats hub'

    return render_template('index.html', title=title)