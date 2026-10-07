# # from sqlalchemy.orm import DeclarativeBase,sessionmaker
# # from app.db.database import engine
# # class Base(DeclarativeBase):
# #     pass

# # sessionlocal=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)
# # def get_db():
# #     db=sessionlocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# from sqlalchemy.orm import DeclarativeBase,sessionmaker
# from app.db.database import engine

# class   Base(DeclarativeBase):
#     pass

# sessionlocal=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)

# def get_db():
#     db=sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()


from sqlalchemy.orm import DeclarativeBase,sessionmaker
from app.db.database import engine

class Base(DeclarativeBase):
    pass

sessionlocal=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()