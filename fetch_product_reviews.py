from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import snowflake.connector


snowflake.connector.paramstyle = 'qmark'


def main():
    engine = create_engine(URL(
        user='****',
        password='*****',
        account='*****',
        warehouse='GDM',
        database='REPLICON',
        client_session_keep_alive=False,
        schema='XAVIER',
        role='****'
    ))
    connection = engine.connect()
    connection.execute("ALTER SESSION SET TIMEZONE = 'UTC';")

    with open('products.txt', 'r') as fl:
        lines = fl.readlines()
        for line in lines:
            sql = f"select g_product_id.global_product_id, rvw.id, rvw.general_comments, rvw.pros_text, rvw.cons_text " \
                  f"from REPLICON.XAVIER.REVIEWS rvw inner join REPLICON.CAP.PRODUCT_DM_REVIEWS g_product_id " \
                  f" on rvw.id = g_product_id.global_review_id " \
                  f"where g_product_id.global_product_id ='" + line.strip() + "' order by written_on desc limit 5;"
            reviews = connection.execute(sql).fetchall()
            print(line.strip(), len(reviews))
            with open('./reviews/' + line.strip() + '.txt', 'w+') as fl_wr:
                for rvw in reviews:
                    if rvw[2] is not None:
                        fl_wr.write(rvw[2] + "\n")
                    # if rvw[3] is not None:
                    #     fl_wr.write(rvw[3] + "\n")
                    # if rvw[4] is not None:
                    #     fl_wr.write(rvw[4] + "\n")


if __name__ == '__main__':
    main()

