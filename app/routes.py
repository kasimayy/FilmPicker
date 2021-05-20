from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AddFilmForm
from app.models import Film
from app import db
import random

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/browse')
def browse():
    all_films = db.session.query(Film).all()
    return render_template('browse.html', all_films=all_films)

@app.route('/browse/remove_film/<int:film_id>', methods=['POST'])
def remove_film(film_id):
    film = db.session.query(Film).get_or_404(film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/addfilm', methods=['GET', 'POST'])
def addfilm():
    form = AddFilmForm()
    if form.validate_on_submit():
        exists = db.session.query(Film).filter_by(title=form.title.data, year=form.year.data).first()
        if exists is not None:
            flash('Film already in database')
        else:
            film = Film(title=form.title.data,
                        year=form.year.data,
                        genre=form.genre.data,
                        platform=form.platform.data,
                        summary=form.summary.data,
                        image_url=form.image_url.data,
                        watched=False)
            db.session.add(film)
            db.session.commit()
            flash('Film \'{}\', {} added successfully'.format(form.title.data, form.year.data))
        return redirect(url_for('addfilm'))
    return render_template('addfilm.html', title='Add Film', form=form)

@app.route('/recommend_me')
def recommend_me():

    return render_template('/recommend_me.html', title='Recommend Me')


@app.route('/recommendation')
def recommendation():
    rand = random.randrange(0, db.session.query(Film).count())
    film = db.session.query(Film)[rand]
    return render_template('recommendation.html', title='Film Recommendation', film=film)