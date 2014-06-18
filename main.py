#!/usr/bin/python3.3

if __name__ == "__main__":
    from app import app
    app.run('0.0.0.0', port=5554, debug=True)
