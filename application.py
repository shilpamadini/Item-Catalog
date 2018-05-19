#!/usr/bin/env python
"""Python code for itemcatalog application."""

from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash, make_response
from sqlalchemy import create_engine
from sqlalchemy import desc, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Catalog, CatalogItem
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import random
import string
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog App"

# Create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
            for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)

    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'),200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;\
-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(username=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
        # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Show the catalog


@app.route('/')
@app.route('/catalog')
def showCatalog():
    """Displays catalogs by rendering catalog.html."""

    catalogs = session.query(Catalog).all()
    items = session.query(CatalogItem).order_by(
            desc(CatalogItem.id)).limit(10).all()
    return render_template('catalog.html', catalogs=catalogs, items=items)


@app.route('/<int:catalog_id>/')
def showItems(catalog_id):
    """Displays catalog items by rendering items.html."""

    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    catalogs = session.query(Catalog).all()
    items = session.query(CatalogItem).filter_by(catalog_id=catalog_id).all()
    if 'username' not in login_session:
        return render_template('publicitems.html', items=items,
                    catalog=catalog, catalogs=catalogs)
    else:
        return render_template('items.html', items=items,
                    catalog=catalog, catalogs=catalogs)



@app.route('/<int:catalog_id>/<int:item_id>/')
def showDescription(catalog_id, item_id):
    """Displays item description by rendering description.html."""

    catalogs = session.query(Catalog).all()
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    item = session.query(CatalogItem).filter_by(id=item_id).all()
    creator = session.query(CatalogItem).filter_by(id=item_id).one()
    if 'username' not in login_session or creator.user_id != login_session['user_id']:
        return render_template('publicdescription.html', catalog=catalog,
            item=item, catalogs=catalogs)
    else:
        return render_template('description.html', catalog=catalog,
            item=item, catalogs=catalogs)


@app.route('/<int:catalog_id>/add', methods=['GET', 'POST'])
def addItem(catalog_id):
    """adds news items in the catalog."""

    if 'username' not in login_session:
        return redirect('/login')
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if request.method == 'POST':
        if request.form['name'] == '':
            return redirect(url_for('showItems', catalog_id=catalog_id))
        else:
            addItem = CatalogItem(item_name=request.form['name'],
                    description=request.form['description'], catalog_id=catalog_id,
                    user_id=login_session['user_id'])
            session.add(addItem)
            session.commit()
            flash('New %s Item Successfully Added' % (addItem.item_name))
            return redirect(url_for('showItems', catalog_id=catalog_id))
    else:
        return render_template('additem.html', catalog_id=catalog_id)


@app.route('/<int:catalog_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(catalog_id, item_id):
    """edits items in a catalog."""

    if 'username' not in login_session:
        return redirect('/login')
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    editItem = session.query(CatalogItem).filter_by(id=item_id).one()
    if login_session['user_id'] != editItem.user_id:
        return "<script>function myFunction() {alert('You are not authorized\
to edit this item.');}</script><body onload='myFunction()''>"

    if request.method == 'POST':
        if request.form['description']:
            editItem.description = request.form['description']
        if request.form['name']:
            editItem.item_name = request.form['name']
        session.add(editItem)
        session.commit()
        flash('Item successfully edited')
        return redirect(url_for('showItems', catalog_id=catalog_id))
    else:
        return render_template('edititem.html', catalog_id=catalog_id,
            item=editItem)


@app.route('/<int:catalog_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(catalog_id, item_id):
    """delete item in a catalog."""

    if 'username' not in login_session:
        return redirect('/login')
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    deleteItem = session.query(CatalogItem).filter_by(id=item_id).one()
    if login_session['user_id'] != deleteItem.user_id:
        return "<script>function myFunction() {alert('You are not authorized\
to delete this item.');}</script><body onload='myFunction()''>"

    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        return redirect(url_for('showItems', catalog_id=catalog_id))
    else:
        return render_template('deleteitem.html', catalog_id=catalog_id,
            item=deleteItem)

# JSON APIs to provide catalog and items data


@app.route('/catalog/JSON')
def showCatalogJSON():
    """provides catalog data in JSON format."""

    catalog = session.query(Catalog).all()
    return jsonify(catalog=[i.serialize for i in catalog])


@app.route('/catalog/items/JSON')
def showItemsJSON():
    """provides items data for all the catalogs in JSON format."""

    items = session.query(CatalogItem).order_by(asc(CatalogItem.id)).all()
    return jsonify(items=[i.serialize for i in items])


@app.route('/catalog/<int:catalog_id>/items/JSON')
def showCatalogItemsJSON(catalog_id):
    """provides items for a particular catalog in JSON format."""
    items = session.query(CatalogItem).filter_by(
        catalog_id=catalog_id).order_by(asc(CatalogItem.id)).all()
    return jsonify(items=[i.serialize for i in items])

# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
        flash("You have successfully been logged out.")
        return redirect(url_for('showCatalog'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCatalog'))

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
