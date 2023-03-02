from flask import Flask, render_template, request
from app.bp.apis import bp

app = Flask(__name__)

app.register_blueprint(bp)
