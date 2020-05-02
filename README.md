![](https://github.com/kuhung/flask_vue_ML/blob/master/flask_vue_ml.jpg?raw=true)


## Build Setup

``` bash
# install python libraries
pip install -r requirements.txt

# run the server
python app.py

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

## Deploy
``` bash
gunicorn -b 0.0.0.0:5000 app:expose -D
```

``` markdown
nginx config

server {
	listen 80;

	root /home/spam/dist;
	index index.html index.htm index.nginx-debian.html;
	server_name 149.129.54.11;

	location / {
		autoindex on;
		root /home/spam/dist;
		index  index.html index.htm;
	}

    location /api {
        proxy_pass http://0.0.0.0:5000; 
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

'''
## Refer
- https://github.com/smutuvi/flask_vue_ML
- https://github.com/oleg-agapov/flask-vue-spa
