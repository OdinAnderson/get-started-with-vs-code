"""Module for managing person data and visualizations."""

from typing import List
import matplotlib.pyplot as plt
import pandas as pd


class Person:
    """A class to represent a person with various attributes."""

    def __init__(
        self,
        name: str,
        age: int,
        email: str,
        phone: str,
        address: str,
        city: str,
        country: str,
        postal_code: str,
        occupation: str,
        company: str,
        salary: float,
    ) -> None:
        """Initialize a new Person instance."""
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.occupation = occupation
        self.company = company
        self.salary = salary

    def __repr__(self) -> str:
        """Return a string representation of the Person instance."""
        return (
            f"Person(name={self.name}, age={self.age}, email={self.email}, "
            f"phone={self.phone}, address={self.address}, city={self.city}, "
            f"country={self.country}, postal_code={self.postal_code}, "
            f"occupation={self.occupation}, company={self.company}, "
            f"salary={self.salary})"
        )


# Sample data
people = [
    Person("Alice Johnson", 30, "alice.johnson@example.com", "123-456-7890", "123 Maple St", "Springfield", "USA", "12345", "Engineer", "TechCorp", 85000.0),
    Person("Bob Smith", 45, "bob.smith@example.com", "234-567-8901", "456 Oak St", "Shelbyville", "USA", "67890", "Teacher", "High School", 55000.0),
    Person("Charlie Brown", 28, "charlie.brown@example.com", "345-678-9012", "789 Pine St", "Capital City", "USA", "11223", "Designer", "Creative Inc", 62000.0),
    Person("Diana Prince", 35, "diana.prince@example.com", "456-789-0123", "321 Elm St", "Metropolis", "USA", "44556", "Doctor", "City Hospital", 120000.0),
    Person("Ethan Hunt", 40, "ethan.hunt@example.com", "567-890-1234", "654 Cedar St", "Gotham", "USA", "77889", "Agent", "IMF", 95000.0),
    Person("Fiona Gallagher", 29, "fiona.gallagher@example.com", "678-901-2345", "987 Birch St", "Riverdale", "USA", "33445", "Chef", "Gourmet Kitchen", 48000.0),
    Person("George Bailey", 50, "george.bailey@example.com", "789-012-3456", "159 Spruce St", "Bedford Falls", "USA", "55667", "Banker", "Savings & Loan", 75000.0),
    Person("Hannah Montana", 22, "hannah.montana@example.com", "890-123-4567", "753 Willow St", "Nashville", "USA", "66778", "Singer", "Music Studio", 100000.0),
    Person("Ian Malcolm", 47, "ian.malcolm@example.com", "901-234-5678", "357 Redwood St", "Jurassic Park", "USA", "77889", "Mathematician", "Chaos Theory Lab", 110000.0),
    Person("Jane Doe", 33, "jane.doe@example.com", "012-345-6789", "951 Aspen St", "Smallville", "USA", "88990", "Journalist", "Daily Planet", 68000.0)
]


def plot_age_vs_salary(people: List[Person]) -> None:
    """Plot a scatter plot comparing people's ages to their salaries."""
    ages = [person.age for person in people]
    salaries = [person.salary for person in people]

    plt.figure(figsize=(10, 6))
    plt.scatter(ages, salaries, color='blue', alpha=0.7)
    plt.title("Age vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary ($)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def create_dataframe(people: List[Person]) -> pd.DataFrame:
    """Convert list of Person objects to a pandas DataFrame."""
    return pd.DataFrame(
        {
            "Name": [p.name for p in people],
            "Age": [p.age for p in people],
            "Email": [p.email for p in people],
            "Phone": [p.phone for p in people],
            "Address": [p.address for p in people],
            "City": [p.city for p in people],
            "Country": [p.country for p in people],
            "Postal Code": [p.postal_code for p in people],
            "Occupation": [p.occupation for p in people],
            "Company": [p.company for p in people],
            "Salary": [p.salary for p in people],
        }
    )


def main() -> None:
    """Display person data and visualizations."""
    df = create_dataframe(people)
    pd.set_option('display.max_columns', None)
    print(df)
    plot_age_vs_salary(people)


if __name__ == "__main__":
    main()

