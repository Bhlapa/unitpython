from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.search_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuario Adicionado"
                else:
                    return "Usuario não adicionado - usuario já existe"
            else:
                return "Usuario não adicionado - algumas das variaveis nao sao str"
        else:
            return "Usuario não adicionado - informações nao podem nulas"

    def remove_user(self, name, job):
        if name is not None and job is not None:
             if isinstance(name, str) and isinstance(job, str):
                for user in self.store.bd:
                    if user.name == name and user.job == job:
                        self.store.bd.remove(user)
                        return "Usuario removido"
                return "Usuario não existe"
             else:
                return "Usuario não removido - algumas das variaveis nao sao str"
        else:
            return "Usuario não removido - informações nao podem nulas"

    def search_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def update_user(self,name,job, newname, newjob):
         if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                for user in self.store.bd:
                    if user.name == name and user.job == job:
                        user.name = newname
                        user.job = newjob
                        return "Usuario modificado"
                return "Usuario nao encontrado"
            else:
                return "Usuario não modificado - algumas das variaveis nao sao str"
         else:
             return "Usuario não modificado - informações nao podem nulas"


