web: gunicorn book_store.wsgi --log-file -
release: python manage.py migrate
web: npm install 
web: node vue_bookstore/server.js