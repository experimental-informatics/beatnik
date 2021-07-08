Beatnik
===========
This python package contains functions for stack-based esoteric programming language: Beatnik
---

Description
-----------
[Beatink] is a stack-based esoteric programming language created by Cliff L. Biffle.
This package contains each ACTION functions by the rules of beatnik, and build a stack to calculate the resulted output from the given text.

<pre>
Scrabble letter values
--- ABCDEFGHIJKLMNOPQRSTUVWXYZ ---
 1: A---E---I--L-NO--RSTU-----
 2: ---D--G-------------------
 3: -BC---------M--P----------
 4: -----F-H-------------VW-Y-
 5: ----------K---------------
 6: --------------------------
 7: --------------------------
 8: ---------J-------------X--
 9: --------------------------
10: ----------------Q--------Z
--- ABCDEFGHIJKLMNOPQRSTUVWXYZ ---
</pre>
---
Action list

<p align="center">
  <img src="action_table.png"  width="500" >
</p>

---
Installation
------------

The Blend Modes package can be installed through pip:
```sh
pip install beatnik
```


Import
-----

```python
from beatnik import beatnik_simple
from beatnik import beatnik_stack
```


Usage
------------
Use the library directly on Jupyter lab
-----
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/experimental-informatics/beatnik/HEAD)

Use the example file beatnik_interact
-----
Simple usage of this library
```python
text = "this is a line of text"
beatnik.beatnik_simple(text,debug=True)
```
---

Step-by-step

preprocess text
```python
text = "this is a line of text"
words = beatnik.preprocess(text)
```


scrabbling word
------------
```python
beatnik.scrabble(words)
```
`words` are list of words that before scrabble


running stack machine
------------
```python
beatnik.stack(words,VALUE,debug=False)
```


License
-------------
The Beatnik package is distributed under the [MIT License (MIT)](https://github.com/experimental-informatics/beatnik/blob/master/LICENSE.txt). Please also take note of the licenses of the dependencies.

   [Beatink]: <https://esolangs.org/wiki/Beatnik>