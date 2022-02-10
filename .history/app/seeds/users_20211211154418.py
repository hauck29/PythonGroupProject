from app.models import db, User



# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', profile_image='https://darebnb.s3.us-east-2.amazonaws.com/amigo.jpg', password='password')
    natgeo = User(
        username='natgeo', email='natgeo@mail.com', profile_image='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/profile_pics/natgeo_95140556_594026277870211_4156802974091313152_n.jpg', password='password')
    nasa = User(
        username='NASA', email='nasa@mail.com', profile_image='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/profile_pics/nasa_29090066_159271188110124_1152068159029641216_n.jpg', password='password')
    oneUser = User(
        username='8thdamon', email='oneuser@mail.com', profile_image='', password='password')
    twoUser = User(
        username='TwoUser', email='twouser@mail.com', profile_image='', password='password')

# profile_image='',

    db.session.add(demo)
    db.session.add(natgeo)
    db.session.add(nasa)
    db.session.add(oneUser)
    db.session.add(twoUser)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
