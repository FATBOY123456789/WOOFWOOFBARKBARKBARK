class animal:
    species='dog'
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age
Crentasota=animal('Golden Shepard','1')
print('My pet crentasota is a ',Crentasota.breed,'and he is just turned',Crentasota.age,'year old!')