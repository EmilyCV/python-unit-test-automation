import pytest

"""
    @pytest.fixture(scope="class")
    - Use o escopo da classe se quiser que o equipamento seja executado em cada classe de testes. 
    Normalmente, você agrupará testes semelhantes em uma classe, então isso pode ser uma boa ideia, 
    dependendo de como você estrutura as coisas.

    - Use o escopo do módulo se quiser que o equipamento seja executado no início do arquivo atual 
    e depois que o arquivo terminar seus testes. Isso pode ser bom se você tiver um fixture que acessa 
    o banco de dados e configurar o banco de dados no início do módulo e, em seguida, 
    o finalizador fechar a conexão.

    - Use o escopo da sessão se quiser executar o equipamento no primeiro teste e executar o finalizador 
    após a execução do último teste.
"""


@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print(f"Fixture Scope: \033[1;31m{str(request.scope)}\033[0;0m")
    print(
        f"Function Name: \033[1;33m{str(request.function.__name__)}\033[0;0m")
    print(f"Class Name: \033[1;36m{str(request.cls)}\033[0;0m")
    print(f"Module Name: \033[0;32m{str(request.module.__name__)}\033[0;0m")
    print(f"File Path: \033[0;34m{str(request.fspath)}\033[0;0m")


@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")
