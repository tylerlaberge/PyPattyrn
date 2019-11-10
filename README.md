# PyPattyrn

```python
from pypattyrn.creational.singleton import Singleton

class DummyClass(object, metaclass=Singleton):  #  DummyClass is now a Singleton!
    ...
```

PyPattyrn is a python package aiming to make it easier and faster to implement design patterns into your own projects.

Design patterns by nature cannot be directly translated into code as they are just a description of how to solve a particular problem. However, many of the common design patterns have boilerplate code that is common throughout all implementations of the pattern. This package captures that common code and makes it easy to use so that you dont have to write it yourself in all your projects.
___

### Contents
___
* [Installation](https://github.com/tylerlaberge/PyPattyrn#installation)
* [Examples](https://github.com/tylerlaberge/PyPattyrn#examples)
  * [Behavioral Patterns](https://github.com/tylerlaberge/PyPattyrn#behavioral-patterns)
    * [Chain of Responsibility](https://github.com/tylerlaberge/PyPattyrn#chain-of-responsibility-pattern)
    * [Command](https://github.com/tylerlaberge/PyPattyrn#command-pattern)
    * [Iterator](https://github.com/tylerlaberge/PyPattyrn#iterator-pattern)
    * [Mediator](https://github.com/tylerlaberge/PyPattyrn#mediator-pattern)
    * [Memento](https://github.com/tylerlaberge/PyPattyrn#memento-pattern)
    * [Null Object](https://github.com/tylerlaberge/PyPattyrn#null-object-pattern)
    * [Observer](https://github.com/tylerlaberge/PyPattyrn#observer-pattern)
    * [Visitor](https://github.com/tylerlaberge/PyPattyrn#visitor-pattern)
  * [Creational Patterns](https://github.com/tylerlaberge/PyPattyrn#creational-patterns)
    * [Builder](https://github.com/tylerlaberge/PyPattyrn#builder-pattern)
    * [Factory](https://github.com/tylerlaberge/PyPattyrn#factory-pattern)
    * [Abstract Factory](https://github.com/tylerlaberge/PyPattyrn#abstract-factory-pattern)
    * [Object Pool](https://github.com/tylerlaberge/PyPattyrn#object-pool-pattern)
    * [Prototype](https://github.com/tylerlaberge/PyPattyrn#prototype-pattern)
    * [Singleton](https://github.com/tylerlaberge/PyPattyrn#singleton-pattern)
  * [Structural Patterns](https://github.com/tylerlaberge/PyPattyrn#structural-patterns)
    * [Adapter](https://github.com/tylerlaberge/PyPattyrn#adapter-pattern)
    * [Composite](https://github.com/tylerlaberge/PyPattyrn#composite-pattern)
    * [Decorator](https://github.com/tylerlaberge/PyPattyrn#decorator-pattern)
    * [Flyweight](https://github.com/tylerlaberge/PyPattyrn#flyweight-pattern)
* [Resources](https://github.com/tylerlaberge/PyPattyrn#resources)

___
### Installation
___
```
pip install pypattyrn
```

or

```
git clone https://github.com/tylerlaberge/PyPattyrn.git
cd PyPattyrn
python setup.py install
```

___
### Examples
___

#### Behavioral Patterns

Patterns which deal with communication between objects.
___
##### Chain of Responsibility Pattern

Pass a request along a chain of objects until the request is handled.

```python
from pypattyrn.behavioral.chain import Chain, ChainLink


class ConcreteChainLinkThree(ChainLink): # This object is a ChainLink

    def handle(self, request): # Implement the handle method.
        if request == 'handle_three':
            return "Handled in chain link three"
        else:
            return self.successor_handle(request) # If this ChainLink can't handle the request, 
                                                  # ask its successor to handle it. 
                                                  # (Has no successor so will raise AttributeError)
                                                  # (This exception is caught and will call a Chains fail method)


class ConcreteChainLinkTwo(ChainLink): # This object is a ChainLink

    def __init__(self): # Override init to set a successor on initialization.
        super().__init__() # first call ChainLinks init
        self.set_successor(ConcreteChainLinkThree()) # Set the successor of this chain link 
                                                     # to a ConcreteChainLinkThree instance.

    def handle(self, request): # Implement the handle method.
        if request == 'handle_two':
            return "Handled in chain link two"
        else:
            return self.successor_handle(request) # If this ChainLink can't handle a request 
                                                  # ask its successor to handle it 
                                                  # (the ConcreteChainLinkThree instance).


class ConcreteChainLinkOne(ChainLink): # This object is a ChainLink

    def __init__(self): 
        super().__init__()
        self.set_successor(ConcreteChainLinkTwo()) # Set the successor of this ChainLink
                                                   # to a ConcreteChainLinkTwo instance.

    def handle(self, request): # Implement the handle method.
        if request == 'handle_one':
            return "Handled in chain link one"
        else:
            return self.successor_handle(request) # If this ChainLink can't handle a request 
                                                  # ask its successor to handle it 
                                                  # (the ConcreteChainLinkTwo instance).

class ConcreteChain(Chain): # This object is a Chain

    def __init__(self): # Override init to initialize a Chain with the starting chain link.
        super().__init__(ConcreteChainLinkOne()) # Initialize this Chain with a start chain link.
                                                 # (a ConcreteChainLinkOne instance)

    def fail(self): # Implement the fail method, this is called if no chain links could handle a request.
        return 'Fail'


chain = ConcreteChain()

assert "Handled in chain link one" == chain.handle("handle_one")
assert "Handled in chain link two" == chain.handle("handle_two")
assert "Handled in chain link three" == chain.handle("handle_three")
assert "Fail" == chain.handle('handle_four')
```
##### Command Pattern

Encapsulate information for performing an action into an object.

```python
from pypattyrn.behavioral.command import Receiver, Command, Invoker


class Thermostat(Receiver): # This object is a Receiver. 
                            # Contains methods for commands to use.

    def raise_temp(self, amount):
        return "Temperature raised by {0} degrees".format(amount)

    def lower_temp(self, amount):
        return "Temperature lowered by {0} degrees".format(amount)


class RaiseTempCommand(Command): # This object is a Command.

    def __init__(self, receiver, amount=5): # Override init to include a temperature amount argument.
        super().__init__(receiver)
        self.amount = amount

    def execute(self): # Implement the execute method.
        return self._receiver.action('raise_temp', self.amount) # Call on the Receiver's action method  with 
                                                                # the name of the method to call and args.
                                                                # (Raises the temperature by 5 degrees.)

    def unexecute(self): # Implement the unexecute method.
        return self._receiver.action('lower_temp', self.amount) # Calls on the Receiver to lower 
                                                                # the temperature by 5 degrees.
                                                     

class LowerTempCommand(Command): # This object is a Command.
 
   def __init__(self, receiver, amount=5):
        super().__init__(receiver)
        self.amount = amount

    def execute(self):
        return self._receiver.action('lower_temp', self.amount) # Call on the receiver to lower the
                                                                # temperature by 5 degrees.

    def unexecute(self):
        return self._receiver.action('raise_temp', self.amount) # Call on the receiver to raise the 
                                                                # temperature by 5 degrees.


class Worker(Invoker): # This object is the Invoker

    def __init__(self): # Override init to initialize an Invoker with Commands to accept.
        super().__init__([LowerTempCommand, RaiseTempCommand]) # Initialize the Invoker with the
                                                               # LowerTempCommand and RaiseTempCommand classes.


thermostat = Thermostat() # Create a Receiver.
worker = Worker() # Create an Invoker.

assert "Temperature lowered by 5 degrees" == worker.execute(LowerTempCommand(thermostat)) # Have the Invoker execute a LowerTempCommand
                                                                                          # which uses the thermostat Receiver.
assert "Temperature raised by 5 degrees" == worker.execute(RaiseTempCommand(thermostat)) # Have the Invoker execute a RaiseTempCommand
                                                                                          # which uses the thermostat Receiver.
assert "Temperature lowered by 5 degrees" == worker.undo() # Undo the previous command (Calls the RaiseTempCommand unexecute method.)
```

##### Iterator Pattern

A way of sequentially accessing elements in a collection.

```python
from pypattyrn.behavioral.iterator import Iterable, Iterator


class Counter(Iterable): # This object is an Iterable

    def __init__(self, max):
        self.count = 0
        self.max = max

    def __next__(self): # Implement the __next__ method.
        self.count += 1 # Increment the count
        if self.count > self.max:
            raise StopIteration() # make sure to raise StopIteration at the appropriate time.
        else:
            return self.count - 1 # Return the count


class CounterIterator(Iterator): # This object is an Iterator

    def __init__(self): # Override init to initialize an Iterator with the Counter object.
        super().__init__(Counter(10)) # Initialize the iterator with a Counter that goes to 10.

counter_iterator = CounterIterator() # Create a CounterIterator.

for count in counter_iterator: # You can loop through it how you would expect.
    print(count)  # 0, 1, 2, 3, ..., 9
```

##### Mediator Pattern

An intermediary for managing communications between many objects.

```python
from pypattyrn.behavioral.mediator import Mediator


class Dog(object):
    sound = ''

    def set_sound(self, sound):
        self.sound = sound


class Cat(object):
    sound = ''

    def set_sound(self, sound):
        self.sound = sound


dog = Dog()
cat = Cat()

mediator = Mediator() # Create a Mediator object.

mediator.connect('set_dog_sound', dog.set_sound) # Connect the signal 'set_dog_sound' to the dog.set_sound method.
mediator.connect('set_cat_sound', cat.set_sound) # Connect the signal 'set_cat_sound' to the cat.set_sound method.

mediator.connect('set_sound', dog.set_sound) # Also connect the signal 'set_sound' to the dog.set_sound method.
mediator.connect('set_sound', cat.set_sound) # Also connect the signal 'set_sound' to the cat.set_sound method.

mediator.signal('set_sound', 'foo') # Send out the signal 'set_sound' 
                                    # with an argument to be passed to the connected methods.
                                    # (Sets dog.sound and cat.sound to 'foo')


assert 'foo' == dog.sound 
assert 'foo' == cat.sound

mediator.signal('set_dog_sound', 'woof') # Send out the signal 'set_dog_sound'
                                         # (Sets dog.sound to 'woof')
mediator.signal('set_cat_sound', 'meow') # Send out the signal 'set_cat_sound'
                                         # (Sets cat.sound to 'meow')

assert 'woof' == dog.sound
assert 'meow' == cat.sound

mediator.disconnect('set_sound', dog.set_sound) # Disconnect the method dog.sound from the signal 'set_sound'

mediator.signal('set_sound', 'bar') # Send out the signal 'set_sound'
                                    # (Only sets cat.sound to 'bar' because we disconnected dog.sound)

assert 'woof' == dog.sound
assert 'bar' == cat.sound
```

##### Memento Pattern

Save the state of an object and rollback to it at a later time.

```python
from pypattyrn.behavioral.memento import Originator


class Cat(Originator): # This object is an Originator
    def __init__(self, name):
        self.name = name


cat = Cat('Tom') # Initialize a Cat with the name 'Tom'
assert cat.name == 'Tom'

cat_memento = cat.commit() # Save the cats current state to a Memento object.
cat.name = 'jerry' # Change the cats name to 'jerry'
assert cat.name == 'jerry'

cat.rollback(cat_memento) # Restore the cats state to the memento object we saved.
assert 'Tom' == cat.name # The cats name was changed back to 'Tom' as expected.
```

##### Null Object Pattern

Encapsulate the absence of an object into an object with neutral behavior.

```python
from pypattyrn.behavioral.null import Null

# You can initialize a Null object with any parameters.
try:
    Null()
    Null('value')
    Null('value', param='value')
except:
    raise AssertionError()

null = Null()

# Attempting to set parameters won't do anything and won't error
try:
    null.foo = 'foo' 
    null.foo.bar = 'bar'
except:
    raise AssertionError()

# Calling on a null object in any way will just return that null object.

assert null == null()
assert null == null('value')
assert null == null('value', param='value')
assert null == null.foo
assert null == null.foo.bar
assert null == null.foo.bar.method1()
assert null == null.foo.bar.method1().method2('foo', bar='bar').attr3

assert str(null) == '' # Null objects string representation is the empty string.
assert repr(null) == '' # Null objects repr is the empty string.
assert bool(null) is False # Null object evaluates to False as a boolean.

# Trying to delete attributes doesn't do anything and won't error.
try:
    del null.foo 
    del null.foo.bar
except:
    raise AssertionError()
```

##### Observer Pattern

Notify many objects when a single object's state changes.

```python
from pypattyrn.behavioral.observer import Observable, Observer


class ConcreteObservable(Observable): # This object is an Observable.
    _kinda_private_var = 'I am kinda private'
    __private_var = 'I am more private'

    def change_state(self, **kwargs): # Some method to change this objects state and notify observers.
        for key, value in kwargs.items():
            setattr(self, key, value) # Change the objects state.

        self.notify() # Notify all observers of the change in state.
                      # Will call the update method of each attached observer with kwargs that come
                      # from this objects __dict__ attribute, minus any private variables (starts with __ or _)


class ConcreteObserver(Observer): # This object is an Observer.
    updated_state = None

    def update(self, **state): # Implement the update method. 
                               # Called when an attached observable calls its notify method.
        self.updated_state = state


observable = ConcreteObservable() # Create an Observable
observer_1 = ConcreteObserver() # Create Observers
observer_2 = ConcreteObserver()
observer_3 = ConcreteObserver()

observable.attach(observer_1) # Attach each of the Observers to the Observable
observable.attach(observer_2)
observable.attach(observer_3)

observable.change_state(foo='foo', bar='bar') # Change the Observable's state.
                                              # Also calls notify which will call each Observers update method.

expected_state = {'foo': 'foo', 'bar': 'bar'} 

# Make sure each Observers state was changed accordingly when the notify method was called by the Observable.

assert sorted(expected_state.keys()) == sorted(observer_1.updated_state.keys()) and \
       sorted(expected_state.values()) == sorted(observer_1.updated_state.values())

assert sorted(expected_state.keys()) == sorted(observer_2.updated_state.keys()) and \
       sorted(expected_state.values()) == sorted(observer_2.updated_state.values())

assert sorted(expected_state.keys()) == sorted(observer_3.updated_state.keys()) and \
       sorted(expected_state.values()) == sorted(observer_3.updated_state.values())

observable.detach(observer_1) # Detach Observer 1 from the Observable
observable.change_state(bar='foobar') # Change the Observables state.
expected_state_2 = {'foo': 'foo', 'bar': 'foobar'}

# Make sure each Observers state was changed accordingly when notify was called by the Observable,
# Except for observer_1 because we detached that Observer from the Observable.

assert sorted(expected_state_2.keys()) != sorted(observer_1.updated_state.keys()) or \
       sorted(expected_state_2.values()) != sorted(observer_1.updated_state.values())

assert sorted(expected_state_2.keys()) == sorted(observer_2.updated_state.keys()) and \
       sorted(expected_state_2.values()) == sorted(observer_2.updated_state.values())

assert sorted(expected_state_2.keys()) == sorted(observer_3.updated_state.keys()) and \
       sorted(expected_state_2.values()) == sorted(observer_3.updated_state.values())
```

##### Visitor Pattern

Add new operations to an existing class without modifying it.

```python
from pypattyrn.behavioral.visitor import Visitee, Visitor


class A(Visitee): # This object is a Visitee
    pass


class B(A): # This object is an A, which also makes this a Visitee.
    pass


class C(B): # This object is a B, which also makes this a Visitee.
    pass


class D(Visitee): # This object is a Visitee
    pass


class NodeVisitor(Visitor): # This object is a Visitor

    def generic_visit(self, node, *args, **kwargs): # Implement the generic visit method.
                                                    # This is called when there is no visit_ method
                                                    # implemented for a particular visitee.

        return 'generic_visit ' + node.__class__.__name__

    def visit_b(self, node, *args, **kwargs): # Called when this object visits a Visitee of class 'B'.
        return 'visit_b ' + node.__class__.__name__

    def visit_d(self, node, *args, **kwargs): # Called when this object visits a Visitee of class 'D'.
        return 'visit_d {0} args: {1} kwargs: {2}'.format(node.__class__.__name__, args, kwargs)

# Create Visitee's
node_a = A()
node_b = B()
node_c = C()
node_d = D()

# Create Visitor
node_visitor = NodeVisitor()

assert 'generic_visit A' == node_a.accept(node_visitor) # Visit node_a with the Visitor.
                                                        # Since the visitor does not have a visit_a method,
                                                        # generic_visit is called.
assert 'visit_b B' == node_b.accept(node_visitor) # Visit node_b with the Visitor.
                                                  # Calls the visitors visit_b method.
assert 'visit_b C' == node_c.accept(node_visitor) # Visit node_c with the Visitor.
                                                  # Even though the visitor does not have a visit_c method, 
                                                  # since node_c inherits B, the Visitors visit_b method is called.

# Visit node_d with the Visitor. Calls the visitors visit_d method.
assert "visit_d D args: ('foo', 'bar') kwargs: {'foobar': 'foobar'}" == node_d.accept(node_visitor,
                                                                                      'foo', 'bar',
                                                                                      foobar='foobar')
```

___
#### Creational Patterns

Patterns which deal with object creation.
___

##### Builder Pattern

Separate object construction from its representation.

```python
from pypattyrn.creational.builder import Builder, Director


class Building(object):  # The object being constructed.

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class HomeBuilder(Builder):  # A base Builder class for constructing homes.

    def __init__(self):
        super().__init__(Building())  # Initialize the Builder class with a Building instance.
        self._register('floor', self._build_floor)  # Register the keyword 'floor' with the _build_floor method.
        self._register('size', self._build_size)  # Register the keyword 'size' with the _build_size method.

    def _build_floor(self):
        pass

    def _build_size(self):
        pass


class HouseBuilder(HomeBuilder):  # A concrete HomeBuilder class for constructing houses

    def _build_floor(self):
        self.constructed_object.floor = 'One'  # Alter the Building's floor attribute.

    def _build_size(self):
        self.constructed_object.size = 'Big'  # Alter the Building's size attribute.


class FlatBuilder(HomeBuilder):  # A concrete HomeBuilder class for constructing flats

    def _build_floor(self):
        self.constructed_object.floor = 'More than one'  # Alter the Building's floor attribute.

    def _build_size(self):
        self.constructed_object.size = 'Small'  # Alter the Building's size attribute.


class HomeDirector(Director):  # A Director class for managing home construction.

    def construct(self):
        self.builder.build('floor')  # Build the floor part of the Building by using the keyword 'floor'
        self.builder.build('size')  # Build the size part of the Building by using the keyword 'size'


home_director = HomeDirector()

home_director.builder = HouseBuilder()  # Use the house builder.
home_director.construct()  # Construct the house.
house = home_director.get_constructed_object()  # Get the constructed house.
print(repr(house))    #Floor: One | Size: Big
    
home_director.builder = FlatBuilder()  # Use the flat builder.
home_director.construct()  # Construct the flat.
house = home_director.get_constructed_object()  # Get the constructed flat.
print(repr(house))    #Floor: More than one | Size: Small
```

##### Factory Pattern

An interface for creating an object.

```python
from pypattyrn.creational.factory import Factory  # This is just an interface


class Cat(object):

    def speak(self):
        print('meow')


class Dog(object):

    def speak(self):
        print('woof')


class AnimalFactory(Factory):  # A factory class for creating animals.

    def create(self, animal_type):  # Implement the abstract create method.
        if animal_type == 'cat':
            return Cat()
        elif animal_type == 'dog':
            return Dog()
        else:
            return None


animal_factory = AnimalFactory()

cat = animal_factory.create('cat')
dog = animal_factory.create('dog')

cat.speak()  # 'meow'
dog.speak()  # 'woof'
```

##### Abstract Factory Pattern

Create an instance from a family of factories.

```python
from pypattyrn.creational.factory import Factory, AbstractFactory


class Cat(object):

    def speak(self):
        print('meow')


class Dog(object):

    def speak(self):
        print('woof')


class Ant(object):

    def march(self):
        print('march')


class Fly(object):

    def fly(self):
        print('fly')


class AnimalFactory(Factory):  # A factory class for creating animals.

    def create(self, animal_type):  # Implement the abstract create method.
        if animal_type == 'cat':
            return Cat()
        elif animal_type == 'dog':
            return Dog()
        else:
            return None


class InsectFactory(Factory):  # A factory class for creating insects.

    def create(self, insect_type):  # Implement the abstract create method.
        if insect_type == 'ant':
            return Ant()
        elif insect_type == 'fly':
            return Fly()
        else:
            return None


class CreatureFactory(AbstractFactory):  # A Factory class for creating creatures.

    def __init__(self):
        super().__init__()
        self._register('insect_factory', InsectFactory())  # Register an InsectFactory with a keyword.
        self._register('animal_factory', AnimalFactory())  # Register an AnimalFactory with a keyword.

    def create(self, creature_type):  # Implement the Abstract create method.
        if creature_type == 'cat' or creature_type == 'dog':
            return self._factories['animal_factory'].create(creature_type)  # Use the AnimalFactory
        elif creature_type == 'ant' or creature_type == 'fly':
            return self._factories['insect_factory'].create(creature_type)  # Use the InsectFactory
        else:
            return None

creature_factory = CreatureFactory()

cat = creature_factory.create('cat')
dog = creature_factory.create('dog')
ant = creature_factory.create('ant')
fly = creature_factory.create('fly')

cat.speak()  # 'meow'
dog.speak()  # 'woof'
ant.march()  # 'march'
fly.fly()  # 'fly'
```

##### Object Pool Pattern

Provide a pool of instantiated objects which can be checked out and returned rather than creating new objects all the time.

```python
from pypattyrn.creational.pool import Reusable, Pool


class Dog(Reusable):
    def __init__(self, sound):
        self.sound = sound
        super().__init__()


class DogPool(Pool):
    def __init__(self):
        super().__init__(Dog, 'woof')


dog_pool = DogPool()

dog_one = dog_pool.acquire()
dog_two = dog_pool.acquire()
dog_two.sound = 'meow'

dog_pool.release(dog_one)
dog_three = dog_pool.acquire()

dog_pool.release(dog_two)
dog_four = dog_pool.acquire()

assert id(dog_one) == id(dog_three)
assert id(dog_two) == id(dog_four)
assert dog_one.sound == dog_two.sound
assert dog_three.sound == dog_four.sound
assert dog_one.sound == dog_four.sound
```

##### Prototype Pattern

Clone an object to produce new objects.

```python
from pypattyrn.creational.prototype import Prototype


class Point(Prototype):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y


point_one = Point(15, 15)
point_two = point_one.prototype(z=20)
point_three = point_two.prototype()

assert point_one.x == point_two.x
assert point_one.y == point_two.y
assert not hasattr(point_one, 'z')
assert hasattr(point_two, 'z')
assert point_two.z == 20
assert point_three.__dict__ == point_two.__dict__

from math import sqrt
def distance_to(this, other):
    return sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2)

point_four = point_three.prototype(distance_to=distance_to)

assert hasattr(point_four, 'distance_to')
assert point_four.distance_to(point_three) == 0
```

##### Singleton Pattern

Ensure that only a single instance of a class exists.

```python
from pypattyrn.creational.singleton import Singleton


class DummySingletonOne(object, metaclass=Singleton):

    def __init__(self):
        pass


class DummySingletonTwo(object, metaclass=Singleton):

    def __init__(self):
        pass


dummy_class_one_instance_one = DummySingletonOne()
dummy_class_one_instance_two = DummySingletonOne()

dummy_class_two_instance_one = DummySingletonTwo()
dummy_class_two_instance_two = DummySingletonTwo()

assert id(dummy_class_one_instance_one) == id(dummy_class_one_instance_two)
assert id(dummy_class_two_instance_one) == id(dummy_class_two_instance_two)

assert id(dummy_class_one_instance_one) != id(dummy_class_two_instance_one)
assert id(dummy_class_one_instance_two) != id(dummy_class_two_instance_two)
```
___

#### Structural Patterns

Patterns which deal with object composition
___

##### Adapter Pattern

Wrap an object into an interface which the client expects. 

```python
from pypattyrn.structural.adapter import Adapter


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"

cat = Cat()
dog = Dog()

cat_adapter = Adapter(cat, make_noise=cat.meow)
dog_adapter = Adapter(dog, make_noise=dog.bark)

assert cat_adapter.make_noise == cat.meow
assert dog_adapter.make_noise == dog.bark

assert cat_adapter.make_noise() == 'meow!'
assert dog_adapter.make_noise() == 'woof!'

assert cat_adapter.name == 'Cat'
assert dog_adapter.name == 'Dog'

assert cat_adapter.meow() == 'meow!'
assert dog_adapter.bark() == 'woof!'

assert cat_adapter.original_dict() == cat.__dict__
assert dog_adapter.original_dict() == dog.__dict__

bad_cat_adapter = Adapter(cat, foo=cat.name)

try:
    bad_cat_adapter.foo
except AttributeError:
    pass
else:
    raise AssertionError()

bad_dog_adapter = Adapter(dog, make_noise=cat.meow)

try:
    bad_dog_adapter.make_noise()
except AttributeError:
    pass
else:
    raise AssertionError()
```

##### Composite Pattern

Compose objects into a tree structure of objects that can be treated uniformly.

```python
from pypattyrn.structural.composite import Composite


class Component(object):

    def do_something(self):
        pass


class Leaf(Component):

    def __init__(self):
        self.did_something = False

    def do_something(self):
        self.did_something = True


leaf_one = Leaf()
leaf_two = Leaf()
leaf_three = Leaf()

composite_one = Composite(Component)
composite_two = Composite(Component)
composite_three = Composite(Component)

composite_one.add_component(leaf_one)
composite_two.add_component(leaf_two)
composite_three.add_component(leaf_three)

composite_two.add_component(composite_three)
composite_one.add_component(composite_two)


assert set() == {leaf_one, composite_two}.symmetric_difference(composite_one.components)
assert set() == {leaf_two, composite_three}.symmetric_difference(composite_two.components)
assert set() == {leaf_three}.symmetric_difference(composite_three.components)

composite_two.remove_component(composite_three)

assert set() == {leaf_two}.symmetric_difference(composite_two.components)

assert not leaf_one.did_something
assert not leaf_two.did_something
assert not leaf_three.did_something

composite_one.do_something()

assert leaf_one.did_something
assert leaf_two.did_something
assert not leaf_three.did_something
```

##### Decorator Pattern

Attach additional functionality to functions.

```python
import time
from pypattyrn.structural.decorator import DecoratorSimple, DecoratorComplex, CallWrapper


class TimeThis(DecoratorSimple):

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time() - start
        return result, end


class SlowClass(object):

    @TimeThis
    def slow_function(self, n):
        time.sleep(n)
        return 'foo'

slow_class = SlowClass()
result = slow_class.slow_function(1)
assert result[0] == 'foo'
assert 1 <= result[1] <= 2


class Alert(DecoratorComplex):

    def __init__(self, alert_time):
        self.alert_time = alert_time

    @CallWrapper
    def __call__(self, func, *args, **kwargs):
        start = time.time()
        return_val = func(*args, **kwargs)
        end = time.time() - start
        if end > self.alert_time:
            return return_val, True
        return return_val, False


class SlowClass(object):

    @Alert(1)
    def slow_function_true(self, n):
        time.sleep(n)
        return n

    @Alert(1)
    def slow_function_false(self, n):
        return n


slow_class = SlowClass()
assert (2, True) == slow_class.slow_function_true(2)
assert (10, False) == slow_class.slow_function_false(10)
```

##### Flyweight Pattern

Share data with other similar objects to increase efficiency.

```python
from pypattyrn.structural.flyweight import FlyweightMeta


class Card(object, metaclass=FlyweightMeta):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


three_of_spades = Card('Spade', 3)
four_of_spades = Card('Spade', 4)
three_of_spades_two = Card('Spade', 3)

assert id(three_of_spades) == id(three_of_spades_two)
assert id(three_of_spades) != id(four_of_spades)
```
___

#### Resources
___

* [API Documentation](https://tylerlaberge.github.io/PyPattyrn/)
* [General Design Pattern Information](https://sourcemaking.com/design_patterns)

___
