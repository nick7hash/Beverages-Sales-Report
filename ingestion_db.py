import pandas as pd
import numpy as np
import logging
import time
from sqlalchemy import create_engine

logging.basicConfig(filename = "log.log", level = logging.INFO, filemode = 'a', format = '%(asctime)s - %(levelname)s - %(message)s' )
engine = create_engine('sqlite:///coffee.db')
df = pd.read_excel("Coffee Shop Sales.xlsx")


def ingestion(df, table_name, engine):
            df.to_sql(table_name, con=engine, if_exists = 'replace', index = False)

def starting():
    try:
        start = time.time()
        logging.info(f"ingestion Started into coffeshop table...")
        ingestion(df, 'coffeshop', engine)
        stop = time.time()
        total_time = stop - start
        logging.info(f"ingestion completed...total time taken is {total_time}")
        print("total time taken is ", total_time)
    except Exception as e:
        logging.error("An error occured : ", e)

if __name__ == "__main__":
    starting()
    