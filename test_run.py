
#!/usr/bin/python3

class Me:
    my_att = "Elgibbor"

    def __init__(self, obj_att):
        self.obj_att = obj_att

m = Me('lll')
print(m.obj_att)
jj = Me('kk')
jj.jj_name = "jj_here"
print(jj.jj_name)
print(dir(m))

