from .BaseDataModel import BaseDataModel
from .db_schemes import Asset
from sqlalchemy.future import select
from sqlalchemy import func,  delete
from bson import ObjectId

class AssetModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = db_client          


    @classmethod
    async def create_instance(cls, db_client: object):
        instance=cls(db_client)
        return instance

            
    async def create_asset(self, asset: Asset):

        async with self.db_client() as session:
            session.add(asset)
            await session.commit()
            await session.refresh(asset)

        return asset

    async def get_all_project_assets(self, asset_project_id: int, asset_type: str):

        async with self.db_client() as session:
            query=  select(Asset).where(
                Asset.asset_project_id ==  asset_project_id,
                Asset.asset_type == asset_type)
            assets = await session.execute(query)
            return assets.scalars().all()
            

    async def get_asset_record(self, asset_project_id: int, asset_name: str):

        async with self.db_client() as session:
            query=  select(Asset).where(
                Asset.asset_project_id ==  asset_project_id,
                Asset.asset_name == asset_name)
            asset = await session.execute(query)
            return asset.scalar_one_or_none()
