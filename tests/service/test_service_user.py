from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuario Adicionado"

        #Chamada
        resultado = service.add_user("Bhl", "Eng")

        #Avalicação
        assert resultado == resultado_esperado

    def test_add_user_falha_existente(self):
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


    
