from logzero import logger, logfile, loglevel



loglevel(1)

def foo():


    
    logfile("/home/kaktus74/nasze_logi.log")

    for i in range(1,100):

        logger.debug("SUper szczegolowe informacje")
        logger.info("Cos siw wydarzylo!")
        logger.warning("Chyba cos sie wywrocilo")
        logger.error("Oj, cos sie na pewno wywrocilo!")
        rok = 19
        logger.critical(f"Wykryto wirusa covid-{rok}! {i}")

if __name__ == '__main__':
    foo()
