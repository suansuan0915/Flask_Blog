from flaskblog import create_app

app = create_app()  # use Config class as default argument

if __name__ == "__main__":
    app.run(debug=True)