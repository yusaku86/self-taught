class Singer:
    def __init__(self):
        self.name = "UVERworld"
uver = Singer()
same_uver = uver
print(uver is same_uver)
another_uver = Singer()
print(another_uver is uver)
print(same_uver.name)
print(another_uver.name) 