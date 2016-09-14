<h1>PyPattyrn</h1>
<h3>Design Pattern Templates for Python.</h3>

<p>PyPattyrn is a python package aiming to make it easier and faster to implement design patterns into your own projects.</p>
<p>Design patterns by nature cannot be directly translated into code as they are just a description of how to solve a particular problem. However, many of the common design patterns have some boilerplate code that is common throughout all implementations of the pattern. This package captures that common code and makes it easy to use so that you dont have to write it yourself in all your projects.<p>

<h4>Example</h4>

<p>A simple example would be the Singleton pattern. Instead of writing your own code to enforce a Singleton class and copying that code between all your projects that need a singleton, simply use the Singleton Metaclass from PyPattyrn.</p>

```python
from pypattyrn.creational.singleton import Singleton

class DummyClass(object, metaclass=Singleton):
    ...
```
    
<p>Done. Thats it, the DummyClass is now a Singleton!</p>

<h4>Resources</h4>

<p>Visit <a href='https://sourcemaking.com/design_patterns'>https://sourcemaking.com/design_patterns</a> for information on common design patterns.

<p>Visit the <a href='https://github.com/tylerlaberge/PyPattyrn/wiki'>wiki</a> for more examples on all the design pattern templates available in PyPattyrn.</p>

<p>Visit https://tylerlaberge.github.io/PyPattyrn/ for API documentation.</p>

<h4>Installation</h4>

    pip install pypattyrn

or

    git clone https://github.com/tylerlaberge/PyPattyrn.git
    cd PyPattyrn
    python setup.py install
