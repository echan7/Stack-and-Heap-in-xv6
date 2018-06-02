# first attempt 1024 * 160 integers - xv6 ran out of space
# Bra, I'm getting super good at big data file testing
# this only took like 3 hours and uhhh... 30ish lines of python code
# but the printer output isn't as good as Zev's...
# woo hoo Jade aggro shaman rocks bra
# RANK 11 - why is this here?!?!

f = open("lots.c", 'w')

f.write('#include \"types.h\"\n#include \"stat.h\"\n#include \"user.h\"\n')
f.write('int\nmain(int argc, char *argv[])\n{\n')

for idx in range(1,157):
    var = '_'
    var += str(idx)

    f.write('    int {}[1024];\n'.format(var))

f.write('    int i;\n    for(i = 0; i < 1024; i++)\n')
f.write('    {\n')

for idx in range(1,157):
    var = '_'
    var += str(idx)
    f.write('        {}[i] = 1;\n'.format(var))
    f.write('        {}[i]++;\n'.format(var))

f.write('    }\n')

f.write('exit();\n}')
