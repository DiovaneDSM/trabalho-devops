from src.main import *
from unittest.mock import patch

import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=98765):
        result = await funcaoteste()
    assert result == {"teste": "deu certo", "num_aleatorio": 98765}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Diovane", curso="DevOps", ativo=True)
    result= await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negative():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positive():
    result = await update_estudante(5)
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negative():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positive():
    result = await delete_estudante(5)
    assert result
