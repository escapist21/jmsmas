import functools
import os
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
)

from .mongo_operations import query_documents, query_one, update_one

bp = Blueprint('qc', __name__, url_prefix="/qc")


@bp.route('/', methods=['GET'])
def qc_index():

    documents = query_documents()

    return render_template('qc/index.html', records=documents)


@bp.route('/<KEY>', methods=['GET'])
def qc_detail(KEY):
    document = query_one(KEY=KEY)

    return render_template('qc/detail.html', record=document)


@bp.route('/<KEY>/edit', methods=['GET', 'POST'])
def qc_edit(KEY):
    document = query_one(KEY=KEY)
    if request.method == "POST":
        comments = request.form['comments']
        rating = request.form['rating']
        is_accepted = request.form.get('accepted', False)
        error = None

        if not comments:
            error = 'Comments is required'
        elif not rating:
            error = 'Rating is required'
        
        if error is not None:
            flash(error)
        else:
            update_one(KEY=KEY, comments=comments, rating=rating, is_accepted=is_accepted)
            return redirect(url_for('qc.qc_detail', KEY=KEY))
    
    return render_template('qc/edit.html', record=document)
