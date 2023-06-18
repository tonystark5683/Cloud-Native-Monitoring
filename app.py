import psutil
# Psutil is a Python cross-platform library used to access system details and process utilities. 
# It is used to keep track of various resources utilization in the system.
# Usage of resources like CPU, memory, disks, network, sensors can be monitored. 
# Hence, this library is used for system monitoring, profiling, limiting process resources, and the 
# management of running processes. It is supported in Python versions 2.6, 2.7, and 3.4+. 
from flask import Flask, render_template 
# Flask is basically a python module. It can work with python only and it is a web-developing framework. 
# It is a collection of libraries and modules. Frameworks are used for developing web platforms. 
# Flask is such a type of web application framework. It is completely written in Python language. 
# Unlike Django, it is only written in Python. As a new user Flask is to be used. As it is easier to handle. 
# As it is only written in Python, before installing Flask on the machine, Python should be installed previously. 
# Also, Python Pip should be installed. Nowadays, the latest version of Python Pip is already installed. 

# Features:

# Flask is easy to use and easily understandable for new users in Web Framework.
# It can also be used as any third-party plugin extension.
# It is also used for prototyping purposes.

app = Flask(__name__)#creating app

# SET  the home path
@app.route("/")
def index():
    cpu_per=psutil.cpu_percent()
    mem_per=psutil.virtual_memory().percent#return physical memory available in percent
    message=""
    if cpu_per > 80 or mem_per > 80:
        message = "High cpu or memory utilization detected . Please scale up"
    return render_template("index.html",cpu_metric=cpu_per, mem_metric=mem_per, message=message)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')


