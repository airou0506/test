# 编写一个战士（Warrior）类，内容如下：
# 1，创建类属性生命值上限(life_max)，生命上限值可以不等于生命值
import os
import time
class warrior:
    life_max = 100
# 2, 创建私有实例属性:姓名(name)，生命值(life)，攻击力(ATK)，防御力(DEF)，
# 3, 要求使用有参构造方式，初始化所有属性,如果初始化中生命值大于生命值上限，强制变为生命值上限
    def __init__(self,NAME,LIFE,ATK,DEF):
        self.__NAME = NAME
        
        if LIFE > warrior.life_max:
            self.__LIFE = 100
            self.basiclife = 100
        else:
            self.__LIFE = LIFE 
            self.basiclife = LIFE
        self.__ATK = ATK 
        self.__DEF = DEF
    
# 4，创建实例方法 attack(self,Warrior)， 参数为战士类,功能如下:
    def attack(self,warrior):
# （1）显示谁攻击谁
        print('[{}]攻击[{}]'.format(self.__NAME,warrior.__NAME))
# （2）如果对方生命值少于等于0，显示[XX] 已经挂了，攻击无效！
        if warrior.__LIFE <= 0:
            print('[{}]已经死了,攻击无效\n[{}]胜利,战斗结束'.format(warrior.__NAME,self.__NAME))
            os._exit(0)

# （3）如果对方生命值大于0，计算伤害，攻击力减去防御力等于最终伤害，如果最终伤害少于等于0 则显示[xx]没有受到伤害
        else:
            lost_life = self.__ATK - warrior.__DEF
            if lost_life <= 0:
                print('[{}]没有受到伤害'.format(warrior.__NAME))
                            
# (4) 显示剩余生命值，生命值等于现有生命值减去最终伤害，如果最终伤害大于生命值，显示[XX]已经挂了
            elif lost_life > warrior.__LIFE:
                print('[{}]受到了{}伤害,已经死了\n战斗结束,[{}]获胜'.format(warrior.__NAME,lost_life,self.__NAME))
                os._exit(0)
# （5）每次攻击以后，对方的类属性生命值相应发生改变，保留伤害后的生命值
            else:
                warrior.__LIFE -= lost_life
                print('[{}]受到了{}伤害,生命值剩余{}/{}'.format(warrior.__NAME,lost_life,warrior.__LIFE,warrior.basiclife))
    def show(self):
        print('[{}]血量:{},攻击力{},防御力{}'.format(self.__NAME,self.__LIFE,self.__ATK,self.__DEF))
    def awaken(self,name,life,atk,DEF):
        self.__NAME = name 
        self.__LIFE = life 
        self.__ATK = atk 
        self.__DEF = DEF
        self.basiclife = life
    def getName(self):
        return self.__NAME

if __name__ == "__main__":
    airou = warrior('airou',100,51,30)
    aim = warrior('aim',100,70,50)
    list = [airou,aim]
    for warrior in list:
        warrior.show()
    while True:
        changeflag = True
        attack_act = list[0]
        defend_act = list[1]
        print('现在是[{}]的回合'.format(attack_act.getName()))
        print('1.攻击\n2.展示双方状态\n3.觉醒\n4.逃跑')
        do = input('请输入指令')
        if do == '1':
            attack_act.attack(defend_act)
        elif do == '2':
            attack_act.show()
            defend_act.show()
            changeflag = False
        elif do == '3':
            attack_act.awaken(attack_act.getName()+'max',200,255,250)
        elif do == '4':
            print('[{}]逃跑成功,战斗结束,胜利者为[{}]'.format(attack_act.getName(),defend_act.getName()))
            os._exit(0)
        else:
            print('未找到指令,请重新输入')
            changeflag = False
        if changeflag == True:
            list = list[::-1]
        time.sleep(1)  
    print('吴泽杰,339005200008220319,2020-03-30')