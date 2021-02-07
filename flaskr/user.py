from random import randint 
n = 1 << 255            # TODO: change

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db
bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/x/<uid>', methods=['GET'])
def get_x(uid):
    db = get_db()
    error = None
    r = 0

    if not uid:
        error = 'uid is required.'
    else:
        r = db.execute(
            'SELECT x FROM user WHERE id = ?', (uid,)
        ).fetchone() 

        if not r:
            error = 'uid does not exist in the db'
        
        elif not r['x']:
            r = randint(1,n)
            r = hex(r)
            r = r[2:]
            db.execute(
                'UPDATE user SET x=? WHERE id = ?', (r, uid)
            )
            db.commit()
        else:
            r = r['x']

    if error is None:
        return str(r)

    return error

@bp.route('/host/<uid>', methods=['GET'])
def get_host(uid):
    db = get_db()
    error = None
    r = 0

    if not uid:
        error = 'uid is required.'
    else:
        r = db.execute(
            'SELECT host FROM user WHERE id = ?', (uid,)
        ).fetchone() 

        if not r:
            error = 'uid does not exist in the db'
        
        else:
            r = r['host']

    if error is None:
        return str(r)

    return error

@bp.route('/port/<uid>', methods=['GET'])
def get_port(uid):
    db = get_db()
    error = None
    r = 0

    if not uid:
        error = 'uid is required.'
    else:
        r = db.execute(
            'SELECT port FROM user WHERE id = ?', (uid,)
        ).fetchone() 

        if not r:
            error = 'uid does not exist in the db'
        
        else:
            r = r['port']

    if error is None:
        return str(r)

    return error

@bp.route('/pk/<uid>', methods=['GET'])
def get_pk(uid):
    db = get_db()
    error = None
    r = 0

    if not uid:
        error = 'uid is required.'
    else:
        r = db.execute(
            'SELECT pk FROM user WHERE id = ?', (uid,)
        ).fetchone() 

        if not r:
            error = 'uid does not exist in the db'
        
        elif not r['pk']:
            r = randint(1,n)
            r = hex(r)
            r = r[2:]
            db.execute(
                'UPDATE user SET pk=? WHERE id = ?', (r, uid)
            )
            db.commit()
        else:
            r = r['pk']

    if error is None:
        return str(r)

    return error
