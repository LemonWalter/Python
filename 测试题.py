# def identifer(fn):
#     def inner(name, game, *args, **kwargs):
#
#         if kwargs.get("clock",24) < 20:
#             fn(name, game)
#         else:
#             print("不可以玩游戏")
#
#     return inner
#
# @identifer
# def play_game(name, game):
#     print("{}在玩{}".format(name,game))
#
# play_game("张三","王者荣耀", clock=19)

def timePlay(fn):
    def inner(name, game, *args, **kwargs):
        if kwargs.get("clock", 24)<22:
            fn(name, game)
        else:
            print("老宋肾虚了,不能玩了")
    return inner

@timePlay
def playGame(name, ganme):
    print("{}在玩{}".format(name, ganme))

playGame("宋忠森","东京热", clock=19)
