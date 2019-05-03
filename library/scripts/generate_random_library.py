#!/usr/bin/env python
# Script that generates some fake data for our library
import os, sys

sys.path.append(os.getcwd())
import django

django.setup()
import random

from django.utils import timezone

from stacks.models import Author, Book, LoanedBook
from libraryusers.models import LibraryUser

from faker import Factory

fake = Factory.create()

from datetime import date, timedelta

NUM_AUTHORS = 200
NUM_BOOKS = 500
NUM_PATRONS = 150
checkout_days = [(date.today() - timedelta(days=x)) for x in range(21)]

# Create a series of fake authors; also create at least one book for each author
for x in range(NUM_AUTHORS):
    author = Author.objects.create(first_name=fake.first_name(), last_name=fake.last_name())
    try:
        b = Book.objects.create(
            call_number=fake.numerify(text="###.###"),
            page_count=fake.random_int(min=10, max=1001),
            title=" ".join(fake.words(nb=fake.random_int(1, 6))).title(),
        )
        b.authors.add(author)
        b.save()
    except:
        pass

authors = Author.objects.all()
for x in range(NUM_BOOKS):
    author_set = set()
    for y in range(fake.random_int(1, 3)):
        author_set.add(random.choice(authors))
    try:
        b = Book.objects.create(
            call_number=fake.numerify(text="###.###"),
            page_count=fake.random_int(min=10, max=1001),
            title=" ".join(fake.words(nb=fake.random_int(1, 6))).title(),
        )
        for author in author_set:
            b.authors.add(author)
        b.save()
    except:
        pass

books = list(Book.objects.all())
random.shuffle(books)
# Create a bunch of users and loan books to them
for x in range(NUM_PATRONS):
    user_profile = fake.simple_profile()
    user = LibraryUser.objects.create(
        username=user_profile["username"],
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=user_profile["mail"],
        is_staff=False,
        is_active=True,
        birthdate=user_profile["birthdate"],
        gender=user_profile["sex"],
        last_login=timezone.now(),
    )
    for x in range(fake.random_int(1, 5)):
        book = books.pop()
        checkout_date = random.choice(checkout_days)
        due_date = checkout_date + timedelta(days=14)
        LoanedBook.objects.create(patron=user, book=book, checkout_date=checkout_date, due_date=due_date)
