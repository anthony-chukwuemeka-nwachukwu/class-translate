# Group-Expense-Tracker-GET

### How To Run

1. Install `virtualenv`:

```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:

```
$ virtualenv env
```

3. Activate the environment:

```
$ .\env\Scripts\activate
```

4. Install the dependencies:

```
$ (env) pip install -r requirements.txt
```

5. Start the web server:

```
$ (env) python application.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

## Contributing
