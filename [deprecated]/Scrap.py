#!/usr/bin/env python
# coding: utf-8

# In[18]:

class Foo:
    def __init__(self):
        self.data = []
        
    def a(self):
        n = len(self.data) + 1
        s = str(n) + '-a'
        self.data.append(s)


# In[19]:


class Foo(Foo):
    def b(self):
        n = len(self.data) + 1
        s = str(n) + '-b'
        self.data.append(s)


# In[20]:


foo = Foo()
foo.a()
foo.b()
foo.a()
foo.b()
foo.b()
print(foo.data)


# In[ ]:

