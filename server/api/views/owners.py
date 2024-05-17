""" Owner router
"""
from fastapi import APIRouter
from server.models.owner import Owner
from server.models import storage
from fastapi import HTTPException
from server.auth.auth import *
from server.api.schemas.all_schemas import (
    OwnerModel, OwnerModelPUT, OwnerModelPWD)

owner_router = APIRouter()


@owner_router.get("/owners/")
async def get_owners():
    """ Return all owners """
    return [owner.to_dict() for owner in storage.all(Owner).values()]


@owner_router.get("/owners/{owner_id}")
async def get_owner(owner_id: str):
    """ Return a owner using its id """
    owner = storage.get(Owner, owner_id)
    if owner is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return owner.to_dict(True)


@owner_router.post("/owners/")
async def create_owner(owner: OwnerModel):
    """ Create a Owner """
    if storage.email_exists(Owner, owner.email):
        raise HTTPException(status_code=409, detail="Email already exists.")
    new_owner = Owner(**owner.__dict__)
    new_owner.save()
    return {"detail": "Owner created successfully"}


@owner_router.put("/owners/{owner_id}")
async def update_user(owner_id: str, owner: OwnerModelPUT):
    """ Update a Owner """
    ignore = ["email", "id", "created_id", "updated_at"]
    inst = storage.get(Owner, owner_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in owner.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)


@owner_router.put("/owners/password/{owner_id}")
async def update_user_password(owner_id: str, owner: OwnerModelPWD):
    """ Update a Owner password """
    target_owner = storage.get(Owner, owner_id)
    if verify_password(owner.old_password, target_owner.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    target_owner.password = owner.new_password
    target_owner.save()
    return {"detail": "Password changed successfully"}


@owner_router.delete("/owners/{owner_id}/")
async def delete_owner(owner_id: str):
    """ Delete a Owner """
    owner = storage.get(Owner, owner_id)
    if owner is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(owner)
    storage.save()
    return {"detail": "Owner deleted successfully"}
