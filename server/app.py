import re
import os
from validate_email import validate_email
from flask import jsonify
from flask import request
from flask import Response
import defusedxml
from werkzeug.exceptions import (
    BadRequest,
    NotFound,
    Unauthorized,
    Forbidden,
)
from werkzeug.wrappers import Request
