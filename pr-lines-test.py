import socket 

s = socket.socket(doesnt, matter)

5 == 5
6 == 6

# ruleid:avoid-bind-to-all-interfaces
s = socket.socket(doesnt, matter)
s.bind(('0.0.0.0', 1337))

# # ruleid:avoid-bind-to-all-interfaces
# s = socket.socket(doesnt, matter)
# s.bind(('::', 1337))

# # ruleid:avoid-bind-to-all-interfaces
# s = socket.socket(doesnt, matter)
# s.bind(('',))
