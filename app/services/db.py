from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("sqlite:///integration_hub.db", echo=False)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
