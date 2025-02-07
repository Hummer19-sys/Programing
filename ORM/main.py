import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules import Publisher, Book, Shop, Stock, Sale, create_tables
from datetime import datetime

DSN = 'postgresql://postgres:123@localhost:5432/test'
engine = create_engine(DSN)
def read_json(file_path):

    Session = sessionmaker(bind=engine)
    session = Session()

    with open(file_path, encoding="utf8") as f:
        json_data = json.load(f)

    for row in json_data:
        if row['model'] == 'publisher':
            publisher = Publisher(
                id= row['pk'],
                name=row['fields']['name']
            )
            session.add(publisher)

        elif row['model'] == 'book':
            book = Book(
                id=row['pk'],
                title=row['fields']['title'],
                id_publisher=row['fields']['id_publisher']
            )
            session.add(book)

        elif row['model'] == 'shop':
            shop = Shop(
                id=row['pk'],
                name=row['fields']['name'],
            )
            session.add(shop)

        elif row['model'] == 'stock':
            stock = Stock(
                id=row['pk'],
                id_book=row['fields']['id_book'],
                id_shop=row['fields']['id_shop'],
                count=row['fields']['count']
            )
            session.add(stock)

        elif row['model'] == 'sale':
            price = float(row['fields']['price'])
            date_sale = datetime.strptime(row['fields']['date_sale'], "%Y-%m-%dT%H:%M:%S.%fZ")
            sale = Sale(
                id=row['pk'],
                price=price,
                date_sale=date_sale,
                count=row['fields']['count'],
                id_stock=row['fields']['id_stock']
            )
            session.add(sale)

    session.commit()
    session.close()

read_json('C:\\Users\\Владислав\\Desktop\\Programing\\ORM\\tests_data.json')




# publisher_data = []
# for row in df.iterrows():
#     print(row)

# publisher_df =
# book_df =
# shop_df =
# stock_df =
# sale_df =