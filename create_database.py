import json

import commit as commit
from sqlalchemy.orm import session

from models.database import create_db, Session
from models.service import Service
from models.users import Users
from models.record import Record
from models.relation import Relation


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_service_data(session: Session):
    with open('data/nail_services.json', encoding='utf-8') as f:
        nail_services = json.load(f)

    for service in nail_services['services']:
        name = service['name']
        price = service['price'] if 'price' in service else None
        price_from = service['price_from'] if 'price_from' in service else None
        price_to = service['price_to'] if 'price_to' in service else None
        session.add(Service(name_service=name, price=price, price_from=price_from, price_to=price_to))

    session.commit()


def _load_relation_data(session: Session):
    with open('data/nail_relations.json', encoding='utf-8') as f:
        nail_relation = json.load(f)

    for relation in nail_relation['relations']:
        parent_id = relation['parent_id']
        child_id = relation['child_id']
        session.add(Relation(parent_id=parent_id, child_id=child_id))
    session.commit()


def _load_fake_data(session: Session):
    _load_service_data(session)
    _load_relation_data(session)
    session.close()
