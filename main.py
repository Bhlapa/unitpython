from src.service.service_user import ServiceUser

service = ServiceUser()
resultado = service.add_user("bhl","eng")
print(resultado)
print(service.store.bd[0].name)
resultado2 = service.update_user("bhl","eng","bhl2","eng2")
print(resultado2)
print(service.store.bd[0].name)
