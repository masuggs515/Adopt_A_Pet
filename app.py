from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPet, EditPet

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'adoptee'


connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def pet_list():
    """Home Page that shows all cats."""

    pets = Pet.query.all()
    return render_template('home_page.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def new_pet_form():
    """Show form to add new pet, and when form is submitted retrieve data and create new pet. Redirect to list of pets."""

    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} the {species}")
        return redirect("/")

    else:
        return render_template("new_pet_form.html", form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def pet_details_and_edit(pet_id):
    """
    Show details of the specific pet with edit form below.
    Show form to edit pet, and when form is submitted retrieve data and update pet. Redirect to list of pets.
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        flash(f"Updated {pet.name} the {pet.species}'s details.")
        return redirect("/")

    else:
        return render_template('pet_details.html', pet=pet, form=form)