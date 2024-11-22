from db import Session, Tour


def add_tour(country, price):
    with Session() as session:
        tour = Tour(country=country, price=price)
        session.add(tour)
        session.commit()
        session.refresh(tour)
        return tour.id


def get_tours():
    with Session() as session:
        return session.query(Tour).all()


def get_tour(id):
    with Session() as session:
        return session.query(Tour).where(Tour.id == id).first()


def update_tour(id, country, price):
    with Session() as session:
        tour = session.query(Tour).filter_by(id=id).first()
        tour.country = country
        tour.price = price
        session.commit()
        return "Дані оновлено"


def delete_tour(id):
    with Session() as session:
        tour = session.query(Tour).filter_by(id=id).first()
        session.delete(tour)
        session.commit()
        return "Подорож видалена"