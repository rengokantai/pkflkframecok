####pkflkframecok
#####cp1 configuration
######
load config 
```
app.config.from_pyfile('myconfig.cfg') #load from another file

app.config.from_object('myapp.default_settings') #an object

app.config.from_object(__name__) #To load from same file

app.config.from_envvar('PATH_TO_CONFIG_FILE') #load env
```
######organization static files
```
<img src='{{ url_for('static', filename="logo.png") }}'>
```
#####Chapter 4. Working with Views

```
bar = request.args.get('foo', 'bar')  //default=bar
```

from post
```
bar = request.form.get('foo', 'bar')  //default=bar
```
get/post
```
@app.route('/a-request', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        bar = request.args.get('foo', 'bar')
    else:
        bar = request.form.get('foo', 'bar')
```
decorator and non-decorator
```
@app.route('/a-get-request')  //or
app.add_url_rule('/a-get-request', view_func=methodname)
```
#####4Vorking with views
######Dealing with XHR requests
```
from flask import request, render_template, jsonify
if request.is_xhr:
        products = Product.query.all()
        return jsonify({
            'count': len(products)
        })
```