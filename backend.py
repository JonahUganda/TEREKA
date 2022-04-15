from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker






class panda_csv1:
    pass


class commandbase:
    pass


class datacon:

    def __init__(self):
        self.database_setput()

    def database_setput(self):

        self.engine = create_engine('sqlite:///shopdatabase.db', echo=True)
        self.meta = MetaData()

        self.students = Table(
            'Prouct_details', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Prouct_name', String),
            Column('Whole_sale_price', String),
            Column('Retail_price', String),
            Column('Quantity', String),
            Column('supplier_contact', String),
            Column('registration_date', String),

        )
        self.sold_products = Table(
            'sold_products ', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Prouct_name', String),
            Column('quantity', Integer),
            Column('unit_product', Integer),
            Column('subtotal', Integer),
            Column('sold_by', String)
        )
        self.admin_users1 = Table(
            'admin_users1', self.meta,
            Column('id', Integer, primary_key=True),
            Column('User_ID',String),
            Column('User_passwords', String),

        )
        self.registered_users = Table(
            'admin_users', self.meta,
            Column('id', Integer, primary_key=True),
            Column('First_name', String),
            Column('Last_name', String),
            Column('Email', String),
            Column('Phone_num', String)),

        self.new_commodity= Table(
            'new_commodity', self.meta,
            Column('id', Integer, primary_key=True),
            Column('Prouct_name', String),
            Column('Whole_sale_price', String),
            Column('Retail_price', String),
            Column('Quantity', String),
            Column('Supplier_contact', String),


        )



        self.meta.create_all(self.engine)

    def reg_new_commodity(self,a,b,c,d,e):
        self.a1 = a
        self.b1 = b
        self.c1 = c
        self.d1 = d
        self.e1 = e

        self.ins = self.new_commodity.insert()
        self.ins = self.new_commodity.insert().values(

            Prouct_name=self.a1,
            Whole_sale_price=self.b1,
            Retail_price=self.c1,
            Quantity=self.d1,
            Supplier_contact=self.e1,


        )
        self.conn = self.engine.connect()
        self.result = self.conn.execute(self.ins)





    def view_newcomt_d(self):
        self.s =  self.new_commodity.select()
        self.conn = self.engine.connect()

        self.Session=sessionmaker(bind=self.engine)
        self.session= self.Session()
        self.result = self.session.query(self.new_commodity).all()
        print(f"anti obi")
        print(self.result)


        return self.result
