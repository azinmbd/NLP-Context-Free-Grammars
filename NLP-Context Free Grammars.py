#!/usr/bin/env python
# coding: utf-8

# In[20]:


# if we have 2 tree means that our sentencee is ambigues


# In[21]:


import nltk


# In[22]:


from nltk import CFG


# In[23]:


grammar  = CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")


# In[24]:


sent = ["I", "shot", "an", "elephant", "in", "my", "pajamas"]


# In[25]:


parser = nltk.ChartParser(grammar)


# In[26]:


trees = parser.parse(sent)


# In[27]:


for tree in trees:
    print(tree)


# In[28]:


grammar1  = CFG.fromstring("""
S -> NP VP
VP -> V NP | VP PP
PP -> P NP
V -> 'saw' | 'ate' | 'walked'
NP -> 'John' | 'Marry' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P -> 'in' | 'on' |'by' | 'with'
""")


# In[29]:


sent = "the dog saw a man in the park".split()


# In[30]:


rd_parser = nltk.RecursiveDescentParser(grammar1)


# In[ ]:


for tree in rd_parser.parse(sent):
    print(tree)


# In[ ]:


# recursve means when we have NP->NP VP
# we have the Np on both side we can handle the recursive that
# the recursive part should be on the left side the above is correct
# but Np-> vp NP is wrong 
# these are direct recursion


# In[ ]:


# indirecy recursion liket
# s-> VP NP
# vp-> v S


# In[ ]:


grammar2  = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | ProbN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'a' | 'the' 
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
Adj -> 'angry' | 'frightened' | 'little' | 'tall' 
V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
P -> 'on'
""")


# In[ ]:


SENT2 = "the angry bear chased  the frightened little squirrel".split()


# In[ ]:


rd_parser = nltk.RecursiveDescentParser(grammar2)


# In[ ]:


for tree in rd_parser.parse(SENT2):
    print(tree)


# In[ ]:


sent2 = "Chatterer said Buster thought the tree was tall".split()


# In[ ]:


rd_parser2 = nltk.RecursiveDescentParser(grammar2)


# In[ ]:


for tree in rd_parser2.parse(sent2):
    print(tree)


# In[ ]:


from nltk.grammar import DependencyGrammar


# In[ ]:


from nltk.parse import DependencyGraph


# In[ ]:


from nltk.parse import ProjectiveDependencyParser


# In[ ]:


from nltk.parse import NonprojectiveDependencyParser


# In[ ]:


groucho_dep_grammar = DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")


# In[ ]:


print(groucho_dep_grammar)


# In[ ]:


sent = "I tried hard for quiz2 in my nlp class"

my_grammar = DependencyGrammar.fromstring("""
'tried' -> 'I' | 'quiz2' | 'for'
'quiz2' -> 'in' | 'for'
'for' -> 'class' | 'hard'
'nlp' -> 'my'
""")

print(my_grammar)

