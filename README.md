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