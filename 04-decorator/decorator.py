import os


# Definindo nosso decoradora
def tem_git(funcao):
    def sub_func():
        if os.path.isdir(".git") in ('C:\Users\joshu\Github\mentoria-dell-lead'):
            funcao()
        else:
            print('Tem não')
    return sub_func()

@tem_git
def fala_se_tem():
    print("Tem simmm, Wheeeee!!")