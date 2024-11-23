from src.service.service_user import ServiceUser


class TestServiceUser:


    #Testes de Add
    def test_add_user_success(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuario Adicionado"

        #Chamada
        resultado = service.add_user("Bhl", "Eng")

        #Avalicação
        assert resultado == resultado_esperado

    def test_add_user_fail(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não adicionado - usuario já existe"

        # Chamada
        service.add_user("Bhl", "Eng")
        resultado = service.add_user("Bhl", "Eng")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_user_falha_str_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não adicionado - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.add_user(1, "Eng")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_user_falha_str_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não adicionado - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.add_user("Bhl", 1)

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_user_falha_none_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não adicionado - informações nao podem nulas"

        # Chamada
        resultado = service.add_user(None, "job")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_user_falha_none_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não adicionado - informações nao podem nulas"

        # Chamada
        resultado = service.add_user("Bhl", None)

        # Avalicação
        assert resultado == resultado_esperado


    #Testes de Remove
    def test_remove_user_falha_str_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não removido - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.remove_user(1, "Eng")

        # Avalicação
        assert resultado == resultado_esperado

    def test_remove_user_falha_str_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não removido - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.remove_user("Bhl", 1)

        # Avalicação
        assert resultado == resultado_esperado

    def test_remove_user_falha_none_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não removido - informações nao podem nulas"

        # Chamada
        resultado = service.remove_user(None, "job")

        # Avalicação
        assert resultado == resultado_esperado

    def test_remove_user_falha_none_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não removido - informações nao podem nulas"

        # Chamada
        resultado = service.remove_user("Bhl", None)

        # Avalicação
        assert resultado == resultado_esperado

    def test_remove_user_success(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuario removido"

        #Chamada
        service.add_user("Bhl","Eng")
        resultado = service.remove_user("Bhl", "Eng")

        #Avalicação
        assert resultado == resultado_esperado

    def test_remove_user_fail(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não existe"

        #Chamada
        service.add_user("Bhl","Eng")
        resultado = service.remove_user("Bhlj", "Eng")

        #Avalicação
        assert resultado == resultado_esperado


    #Testes de Update

    def test_update_user_success(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario modificado"

        # Chamada
        service.add_user("Bhl", "Eng")
        resultado = service.update_user("Bhl", "Eng","Bhl2","Eng2")

        # Avalicação
        assert resultado == resultado_esperado

    def test_update_user_fail_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario nao encontrado"

        # Chamada
        service.add_user("Bhl", "Eng")
        resultado = service.update_user("Bhj", "Eng", "Bhl2", "Eng2")

        # Avalicação
        assert resultado == resultado_esperado

    def test_update_user_fail_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario nao encontrado"

        # Chamada
        service.add_user("Bhl", "Eng")
        resultado = service.update_user("Bhl", "Enj", "Bhl2", "Eng2")

        # Avalicação
        assert resultado == resultado_esperado


    def test_update_user_falha_str_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não modificado - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.update_user(1, "Eng","Bhl","Eng")

        # Avalicação
        assert resultado == resultado_esperado

    def test_update_user_falha_str_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não modificado - algumas das variaveis nao sao str"

        # Chamada
        resultado = service.update_user("Bhl", 1,"Bhl","job")

        # Avalicação
        assert resultado == resultado_esperado

    def test_update_user_falha_none_job(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não modificado - informações nao podem nulas"

        # Chamada
        resultado = service.update_user("Bhl", None, "Bhl2", "Eng2")

        # Avalicação
        assert resultado == resultado_esperado

    def test_update_user_falha_none_name(self):
        # Setup
        service = ServiceUser()
        resultado_esperado = "Usuario não modificado - informações nao podem nulas"

        # Chamada
        resultado = service.update_user(None, "Eng", "Bhl2","Eng2")

        # Avalicação
        assert resultado == resultado_esperado







    
