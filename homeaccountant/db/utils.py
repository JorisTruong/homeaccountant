from dataclasses import dataclass

@dataclass
class User:
    email: str = None
    password_salt: str = None
    password_hash: str = None
    uid: int = None
    enabled: bool = False
    display_name: str = None

@dataclass
class Account:
    uid: int = None
    name: str = None
    balance: int = None
    acronym: str = None
    user: User = None

@dataclass
class TransactionFamily:
    uid: int = None
    name: str = None


@dataclass
class TransactionCategory:
    uid: int = None
    name: str = None
    user: User = None
    family: TransactionFamily = None
