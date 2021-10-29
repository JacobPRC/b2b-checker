# Okay, so we got 2 options for checking this. We can do a binary search to compare 2 lists
# w/ a time complexity of log N, or we can form a list. Nevermind, that's the best option. If I
# converted the list into a dict, we could search through dict with linear complexity, but in
# order to do that I'd need to loop through all items in a list, which has o(n) complexity
