import logging

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--logs",
        action="store",
        default="true",
        help="enter logs",
    )


@pytest.fixture(autouse=True, scope="session")
def logger(request):
    logger = logging.getLogger()
    logs = request.config.getoption("--logs")
    if logs == "True":
        logger.setLevel(10)
    elif logs == "False":
        logger.setLevel(50)
    return logger


@pytest.fixture(autouse=True, scope="session")
def test_logger(request, logger):
    logger.info("\nНачало тестовой сессии")
    yield
    logger.info("Конец тестовой сессии \n")


@pytest.fixture(autouse=True)
def session_logger(request, logger):
    logger.info(f" \n + Начало теста - {request.node.nodeid}")
    yield
    logger.info(f"Конец теста - - {request.node.nodeid} \n")

