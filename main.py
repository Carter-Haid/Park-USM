#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import render_template
import GetMap
app=Flask(__name__)


@app.route("/")
def home():
    GetMap.getmap()
 
    return render_template('DorhamMap.html')
if __name__ == '__main__':
    app.run()


# In[ ]:




