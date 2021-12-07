import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

a = 10

test = logging.basicConfig(filename="app.log", level=logging.DEBUG, filemode='w',format=LOG_FORMAT , encoding="utf-8")
log = logging.getLogger()
log.info("Olá Tião")
log.critical("Erro grave")
log.debug("Testando retorno da variável 'a' = {}".format(a))
log.warning("Módulo depreciado, atualize pelo PIP o módulo.")
log.error("Erro de execução")

