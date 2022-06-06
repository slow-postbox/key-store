from secrets import token_bytes

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from app.sql import get_session
from app.models import KeyStore
from key import read

router = APIRouter()

auth_scheme = HTTPBearer()
token = read()


class Key(BaseModel):
    key: str
    iv: str


@router.get(
    "/key",
    description="키를 불러옵니다.",
    response_model=Key
)
async def fetch_key(owner_id: int, mail_id: int, auth=Depends(auth_scheme)):
    if auth.credentials != token:
        raise HTTPException(
            status_code=403,
            detail="invalid token detected"
        )

    session = get_session()
    key_store: KeyStore = session.query(KeyStore).filter_by(
        owner_id=owner_id,
        mail_id=mail_id
    ).first()

    if key_store is None:
        raise HTTPException(
            status_code=404,
            detail="key store not found"
        )

    return Key(
        key=key_store.key,
        iv=key_store.iv,
    )


@router.post(
    "/key",
    description="키를 생성합니다.",
    response_model=Key
)
async def create_key(owner_id: int, mail_id: int, auth=Depends(auth_scheme)):
    if auth.credentials != token:
        raise HTTPException(
            status_code=403,
            detail="invalid token detected"
        )

    key_store = KeyStore()
    key_store.owner_id = owner_id
    key_store.mail_id = mail_id
    key_store.key = token_bytes(32).hex()
    key_store.iv = token_bytes(16).hex()

    try:
        session = get_session()
        session.add(key_store)
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="already key store created"
        )

    return Key(
        key=key_store.key,
        iv=key_store.iv,
    )


@router.delete(
    "/key",
    description="키를 삭제합니다.",
)
async def delete_key(owner_id: int, mail_id: int, auth=Depends(auth_scheme)):
    if auth.credentials != token:
        raise HTTPException(
            status_code=403,
            detail="invalid token detected"
        )

    session = get_session()

    result = session.query(KeyStore).filter_by(
        owner_id=owner_id,
        mail_id=mail_id
    ).delete()

    session.commit()

    if result == 0:
        raise HTTPException(
            status_code=400,
            detail="already deleted"
        )

    return {}
