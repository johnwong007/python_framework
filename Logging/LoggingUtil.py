import traceback
import logging
logging.basicConfig(filename='./jsinfo.log', level=logging.DEBUG)

logging.info(traceback.format_exc())