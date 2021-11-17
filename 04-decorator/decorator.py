import os


# Definindo nosso decoradora
def tem_git(funcao):
    def escrava():
        if os.path.isdir(".git"):
            funcao()
        else:
            print('Tem não')
    return escrava()

@tem_git
def fala_se_tem():
    print("Tem simmm, Wheeeee!!")