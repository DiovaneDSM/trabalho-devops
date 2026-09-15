from src.main import *
from unittest.mock import patch



def test_root():
    assert root() == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', return_value=98765):
        result = funcaoteste()
    assert result == {"teste": True,
            "num_aleatorio": 98765}


def test_create_estudante():
    estudante_teste = Estudante(name="Diovane", curso="DevOps", ativo=True)
    assert estudante_teste == create_estudante()


def test_update_estudante_negative():
    assert not update_estudante(-5)


def test_update_estudante_positive(id_estudante: int):
    assert update_estudante(5)


def test_delete_estudante_negative():
    assert not delete_estudante(-5)


def test_delete_estudante_positive():
    assert delete_estudante(5)
