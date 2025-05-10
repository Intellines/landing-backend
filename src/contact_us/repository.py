from sqlmodel.ext.asyncio.session import AsyncSession


class ContactUsRepository:
    def __init__(self, session: AsyncSession):
        session: AsyncSession = session

