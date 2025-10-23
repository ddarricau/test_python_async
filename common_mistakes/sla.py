import asyncio
from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, selectinload

Base = declarative_base()

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")

# Use in-memory SQLite in async mode
DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        p = Parent(name="Parent 1", children=[Child(name="Kid 1")])
        session.add(p)
        await session.commit()

    async with async_session() as session:
        result = await session.execute(select(Parent))
        # result = await session.execute(select(Parent).options(selectinload(Parent.children)))
        parent = result.scalars().first()
        print(f"Parent loaded: {parent.name}")
        # It will fail with a MissingGreenlet error
        print(f"Trying to access children: {parent.children[0].name}")

if __name__ == "__main__":
    asyncio.run(main())