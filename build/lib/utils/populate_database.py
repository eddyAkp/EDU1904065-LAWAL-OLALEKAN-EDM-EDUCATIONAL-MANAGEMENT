"""
This util has the sole purpose of generating and storing randomized (fake)
data into the database. The data will be of the following nature (in no particular order)

    -   * Author -> QuerySet<Author>
            - name (str)

    -   * Information Material (tied to unique 'Author') -> <QuerySet<InformationMaterial>
            - title (str)
            - quan (int)
            - price per unit  (int)
            - Author (Author)

    -   * AudioVisualMaterial (tied to unique 'Author') -> QuerySet<AudioVisualMaterial>
            - Author (Author)

    -   * PrintMediaMaterial (tied to unique 'Author') -> QuerySet(PrintMediaMaterial>
            - ISBN (str)
            - publish date (Date)
            - Author (Author)

    -   * SerialPrintMediaMaterial (tied to unique (Author) -> QuerySet<SerialPrintMaterial>
            - serialization mode (str)
            - serial (str)
"""
import datetime
import random
from typing import NoReturn, Set, Optional, List

from django.db.utils import IntegrityError
from faker import Faker

from resources.models import Author, PrintMediaMaterial, SerialMaterial, AudioVisualMaterial
from resources.models import EDITIONS

faker = Faker()
AUTHORS: List[Optional[Author]] = []


def gen_issn() -> str:
    """Generate ISSN -> International Standard Serial Number"""
    return ''.join([str(random.SystemRandom().randint(0, 9)) for i in range(4)]) + "-" + ''.join(
        [str(random.SystemRandom().randint(0, 9)) for i in range(4)])


def gen_publish_date() -> datetime.date:
    return datetime.date(
        day=random.SystemRandom().randint(1, 28),
        month=random.SystemRandom().randint(1, 12),
        year=random.SystemRandom().randint(1890, datetime.date.today().year))


def generate_authors(quan: int = random.SystemRandom().randint(10, 50)) -> NoReturn:
    """
    Given quan create and save {quan} number of random Authors.
    If quan isn't supplied, a random quan from 10 to 50 (inclusive)
    serves as quan instead.

    If a quan of 0 (zero) is supplied, a default of 1 would be used as quan.
    """
    global AUTHORS

    if not quan: quan = 1
    authors: Set[str] = {faker.name() for i in range(quan)}
    for i in authors: AUTHORS.append(Author.objects.create(name=i))


def generate_audiovisual_materials(quan: int = random.SystemRandom().randint(10, 50)) -> NoReturn:
    """
    Given quan create and save {quan} number of random Authors.
    If quan isn't supplied, a random quan from 10 to 50 (inclusive)
    serves as quan instead.

    [Stock] Quantity is a random value from 1 to 1000 (inclusive)
    Price per unit is a random value from 250 to 23,000 (inclusive)

    if a quan of 0 (zero) is supplied, a default of 1 would be used a quan
    """
    if not quan: quan = 1
    titles: Set[str] = {faker.sentence(nb_words=random.SystemRandom().randint(3, 7))[:-1] for i in range(quan)}
    for t in titles:
        try:
            AudioVisualMaterial.objects.create(
                title=t,
                author=(lambda: random.SystemRandom().choice(AUTHORS))(),
                quantity=(lambda: random.SystemRandom().randint(1, 1000))(),
                price_per_unit=(lambda: random.SystemRandom().randint(250, 23000))())
        except IntegrityError: continue


def generate_printed_media_materials(quan: int = random.SystemRandom().randint(10, 50)) -> NoReturn:
    """
    Given quan create and save {quan} number of random Authors.
    If quan isn't supplied, a random quan from 10 to 50 (inclusive)
    serves as quan instead.

    [Stock] Quantity is a random value from 1 to 1000 (inclusive)
    Price per unit is a random value from 250 to 23,000 (inclusive)

    if a quan of 0 (zero) is supplied, a default of 1 would be used a quan
    """
    if not quan: quan = 1
    isbns = {faker.isbn10() for i in range(quan)}
    for s in isbns:
        try:
            PrintMediaMaterial.objects.create(
                title=(lambda: faker.sentence(nb_words=random.SystemRandom().randint(3, 7))[:-1])(),
                author=(lambda: random.SystemRandom().choice(AUTHORS))(),
                ISBN=s,
                publish_date=gen_publish_date(),
                quantity=(lambda: random.SystemRandom().randint(1, 1000))(),
                price_per_unit=(lambda: random.SystemRandom().randint(250, 23000))(),
                edition=(lambda: random.SystemRandom().choice(EDITIONS)[0])()
            )
        except IntegrityError: continue


def generate_serial_materials(quan: int = random.SystemRandom().randint(10, 50)) -> NoReturn:
    """
    Given quan create and save {quan} number of random Authors.
    If quan isn't supplied, a random quan from 10 to 50 (inclusive)
    serves as quan instead.

    [Stock] Quantity is a random value from 1 to 1000 (inclusive)
    Price per unit is a random value from 250 to 23,000 (inclusive)

    if a quan of 0 (zero) is supplied, a default of 1 would be used a quan
    """
    if not quan: quan = 1
    issns = {gen_issn() for i in range(quan)}
    for s in issns:
        try:
            SerialMaterial.objects.create(
                title=(lambda: faker.sentence(nb_words=random.SystemRandom().randint(3, 7))[:-1])(),
                author=(lambda: random.SystemRandom().choice(AUTHORS))(),
                publish_date=gen_publish_date(),
                ISSN=s,
                issue_number=(lambda: random.SystemRandom().randint(1, 1000))(),
                quantity=(lambda: random.SystemRandom().randint(1, 1000))(),
                price_per_unit=(lambda: random.SystemRandom().randint(250, 23000))(),
                volume_number=(lambda: random.SystemRandom().randint(1, 500))())
        except IntegrityError:
            continue


def execute(quan: int):
    generate_authors(quan)
    generate_audiovisual_materials(quan)
    generate_printed_media_materials(quan)
    generate_serial_materials(quan)
