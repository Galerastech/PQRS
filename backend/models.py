
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey,Text,Boolean
from sqlalchemy.orm import relationship
from backend.database import Base


class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    nit = Column(String(20), nullable=False, unique=True)
    address = Column(String(200), nullable=True)
    phone = Column(String(20), nullable=True)
    status = Column(String(20), nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    apartment = Column(Integer, nullable=False)
    phone = Column(String(100), nullable=True)
    is_superadmin = Column(Boolean,nullable=False, default=False)
    status = Column(String(20), nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=True)

    tenant = relationship('Tenant', backref='users')


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    payment_method = Column(String(20), nullable=False)
    modality = Column(String(20), nullable=False)
    start_date = Column(DateTime, nullable=False, default=func.now())
    end_date = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default='activo')
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    tenant = relationship('Tenant', backref='subscriptions')


class Pqrs(Base):
    __tablename__ = 'pqrs'
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    urlfile = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    user = relationship('User', backref='pqrs')
    tenant = relationship('Tenant', backref='pqrs')

class PqrsResponse(Base):
    __tablename__ = 'pqrs_response'
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    urlfile = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default='activo')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    pqrs_id = Column(Integer, ForeignKey('pqrs.id', ondelete='CASCADE'), nullable=False)
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    pqrs = relationship('Pqrs', backref='pqrs_response')
    tenant = relationship('Tenant', backref='pqrs_response')


class Auditories(Base):
    __tablename__ = 'auditories'
    id = Column(Integer, primary_key=True)
    operation = Column(String(200), nullable=False)
    date = Column(DateTime, nullable=False)
    ip = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    tenant = relationship('Tenant', backref='auditories')

class Parameters(Base):
    __tablename__ = 'parametres'
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    parameter = Column(String(20), nullable=False)
    value = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    tenant_id = Column(Integer, ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False)

    tenant = relationship('Tenant', backref='parameters')
