# import app
from app import app

# import model and db instance
from models import db, Sighting

# Define seeding functions (optional: use Faker to help generate fake data)

if __name__ == "__main__":
    with app.app_context():
        
        db.session.add(Sighting(date='09/2024', time="0600", location="Arizona", shape_of_craft='circular', approximate_size=60, approximate_speed=20, description="scary", reporter="Alex", reporter_reliable_witness= True))

        db.session.add(Sighting(date='08/2023', time="0500", location="Utah", shape_of_craft='circular', approximate_size=80, approximate_speed=50, description="odd", reporter="Byron", reporter_reliable_witness= True))

        db.session.add(Sighting(date='07/2023', time="0400", location="Wyoming", shape_of_craft='circular', approximate_size=90, approximate_speed=60, description="odd", reporter="Charles", reporter_reliable_witness= False))

        # Commit the transaction
        db.session.commit()
