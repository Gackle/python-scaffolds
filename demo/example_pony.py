from pony import orm  # type: ignore


@orm.db_session
def get_wxpay_order():
    result = db.select("* FROM T_WXPAY_ORDER")
    return result


if __name__ == "__main__":
    orm.set_sql_debug(True)
    db = orm.Database()
    db.bind(
        provider="oracle",
        user="huangjh82",
        password="U41#9_7B",
        dsn="132.98.25.72:1521/gzcent",
    )
    print(get_wxpay_order())
