# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequences of values. The difference is that lists are dynamic and tuples are immutable. Only tuples will work as keys in dictionaries. This is because tuples can be hashed because their content can't be modified. Dictionaries require that keys provide a hash function to store and look up keys/values. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they are both a sequence of values. Their differences:  
- Sets can't contain duplicates
- Sets are unordered  
- Sets can only contain hashable items  

>>Sets are faster for finding an element. Because sets are implemented using hash tables, that means that the position of an object inside a set is recorded and the time it takes to search is the same no matter the size of the set. A list isn't hashable, so the larger the list, the longer it could take to search.  

>>Example of a list: my_list = ['Tom', 'Mary', 'Jonas', 'Tom']  
>>Example of a set: my_set = {1, 2, 3}  

 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda keyword allows the user to create an anonymous function. Lambda functions are restricted to a single expression. It can be used to pass a function as an argument.  

>> Example:  

>> sorted(['Cat', 'dog', 'antelope', 'zebra']) would return ['Cat', 'antelope', 'dog', 'zebra']  
>> sorted(['Cat', 'dog', antelope', 'zebra'], key = lambda word: word.lower()) would return ['antelope', 'Cat', 'dog', zebra'] 


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





