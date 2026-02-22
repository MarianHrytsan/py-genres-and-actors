import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    actor_tuple = ("George Klooney", "Kianu Reaves", "Scarlett Keegan", "Will Smith", "Jaden Smith", "Scarlett Johansson")
    genre_tuple = ("Western", "Action", "Dramma")
    for genre in genre_tuple:
        Genre.objects.create(name=genre)
    for actor in actor_tuple:
        Actor.objects.create(first_name=actor.split(" ")[0], last_name=actor.split(" ")[1])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlet").delete()
    return Genre.objects.filter(last_name="Smith").order_by("first_name")
