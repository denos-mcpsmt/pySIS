from db import Base, engine

# Drop all tables
Base.metadata.drop_all(engine)

# Create all tables
Base.metadata.create_all(engine)