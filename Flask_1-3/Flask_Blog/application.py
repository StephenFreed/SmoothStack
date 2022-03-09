from app_package import application, db


if __name__ == "__main__":
    db.create_all()  # creates DB if there is not one
    # application.run(debug=True)  # runs application
    application.run()  # runs application
