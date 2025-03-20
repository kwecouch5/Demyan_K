class Tyson:
    def __init__(self,weight=100,hight=178,fat=20,impact_force=700):
        self.weight=weight
        self.hight=hight
        self.fat=fat
        self.impact_force=impact_force
    def __str__(self):
        s= f'Вес={self.weight},Рост={self.hight}'
        return s
    def index_hw(self):
        hig=self.hight/100
        index_t=self.weight/hig**2
        return index_t
    def fat_pr(self):
        fat_pr=self.fat/self.weight
        return fat_pr
    def type_tyson(self):
        a_in_hw=self.index_hw()
        if a_in_hw<=16:
            return 0
        b_fat_pr=self.fat_pr()
        if b_fat_pr>=45:
            return 0
        summ=self.impact_force
        summ+=a_in_hw*50-b_fat_pr*35+((self.hight-170)*35)
        return summ
Tyson1=Tyson(100,170,10,1200)
Tyson2=Tyson(100,178,15,1000)
a=Tyson1.type_tyson()
b=Tyson2.type_tyson()
def Tysons_fight(Tyson1_type,Tyson2_type):
    Tyson1=''
    Tyson2=''
    if Tyson1_type>Tyson2_tupe:
        Tyson1 = 'win'
        Tyson2 = 'lose'
    else:
        Tyson2 ='win'
        Tyson1 ='loss'
    print('Tyson1',Tyson1,'Tyson2',Tyson2)
    return Tyson1,Tyson2
print(Tysons_fight(a,b))