from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from base import Base



class Train(Base):
    __tablename__ = 'train'
    id_train = Column('id_train', Integer, primary_key=True, autoincrement=True)
    departure_time = Column('departure_time', Date)
    arrival_time = Column('arrival_time', Date)
    route = Column('route', String(100))
    train_railcar = relationship('Railcar', cascade='delete-orphan')

    def __repr__(self):
        return "<Train(id_train='{}', departure_time='{}', arrival_time='{}', route='{}')>".format(self.id_train,
                                                                                                   self.departure_time,
                                                                                                   self.arrival_time,
                                                                                                   self.route)


class Railcar(Base):
    __tablename__ = 'railcar'
    id_railcar = Column('id_train', Integer, primary_key=True, autoincrement=True)
    type_railcar = Column('type_railcar', String(50))
    year_start_use_railcar = Column('year_start_use_railcar', Date)
    train = Column('train', Integer, ForeignKey('Train.id_train', onupdate='cascade'), primary_key=True)
    railcar_ticket = relationship('Ticket', cascade='delete-orphan')

    def __repr__(self):
        use_railcar = self.year_start_use_railcar
        return "<Railcar(id_railcar='{}', type_railcar='{}', year_start_use_railcar='{}')>".format(self.id_railcar,
                                                                                                   self.type_railcar,
                                                                                                   use_railcar
                                                                                                   )


class Ticket(Base):
    __tablename__ = 'ticket'
    id_ticket = Column('id_ticket', Integer, primary_key=True, autoincrement=True)
    cost = Column('cost', Integer)
    seat_in_the_train = Column('seat_in_the_train', Integer)
    material = Column('material', String(50))
    railcar = Column('railcar', Integer, ForeignKey('Railcar.id_railcar', onupdate='cascade'), primary_key=True)

    def __repr__(self):
        ticket = self.id_ticket
        cost = self.cost
        seat = self.seat_in_the_train
        material = self.material
        return "Ticket(id_ticket='{}', cost='{}', seat_in_the_train='{}', material='{}'".format(ticket,
                                                                                                cost,
                                                                                                seat,
                                                                                                material)


def get_class_by_tablename(tablename):
    for _class in [Ticket, Railcar, Train]:
        if hasattr(_class, '__tablename__') and _class.__tablename__ == tablename:
            return _class


def get_attr_name_of_class(table_name):
    return [attr.name for attr in dir(get_class_by_tablename(table_name)) if isinstance(attr, Column)]

