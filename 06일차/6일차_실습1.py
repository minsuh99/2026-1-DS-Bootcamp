class PartTimer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.work_hours = 0
    
    def work(self, hour):
        self.work_hours += hour
        
    def get_salary(self):
        return self.money * self.work_hours
    
    # "<" 쓸 때 작동하는 메서드
    def __lt__(self, value):
        return self.get_salary() < value.get_salary()

    def __str__(self):
        return f"이름: {self.name} / 근무시간: {self.work_hours}시간 / 급여: {self.get_salary():,}원"


pt_list = []

with open("parttimer.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        name, money, h1, h2, h3 = line.split(",")
        p = PartTimer(name, int(money))
        for h in [h1, h2, h3]:
            p.work(int(h))
        pt_list.append(p)
        
pt_list.sort(reverse=True)

for p in pt_list[:3]:
    print(p)
    