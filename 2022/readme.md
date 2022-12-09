# Lessons learned


## Listen
- Elemente löschen mit `del stack[index]`, z.B. für das letzte Item: `del stack[-1]`.
- Element am Ende einfügen: `stack.append(item)`
- Elemten an bestimmten Index einfügen (Rest rückt weiter nach hinten): `stacks.insert(index, item)`
- Mehrdimensionale Listen können so angelegt werden:
    ```python
    stacks = [[],[],[]]
    # len(stacks)    --> 3
    # len(stacks[0]) --> 0
    ```
- oder auch in Schleifen:
    ```python
    while len(stacks) < 9:
        stacks.append([])
    ```
- Anzahl Vorkommen mit z.B. `amount = stream.count(char)`


## Zugriff auf Dateien zuverlässig implementieren
Je nachdem wie ein Python-Skript ausgeführt wird, ist der aktuelle Ausführungort unterschiedlich (z.B. Quellordner dieses Repos vs. Unterordner wie 2022). Das führt zu Error2: File not found.

Ein Lösungsansatz von [stackoverflow](https://stackoverflow.com/a/4060259):
```python
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
 
 # und anschließend Dateien öffnen mit:
 with open(os.path.join(__location__, '5_input_stacks.txt')) as input_file:
```