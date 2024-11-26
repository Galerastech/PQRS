from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nit = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    status = Column(String, nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    apartment = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    status = Column(String, nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    tenant = relationship('Tenant', backref='users')



class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    payment_method = Column(String, nullable=False)
    modality = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False, default=func.now())
    end_date = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default='activo')
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    tenant = relationship('Tenant', backref='subscriptions')


