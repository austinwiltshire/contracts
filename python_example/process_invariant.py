

...
items = [x for x in the_list if x > 20]
#process invariant
assert len(items) == 1, "There should be only one item more than 20"
...
